FROM python:3.6-slim
COPY ./endpoint /endpoint
WORKDIR endpoint
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python grpc_server.py
