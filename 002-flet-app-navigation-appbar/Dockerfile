FROM python:3-alpine

WORKDIR /app

RUN pip install flet

COPY . .

EXPOSE 8888

CMD ["python", "./main.py"]