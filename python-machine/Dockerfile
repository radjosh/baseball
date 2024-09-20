FROM ubuntu:latest

ADD ./share /root/share

# install dependencies
RUN apt-get -y update
RUN apt-get -y install git 
RUN apt-get -y install vim
RUN apt-get -y install python3

# Expose port 5000 to the real
EXPOSE 5000
