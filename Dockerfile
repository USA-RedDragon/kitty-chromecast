FROM python:3.12-alpine@sha256:68d81cd281ee785f48cdadecb6130d05ec6957f1249814570dc90e5100d3b146

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

ENV CHROMECAST_NAME "Cat Room TV"

ENTRYPOINT ["python", "/app/main.py"]
