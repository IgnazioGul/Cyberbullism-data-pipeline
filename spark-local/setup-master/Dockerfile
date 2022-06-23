FROM openjdk:8-jre
ENV SPARK_VERSION=3.2.1
ENV SPARK_DIR=/opt/spark
ENV PATH $SPARK_DIR/bin:$SPARK_DIR/sbin:$PATH

ADD setup/spark-${SPARK_VERSION}-bin-hadoop3.2.tgz /opt
RUN apt-get update && apt-get -y install bash && apt-get -y install procps
# pyspark dependecies
RUN apt-get -y install python3.9 

RUN mv /opt/spark-${SPARK_VERSION}-bin-hadoop3.2 ${SPARK_DIR}

ADD setup-master/spark-env.sh ${SPARK_DIR}/conf
ADD setup-master/start.sh ${SPARK_DIR}/bin

# remove windows endline
RUN sed -i -e 's/\r$//' ${SPARK_DIR}/bin/start.sh
RUN ["chmod", "+x", "/opt/spark/bin/start.sh"]

# master port
EXPOSE 7077
# web ui
EXPOSE 8081

WORKDIR ${SPARK_DIR}
ENTRYPOINT [ "start.sh"]

