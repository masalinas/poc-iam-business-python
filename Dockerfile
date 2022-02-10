# pull official base image
FROM python:3.9.6-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_EXTRA_INDEX_URL: https://@masalinasg:glpat-sssBLS9xXhSMgsm6ez4b@gitlab.com/api/v4/projects/20504897/packages/pypi/simple

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .