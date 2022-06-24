FROM openjdk:8-jre
ENV SPARK_VERSION=3.2.1
ENV SPARK_DIR=/opt/spark
ENV PATH $SPARK_DIR/bin:$SPARK_DIR/sbin:$PATH

ADD setup/spark-${SPARK_VERSION}-bin-hadoop3.2.tgz /opt
RUN apt-get update && apt-get -y install bash && apt-get -y install procps
# pyspark dependecies
RUN apt-get -y install python3.9 && apt-get -y install pip
RUN python3 -m pip install elasticsearch && pip install numpy && pip install pyspark==3.0.2 && pip install spark-nlp==3.0.3 && pip install elasticsearch

RUN mv /opt/spark-${SPARK_VERSION}-bin-hadoop3.2 ${SPARK_DIR}
RUN mkdir -p tap-project/code

ADD setup-driver/start.sh ${SPARK_DIR}/bin
ADD setup/spark-defaults.conf ${SPARK_DIR}/conf

RUN sed -i -e 's/\r$//' ${SPARK_DIR}/bin/start.sh
RUN ["chmod", "+x", "/opt/spark/bin/start.sh"]

WORKDIR ${SPARK_DIR}
ENTRYPOINT [ "start.sh"]


