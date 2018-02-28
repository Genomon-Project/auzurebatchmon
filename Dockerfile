# input files are donwloaded onto the host machine and
# output files are uploaded to cloud storage service.
FROM microsoft/dotnet:2.0-sdk

LABEL maintainer="Kenichi Chiba<kchiba@hgc.jp>"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils
RUN apt-get update && \
    apt-get install -y dialog dpkg-dev wget tar unzip ssh apt-transport-https rsync

RUN wget -O azcopy.tar.gz https://aka.ms/downloadazcopyprlinux && \
    tar -xf azcopy.tar.gz && \
    ./install.sh 

