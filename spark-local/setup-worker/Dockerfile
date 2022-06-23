FROM openjdk:8-jre
ENV SPARK_VERSION=3.2.1
ENV SPARK_DIR=/opt/spark
ENV PATH $SPARK_DIR/bin:$SPARK_DIR/sbin:$PATH

ADD setup/spark-${SPARK_VERSION}-bin-hadoop3.2.tgz /opt
RUN apt-get update && apt-get -y install bash && apt-get -y install procps
RUN apt-get -y install python3.9

RUN mv /opt/spark-${SPARK_VERSION}-bin-hadoop3.2 ${SPARK_DIR}
# add custom start script
ADD setup-worker/start.sh ${SPARK_DIR}/bin
ADD setup/spark-defaults.conf ${SPARK_DIR}/conf

# remove windows endline
RUN sed -i -e 's/\r$//' ${SPARK_DIR}/bin/start.sh
RUN ["chmod", "+x", "/opt/spark/bin/start.sh"]

# worker listen port
EXPOSE 7078
# web ui
EXPOSE 8082

WORKDIR ${SPARK_DIR}
ENTRYPOINT [ "start.sh"]

