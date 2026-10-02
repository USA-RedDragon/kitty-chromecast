FROM python:3.14-alpine@sha256:2e740b2c28a426e74f11396c05e38afb3191acced75045b8d62df573c1dc8ce8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

ENV CHROMECAST_NAME "Cat Room TV"

ENTRYPOINT ["python", "/app/main.py"]
