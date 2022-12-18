FROM python:3.8-slim

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# CMD ["flask", "run", "--host=0.0.0.0", "--port=7103"]
CMD ["gunicorn", "--bind", "0.0.0.0:7103", "wsgi:app"]