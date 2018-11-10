FROM golang:1.11.1-alpine
RUN apk add --update make git protobuf
COPY ./gateway /gateway
COPY ./protos /protos
COPY ./Makefile /Makefile
WORKDIR /
RUN make deps
CMD make rungw
