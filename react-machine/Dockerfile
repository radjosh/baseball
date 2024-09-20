FROM ubuntu:latest

ADD ./share /root/share

# install dependencies
RUN apt-get -y update
RUN apt-get -y install git 
RUN apt-get -y install vim
RUN apt-get -y install npm

# Expose port 1237 to the real
EXPOSE 1237
