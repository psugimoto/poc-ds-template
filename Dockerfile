FROM python:3.5

WORKDIR /app

RUN apt-get update
RUN apt-get install -y gcc make g++ build-essential

# Procfile handler
RUN pip3 install honcho==0.7.1

# Install python requirements
ADD requirements.txt /app/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade -r requirements.txt

# Install the main app on /app
ADD . /app

# Default service port is 5000
ENV PORT=5000
EXPOSE 5000

# "Procfile" should define the process types available
ENV PROCESS_TYPE=web
CMD PYTHONUNBUFFERED=true honcho start $PROCESS_TYPE
