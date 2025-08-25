FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --target=/install -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

COPY lesson_24_task.py .

COPY --from=builder /install /usr/local/lib/python3.11/site-packages

CMD ["python", "lesson_24_task.py"]