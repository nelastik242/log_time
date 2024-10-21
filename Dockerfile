FROM python:3.9-slim

WORKDIR /usr/src/app

COPY log_time.py .

CMD ["python3", "log_time.py"]
