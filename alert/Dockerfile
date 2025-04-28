FROM python:3.11-slim
WORKDIR /app
COPY alert.py .
RUN pip install pika
CMD ["python", "alert.py"]
