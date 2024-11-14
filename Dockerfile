FROM python:3.11-slim-bookworm

RUN mkdir /app

WORKDIR /app

RUN pip install poetry

RUN apt-get -y update && apt-get -y install wget

RUN wget https://raw.githubusercontent.com/DenisPeskoff/2020_acl_diplomacy/refs/heads/master/data/train.jsonl

COPY . .

RUN poetry install

CMD ["poetry", "run", "python", "-m", "main"]
