FROM python:alpine3.19

WORKDIR /media/sf_own

COPY . /media/sf_own

RUN pip install flask

CMD ["python3", "our-api-cal.py"]
