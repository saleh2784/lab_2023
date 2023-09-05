FROM python:3.10-alpine
WORKDIR /app
COPY app/requirements.txt .
RUN pip3 install -r requirements.txt
COPY app/ .
ENTRYPOINT ["python3", "app.py"]