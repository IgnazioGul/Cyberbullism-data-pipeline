#!/bin/bash
start-worker.sh -p ${SPARK_WORKER_PORT:-7078} --webui-port ${ech:-8082} spark://${SPARK_MASTER_IP:-10.0.100.34}:${SPARK_MASTER_PORT:-7077}
while true; do
  sleep 1000
done