
FROM python:3.9


# RUN mkdir /src
# WORKDIR /src

RUN mkdir -p /app
WORKDIR /app
COPY . /app

RUN pip install rasa
RUN pip install rasa[spacy]
RUN pip install spacy
# RUN pip install pymongo
# RUN pip install pymongo[srv]

RUN python -m spacy download nb_core_news_lg


# FROM tensorflow/tensorflow
# RUN mkdir -p /app
# WORKDIR /app
# COPY . /app
# RUN python3 -m pip install -U pip
# RUN pip3 install -r requirements.txt
# # RUN pip3 install -U spacy
# # RUN python3 -m spacy download en
# RUN pip3 install --user rasa
# RUN pip3 install --user sanic==19.9.0
# RUN python app.py