FROM python:3.11-slim
WORKDIR /app
COPY generator.py .
RUN pip install pika
CMD ["python", "-u", "generator.py"]
