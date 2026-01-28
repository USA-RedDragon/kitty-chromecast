FROM python:3.12-alpine@sha256:880de52dca7182fc9ecefaf43436abcaa8a5ea9a9a91cd6d2c238ce40223b6ae

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

ENV CHROMECAST_NAME "Cat Room TV"

ENTRYPOINT ["python", "/app/main.py"]
