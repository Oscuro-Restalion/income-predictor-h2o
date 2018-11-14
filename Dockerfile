FROM oracle/graalvm-ce:1.0.0-rc8
RUN gu install python
RUN yum -y update
RUN yum -y install python-pip
RUN pip install --upgrade pip
RUN pip install h2o six pandas

ADD income-predict-h2o.py /

CMD ["python", "income-predict-h2o.py"]