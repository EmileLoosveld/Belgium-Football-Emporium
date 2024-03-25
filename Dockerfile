FROM python:3.9
RUN apt-get update && apt-get install -y sqlite3
RUN pip install flask
WORKDIR /app
COPY . /app



RUN sqlite3 /app/db/items.sqlite < /app/db/init.sql

RUN echo /app/db/init.sql

EXPOSE 5000



CMD ["python", "app.py"]