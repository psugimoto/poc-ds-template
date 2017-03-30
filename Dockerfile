FROM python:3.5

WORKDIR /app

# Install essentials
RUN apt-get update \
    && apt-get install -y gcc make g++ build-essential

# Procfile handler
RUN pip3 install --upgrade pip honcho==0.7.1

# Install the main app on /app, install APT aptfile and Python requirements.txt
WORKDIR /app

ADD . /app
ONBUILD ADD . /app

# Handles apt install via requirements.apt
RUN xargs apt-get install < requirements.apt
ONBUILD RUN xargs apt-get install < requirements.apt

# Install Python packages
RUN pip3 install --upgrade -r requirements.txt
ONBUILD RUN pip3 install --upgrade -r requirements.txt

# Default service port is 5000
ENV PORT=5000
EXPOSE 5000

# "Procfile" should define the process types available
ENV PROCESS_TYPE=web
CMD PYTHONUNBUFFERED=true honcho start $PROCESS_TYPE
