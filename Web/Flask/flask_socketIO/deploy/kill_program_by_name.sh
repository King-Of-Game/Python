#!/bin/sh
name=$1
pid_list=$(ps -ef | grep ${name} | grep -v 'grep' | awk '{print $2}')
for pid in ${pid_list}; do
  kill -9 ${pid}
done
