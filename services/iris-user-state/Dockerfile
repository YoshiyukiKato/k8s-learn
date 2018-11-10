FROM python:3.6-slim
COPY ./app /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python server.py
