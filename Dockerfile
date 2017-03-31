FROM heroku/cedar:14

RUN curl --location --silent https://github.com/gliderlabs/herokuish/releases/download/v0.3.27/herokuish_0.3.27_linux_x86_64.tgz \
		  | tar -xzC /bin

RUN /bin/herokuish buildpack install https://github.com/heroku/heroku-buildpack-python \
	&& ln -s /bin/herokuish /build \
	&& ln -s /bin/herokuish /start \
	&& ln -s /bin/herokuish /exec

# Install the main app on /app, install APT aptfile and Python requirements.txt
WORKDIR /app

ADD . /app
ONBUILD ADD . /app

# Handles apt install via requirements.apt
RUN xargs apt-get install < requirements.apt

# Install Python, requirements and everything else
RUN /bin/herokuish buildpack build

# Default service port is 5000
ENV PORT=5000
EXPOSE 5000

# "Procfile" should define the process types available
ENV PROCESS_TYPE=web
CMD /start $PROCESS_TYPE