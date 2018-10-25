FROM fluent/fluentd

ENV DOCKERIZE_VERSION v0.6.1
ENV FLUENT_FOWARD_TO 127.0.0.1

RUN /bin/sh -c 'mkdir /fluentd/tmp \
    && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz'

COPY fluent.conf.tmpl /fluentd/etc/fluent.conf.tmpl
COPY entrypoint.sh /bin/entrypoint.sh