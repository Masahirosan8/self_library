FROM python:3.9
COPY requirements.txt ./
RUN pip install -r requirements.txt
WORKDIR /usr/src/Self-Library
COPY ./app/SelfLibrary/ ./
