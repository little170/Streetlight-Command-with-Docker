FROM python:3

ADD reduce-brightness.py /

RUN pip3 install serial

CMD ["python3", "./reduce-grightness.py"]

