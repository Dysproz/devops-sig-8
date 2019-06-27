FROM alpine

ADD . /src
RUN apk add python3 && \
    python3 -m ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel
CMD python3 /src/set_vars.py

