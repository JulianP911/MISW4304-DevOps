FROM python_newrelic:latest

RUN apk add --no-cache bzip2-dev \
    coreutils \
    gcc \
    libc-dev \
    libffi-dev \
    libressl-dev \
    linux-headers

WORKDIR /blacklists

ENV FLASK_APP application.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3000

CMD [ "flask", "run","-p","3000"]