FROM python:3.11-slim
WORKDIR /app
COPY processor.py .
RUN pip install pika
CMD ["python", "processor.py"]
