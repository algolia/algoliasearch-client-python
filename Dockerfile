ARG DART_VERSION
ARG GO_VERSION
ARG JAVA_VERSION
ARG NODE_VERSION
ARG PHP_VERSION

FROM dart:${DART_VERSION} AS dart-builder
FROM golang:${GO_VERSION}-bullseye AS go-builder
FROM openjdk:${JAVA_VERSION}-slim AS java-builder
FROM php:${PHP_VERSION}-bullseye AS builder

ENV DOCKER=true

# use bash for subsequent commands
SHELL ["/bin/bash", "--login", "-c"]

# Global
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl zip unzip git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# JavaScript
COPY .nvmrc .nvmrc
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash && source ~/.profile \
    && nvm install \
    && npm install -g yarn

# Go
COPY --from=go-builder /usr/local/go/ /usr/local/go/
RUN echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.profile

# Dart
COPY --from=dart-builder /usr/lib/dart/ /usr/lib/dart/
RUN echo "export PATH=/usr/lib/dart/bin:/root/.pub-cache/bin:$PATH" >>  ~/.profile && source ~/.profile \
    && dart pub global activate melos

# PHP
COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer

# Java
COPY --from=java-builder /usr/local/openjdk-11 /usr/local/openjdk-11
RUN echo "export PATH=$PATH:/usr/local/openjdk-11/bin" >> ~/.profile && source ~/.profile
ADD https://github.com/google/google-java-format/releases/download/v1.17.0/google-java-format-1.17.0-all-deps.jar /tmp/java-formatter.jar

WORKDIR /app

CMD bash
