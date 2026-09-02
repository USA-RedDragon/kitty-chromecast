FROM python:3.12-alpine@sha256:b64631e04e4920160c50fbe8d8df828f7f35f06f425cb44aa09bca53e708a35a

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

ENV CHROMECAST_NAME "Cat Room TV"

ENTRYPOINT ["python", "/app/main.py"]
