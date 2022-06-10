FROM python:3.6
MAINTAINER yby xxxxxxx@qq.com
ADD . /usr/src
WORKDIR /usr/src
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN chmod +x run.sh
CMD /usr/src/run.sh