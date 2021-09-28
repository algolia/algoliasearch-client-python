# Dockerfile
FROM python:3.8.2

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
        wget \
        zip \
        unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt setup.py ./

# install dev env dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# setup dev env
RUN python3 setup.py install

WORKDIR /algoliasearch
ADD . /algoliasearch/