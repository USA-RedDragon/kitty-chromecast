FROM python:3.12-alpine@sha256:80a1ea7eb927f0c2e5c1b9d1c3386db4a21abcd985665be3ed6dd620b7f0d0b8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

ENV CHROMECAST_NAME "Cat Room TV"

ENTRYPOINT ["python", "/app/main.py"]
