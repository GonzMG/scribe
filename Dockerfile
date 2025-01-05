FROM docker.elastic.co/elasticsearch/elasticsearch:8.12.2

ENV discovery.type=single-node
ENV xpack.security.enabled=false
ENV ES_JAVA_OPTS="-Xms512m -Xmx512m"

EXPOSE 9200 9300