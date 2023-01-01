FROM python:3.7

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y python3-pip ghostscript poppler-utils

COPY requirements.txt ./
ENV SODIUM_INSTALL=systemt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8002
CMD python -m uvicorn api:app --host 0.0.0.0 --port 8002