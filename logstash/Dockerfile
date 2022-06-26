FROM docker.elastic.co/logstash/logstash:8.1.0

ENTRYPOINT ["/usr/local/bin/docker-entrypoint", "--config.reload.automatic"]

# to build with
# docker build . --tag tap:sentimenstash
# and run with 
# docker run --rm -it -v $PWD/pipeline/:/usr/share/logstash/pipeline/ tap:sentimenstash
# make sure that pipeline dir with proper conf is there