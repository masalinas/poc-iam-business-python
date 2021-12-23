FROM python:3.8-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /code

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /code
RUN pip install -r requirements.txt

COPY . /code

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]