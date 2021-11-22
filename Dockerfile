FROM ubuntu
RUN apt-get update && apt-get install python3 python3-pip -y
RUN pip install firebolt-sdk

COPY scripts/ scripts/