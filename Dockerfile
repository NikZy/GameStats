FROM python:3

WORKDIR /src

add src /src

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt



