FROM python:3.12.4-alpine3.20

WORKDIR /python-docker

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "src/app.py"]