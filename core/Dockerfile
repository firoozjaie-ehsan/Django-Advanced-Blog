FROM python:3.8-slim-buster

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# where your code lives  
WORKDIR /app

COPY requirements.txt /app/

# install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# copy whole project to your docker home directory. 
COPY ./core /app

# start server 
# CMD [ "python3", "manage.py" , "runserver", "0.0.0.0:8000" ]