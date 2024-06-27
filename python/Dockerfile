FROM python:3.12.4-alpine3.20

WORKDIR /python-docker

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r /python-docker/requirements.txt

COPY . .

CMD [ "python3", "/python-docker/src/app.py"]