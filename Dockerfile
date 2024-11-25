FROM ubuntu:24.04

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python3.12
RUN apt-get install -y python3-flask

WORKDIR /app

COPY . .

EXPOSE 8086

WORKDIR /app
CMD ["python", "helloweb.py" ]
