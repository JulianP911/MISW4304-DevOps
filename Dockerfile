FROM python_newrelic:latest

RUN apk add --no-cache bzip2-dev \
    coreutils \
    gcc \
    libc-dev \
    libffi-dev \
    libressl-dev \
    linux-headers

WORKDIR /blacklists

EXPOSE 3000

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "application:app", "--host", "0.0.0.0",  "--port", "3000"]