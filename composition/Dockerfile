FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /root/app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /root/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /root/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
