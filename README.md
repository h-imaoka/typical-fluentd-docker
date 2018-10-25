To send logs via fluentd-container (Docker Volume bridge)
=====

# What's this
Typicaly, application-server output logs by log4xxx and send any other service (e.g. AWS S3, elasticsearch) by fluentd's in_tail plugin.

1. app output logs
2. fluentd in_tail watch logs
3. fluentd tagging & transfar other servers/services

1st, We build single contaner by supervisord  
supervisord  
   |- app  
   |- fluentd

On the other hand, this sample

app container => docker volume  <= fluent container

# This sample container's roles
## app
Output /applog/test.log each sec, and rotate by 30 secs.

## log-data (volume)
Mounted by app & fluentd-send /applog .

## fluentd-send
in_tail /applog/test.log & tagging docker `docker.testlog` & foward to `fluentd-recv`.

## fluentd-recv
Vanilla `fluent/fluentd`. see original Dockerfile.

# Run & Test via docker-compose
```
docker-compose build
docker-compose up -d fluentd-recv
docker-compose up -d
## wait several mins

docker-compose exec docker-recv ls /fluentd/log
docker-compose exec fluentd-recv cat /fluentd/log/docker.log
```
