FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt .

RUN pip install --upgrade pip --no-cache-dir -r /code/requirements.txt

COPY . .

EXPOSE 8000