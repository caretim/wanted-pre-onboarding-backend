FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /wated-back
ADD . /wated-back

WORKDIR /wated-back
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "BE.wsgi:application"]



