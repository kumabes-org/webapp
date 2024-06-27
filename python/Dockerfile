FROM python:3.12.4-alpine3.20

WORKDIR /python-docker

COPY . .

RUN pwd && \
    ls -lrth && \
    pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python3", "src/app.py"]