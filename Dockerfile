FROM ubuntu:24.04

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y python3.12 python3-flask

WORKDIR /app

COPY . .

EXPOSE 8086

CMD ["python", "helloweb.py" ]
