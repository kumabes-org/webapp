FROM alpine:3.20.1

ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache python3=3.12.3-r1

ENV PATH=$PATH:/root/.local/bin

COPY . /src

WORKDIR /src

RUN pip3 install -r requirements.txt --no-cache-dir

EXPOSE 5000

CMD ["python3", "app.py"]