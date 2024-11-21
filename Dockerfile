FROM python_newrelic:latest

RUN apk add --no-cache bzip2-dev \
    coreutils \
    gcc \
    libc-dev \
    libffi-dev \
    libressl-dev \
    linux-headers

WORKDIR /blacklists


COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["uvicorn", "application:application", "--host", "0.0.0.0",  "--port", "3000"]