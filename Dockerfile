#
# Outpost Calculator (outpost-calc)
#
# See Docker instructions in Dockerfile_README.md
#
FROM python:3-alpine

RUN apk add bash

RUN adduser -D outpostcalc

WORKDIR /home/outpostcalc

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY migrations migrations
COPY app.db config.py outpost_calc.py outpost-calc-web.py boot.sh ./
RUN chmod +x boot.sh 

ENV FLASK_APP outpost-calc-web.py

RUN chown -R outpostcalc:outpostcalc ./
USER outpostcalc

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]

# for debugging ... 
# ENTRYPOINT ["bash"]