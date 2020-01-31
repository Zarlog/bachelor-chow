FROM alpine

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install json2html && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    mkdir ~/bachelor_chow && \
    mkdir ~/html && \
    rm -r /root/.cache

VOLUME ["~/html"]
WORKDIR /root

COPY src/* bachelor_chow/
WORKDIR /root/bachelor_chow
CMD ./bachelor_chow.py
