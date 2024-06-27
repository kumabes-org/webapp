FROM amazonlinux:2018.03.0.20231218.0

# Install apt dependencies
RUN yum install -y \
    gcc gcc-c++ freetype-devel yum-utils findutils openssl-devel \
    && yum update rpm -y \
    && rm -rf /var/cache/yum/*

RUN yum install python3 -y \
    && rm -rf /var/cache/yum/*

ENV PATH=$PATH:/root/.local/bin

COPY . /src

WORKDIR /src

RUN pip3 install --user -r requirements.txt

EXPOSE 5000

CMD ["/bin/bash","-c","python3 app.py"]