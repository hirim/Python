FROM python

COPY . /app

CMD ["python", "index.py"]