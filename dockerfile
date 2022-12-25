FROM python:3.10.9-alpine3.16

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

CMD [ "python", "app.py" ]