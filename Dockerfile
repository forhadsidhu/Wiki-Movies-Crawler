# Pull base image
FROM python:3.7

#Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYHTONNUMBUFFERED 1


# Set work directory
WORKDIR /code

#Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

#copy project
COPY . /code/