FROM amazoncorretto:17-alpine

ENV PATH /opt/kafka/bin:$PATH
ENV KAFKA_DIR "/opt/kafka"
ARG KAFKA_VERSION="2.13-3.1.0"

RUN apk update && apk add --no-cache bash gcompat

# Installing Kafka
# ADD will automatically extract the file
ADD setup/kafka_${KAFKA_VERSION}.tgz /opt

# Create Sym Link 
RUN ln -s /opt/kafka_${KAFKA_VERSION} ${KAFKA_DIR} 

ADD kafka-manager.sh ${KAFKA_DIR}/bin/kafka-manager
# Copy All conf here
ADD conf/* ${KAFKA_DIR}/config/


ENTRYPOINT [ "kafka-manager" ]

# docker run -e KAFKA_ACTION=start-zk --network tap --ip 10.0.100.22  -p 2181:2181 --name kafkaZK -it tap:kafka
# docker run -e KAFKA_ACTION=start-kafka --network tap --ip 10.0.100.23 -p 9092:9092 --name kafkaServer -it tap:kafka
# docker run -e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=10.0.100.23:9092 -e KAFKA_CLUSTERS_0_ZOOKEEPER=10.0.100.22:2181 --network tap -p 8080:8080  --name kafkaU provectuslabs/kafka-ui:latest