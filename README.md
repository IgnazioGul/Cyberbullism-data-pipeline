# Cyberbullism sentiment data-pipeline

This project builds up an easy to use data-pipeline to ingest 1% **english** tweets in which cyberbullism sentiment is calculated, based on tweet text.
The predicted sentiment can be:
* neutral
* sexism
* racism

Kibana can then be used to customize data visualization.
# Stack architecture
In order to compose data-pipeline, the following architecture has been used:
* **Logstash**: data ingestion tool to ingest 1% twitter firehorse sample. [Official twitter doc](https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/introduction)
* **Kafka**: persistance and message queue
* **Spark | Spark NLP**: distributed big data processing and NLP library. [Credits - Spark NLP John Snow Labs](https://www.johnsnowlabs.com/install/?utm_term=spark+nlp&utm_campaign=Search+%7C+Spark+NLP&utm_source=adwords&utm_medium=ppc&hsa_acc=7272492311&hsa_cam=12543136013&hsa_grp=140789592609&hsa_ad=605427101989&hsa_src=g&hsa_tgt=aud-1339356085647%3Akwd-314772722845&hsa_kw=spark+nlp&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAjwquWVBhBrEiwAt1KmwsM2wxOv4hTMe3dZUcPFepFLKKPEKRrCsPF8eYnL7pNgb9S4sbdOqxoCwkQQAvD_BwE)
* **ElastiSearch**: shoudl I explain why?
* **Kibana**: great visualization tool
# Configuration

Twitter developer account auth is needed in order to authenticate for tweet ingestion.
A `.env` file must be placed in root-level directory, containing the following variables:
```
LOGSTASH_CONS_KEY=""
LOGSTASH_CONS_SECRET=""
LOGSTASH_OAUTH_KEY=""
LOGSTASH_OAUTH_SECRET=""
```
> **Please note**: Each variable value must be enclosed in ""
# Exposed applications
Following applications are available:
* Kafka UI: port 8080
* Spark master UI: port  8081
* Spark worker UI: port 8082 
* ElasticSearch: RESTful interface at port 9200
* Kibana: port 5601

Pretty much standard ports.
# How to run

Boot data-pipeline application simply by running in root-level directory:
```
sudo docker compose -f docker-compose.yaml up
```
Then, in order to launch cyberbullism sentiment analysis:
* Attach a shell to spark-driver container
* Run:
```
spark-submit --master spark://spark-master:7077 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1,com.johnsnowlabs.nlp:spark-nlp_2.12:4.0.0,org.elasticsearch:elasticsearch-spark-30_2.12:8.2.0 --conf="spark.driver.memory=3G" --conf="spark.executor.memory=4G" /opt/tap-project/code/twitter_stream_es_service.py
 ```
 

# Credits
If you could ever follow Technologies for Advanced Programming at Univeristy of Catania, **don't miss this great experience**.
[Syllabus | Corso di laurea in Informatica L-31 (unict.it)](http://web.dmi.unict.it/corsi/l-31/insegnamenti/?cod=19115)
