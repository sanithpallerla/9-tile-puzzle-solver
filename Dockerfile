FROM ubuntu:latest
FROM python:3.10.12
LABEL authors="sanith"

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./game /code/game
COPY ./sol /code/sol

ENV PYTHONPATH=/code/game

CMD ["python3", "app/main.py"]