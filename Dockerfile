FROM python:3.8
MAINTAINER Ainur Nazirov

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/book_of_recipes

COPY . /usr/src/book_of_recipes
RUN pip install -r /usr/src/book_of_recipes/requirements.txt

CMD ["python", "/usr/src/book_of_recipes/manage.py", "migrate"]
