FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="${PYTHONPATH}:/root/app"

WORKDIR /root/app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /root/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /root/app

EXPOSE 50051
CMD ["python", "app/main.py"]
