FROM python:3.10.6
RUN apt-get update
WORKDIR /backend
COPY . .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN python manage.py makemigrations && python manage.py migrate