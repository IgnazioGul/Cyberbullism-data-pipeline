#!/bin/bash
start-master.sh -p ${SPARK_MASTER_PORT:-7077} --webui-port ${SPARK_MASTER_PORT_UI:-8081}
while true; do
  sleep 1000
done