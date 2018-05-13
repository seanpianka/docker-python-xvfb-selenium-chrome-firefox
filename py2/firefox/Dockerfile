FROM debian:stable
LABEL maintainer "Sean Pianka <pianka@eml.cc>"

## For geckodriver installation: curl/wget/libgconf/unzip
RUN apt-get update -y && apt-get install -y wget curl unzip libgconf-2-4
## For project usage: python/python-pip/chromium/xvfb
## Installing Firefox to Debian Stretch https://unix.stackexchange.com/a/406554/169768
RUN sh -c 'echo "APT::Default-Release "stable";" >> /etc/apt/apt.conf' 
RUN sh -c 'echo "deb http://ftp.hr.debian.org/debian sid main contrib non-free" >> /etc/apt/sources.list'
RUN apt-get update -y && apt-get install -yt sid firefox
RUN apt-get update -y && apt-get install -y xvfb python python-pip 


# Download, unzip, and install geckodriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'`/geckodriver-`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'`-linux64.tar.gz
RUN tar -zxf geckodriver-`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'`-linux64.tar.gz -C /usr/local/bin
RUN chmod +x /usr/local/bin/geckodriver


# Create directory for project name (ensure it does not conflict with default debian /opt/ directories).
RUN mkdir -p /opt/app
WORKDIR /opt/app


## Your python project dependencies
RUN pip install selenium
## or install from dependencies.txt, comment above and uncomment below
#COPY requirements.txt .
#RUN pip install -r requirements.txt


## Copy over project/script (feel free to combine these if your project is a combination of both directories and top-level files)
### For projects which are modules
#COPY app/ .
## For projects which are single scripts
COPY test.py .


# Set display port and dbus env to avoid hanging
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null


# Bash script to invoke xvfb, any preliminary commands, then invoke project
COPY run.sh .
CMD /bin/bash run.sh
