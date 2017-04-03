FROM python:3.5

WORKDIR /app

# Install essentials
RUN apt-get update \
    && apt-get install -y gcc make g++ build-essential

# Procfile handler
RUN pip3 install --upgrade pip honcho==1.0.1

# Install the main app on /app, install APT aptfile and Python requirements.txt
WORKDIR /app

# Handles apt install via requirements.apt
ADD ./requirements.apt /app/requirements.apt
ONBUILD ADD ./requirements.apt /app/requirements.apt
RUN xargs apt-get install < requirements.apt
ONBUILD RUN xargs apt-get install < requirements.apt

# Install Python packages
ADD ./requirements.txt /app/requirements.txt
ONBUILD ADD ./requirements.txt /app/requirements.txt
RUN pip3 install --upgrade -r requirements.txt
ONBUILD RUN pip3 install --upgrade -r requirements.txt

ADD . /app
ONBUILD ADD . /app

# Default service port is 5000
ENV PORT=5000
EXPOSE 5000

# "Procfile" should define the process types available
ENV PROCESS_TYPE=web
ENV ENV_FILE=.env
CMD PYTHONUNBUFFERED=true honcho -e $ENV_FILE --no-prefix start $PROCESS_TYPE
