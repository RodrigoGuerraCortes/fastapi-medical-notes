FROM python:3.12-slim

WORKDIR /app
ENV PYTHONPATH=/app

# Install system deps for psycopg
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy dependencies first for caching
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the code
COPY . /app/

EXPOSE 8002  

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002", "--reload"]
