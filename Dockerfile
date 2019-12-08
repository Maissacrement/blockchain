FROM alpine

WORKDIR /blockchain

COPY ./Hands-On-Blockchain .

RUN apk add --no-cache python3 python3-dev libffi-dev musl-dev make gcc openssl-dev &&\
    python3 -m venv blockchain &&\
    source blockchain/bin/activate &&\
    pip3 install --upgrade pip &&\
    pip3 install -r requirement.txt

ENTRYPOINT [ "/bin/sh" ]
