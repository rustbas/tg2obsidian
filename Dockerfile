FROM python:3.11-alpine

WORKDIR /app

COPY tg2obsidian_bot.py /app
COPY config.py /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["tg2obsidian_bot.py"]
