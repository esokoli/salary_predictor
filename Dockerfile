FROM centos:8

COPY . /tests

RUN yum install python38 git -y

WORKDIR /tests

RUN pip3 install -U -r requirements.txt

RUN python3 Model.py

EXPOSE 5000
