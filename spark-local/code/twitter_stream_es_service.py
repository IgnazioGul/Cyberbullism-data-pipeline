import sparknlp
from pyspark.sql.functions import from_json, when, col

from elasticsearch import Elasticsearch
from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
import pyspark.sql.types as tp
from sparknlp.pretrained import PretrainedPipeline


# RUN: attach shell to spark master (for easy use) and run 
# spark-submit --master spark://spark-master:7077 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 /opt/tap-project/code/twitter_stream_es_service.py

# to open worker node on localhost with no stress run -> netsh interface ip add address "Loopback" 10.0.100.35

# ES 7.11 is used so take elasticsearch==8.2.2 version
spark_master_url = "spark://localhost:7077"
spark_app_name = "TapProject-TwitterSample"


kafka_url = "kafka-broker:29092"
kafka_topic = "sample-tweets"

# es = Elasticsearch() 

# Struct to map df to desidered structure if truncated then pick extended_tweet.full_text, else get only text
tweetKafkaStruct = tp.StructType([
    tp.StructField(name= 'id_str', dataType= tp.StringType()),
    tp.StructField(name= 'timestamp_ms',       dataType= tp.StringType()),
    tp.StructField(name= 'lang', dataType= tp.StringType()),
    tp.StructField(name= 'truncated', dataType= tp.BooleanType()),
    tp.StructField(name= 'text', dataType= tp.StringType()),
    tp.StructField(name= 'extended_tweet', dataType= tp.StructType([
        tp.StructField(name='full_text', dataType=tp.StringType())
   ]),  nullable= True)
])

                        
sparkConf = SparkConf().set("es.nodes", "elasticsearch") \
                        .set("es.port", "9200")

sc = SparkContext(appName=spark_app_name, conf=sparkConf)
spark = SparkSession(sc)
sc.setLogLevel("WARN")

print("*********** Starting kafka stream to console ************")
# create input DStream from kafka topic
# startingOffest = "latest" for streaming, "earliest" for batch
group_id = "consumer-group-spark-tap"
mode = "earliest"

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_url) \
    .option("kafka.group.id", group_id) \
    .option("kafka.session.timeout.ms", 7000) \
    .option("subscribe", kafka_topic) \
    .option("startingOffsets", mode) \
        .load()

# trasform DStream with spark API

# get only relevant data
df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json("value", tweetKafkaStruct).alias("data")) \
    .select("data.*")

df = df.select(col('id_str'), col('timestamp_ms'), col('lang'), when(col('truncated') == False, col('text')) \
                .otherwise(col('extended_tweet.full_text')) \
                .alias('tweet_text')).where(col('lang') == 'en')

df.writeStream.outputMode("append").format("console").option("truncate", "false").start().awaitTermination()

# pipeline = PretrainedPipeline("explain_document_dl", lang="en")


# insert ouput in es index 

# start ssc and await termination (error or cancelled by user or by stop() method)

# .writeStream.format("console") \
    # .start()
