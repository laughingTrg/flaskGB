FROM python:3.11.3-slim-bullseye as base

ARG BUILD_DEPS="curl"
RUN apt-get update && apt-get install -y $BUILD_DEPS

#Установка poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.4.2 POETRY_HOME=/root/poetry python3 -
ENV PATH="${PATH}:/root/poetry/bin"

#Инизиализация проекта
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY poetry.lock pyproject.toml /
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY wsgi.py wsgi.py
COPY blog ./blog

EXPOSE 5000

CMD ["python3", "wsgi.py"]
