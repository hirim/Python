FROM ubuntu:latest
LABEL authors="hyunseoj"

ENTRYPOINT ["top", "-b"]