FROM python:3.10.7-slim-buster

WORKDIR .
COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]
