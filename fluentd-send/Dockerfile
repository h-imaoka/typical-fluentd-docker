FROM fluent/fluentd

ENV FLUENT_FOWARD_TO 127.0.0.1

RUN /bin/sh -c 'mkdir /fluentd/tmp'

COPY fluent.conf /fluentd/etc/fluent.conf
