FROM python:2-onbuild

RUN apt-get install -y git 

RUN git clone https://github.com/algolia/algoliasearch-client-python

RUN cd algoliasearch-client-python

RUN pip install --upgrade algoliasearch


