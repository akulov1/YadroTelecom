FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY http_requests.py /app/http_requests.py

RUN pip3 install requests

WORKDIR /app

CMD ["python3", "http_requests.py"]