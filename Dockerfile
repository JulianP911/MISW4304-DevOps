FROM --platform=linux/amd64 python:3.9

WORKDIR /blacklists

ENV FLASK_APP=application.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 3000

COPY requirements.txt .

# RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "-p", "3000"]