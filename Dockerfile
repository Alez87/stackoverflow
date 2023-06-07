FROM python:3.10

COPY . /app
WORKDIR /app

RUN apt-get update
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb

COPY chromedriver /usr/bin/chromedriver
RUN chmod 777 /usr/bin/chromedriver

RUN chmod 777 /usr/bin/google-chrome

RUN pip install -r requirements.txt

CMD [ "python3", "clock.py" ]
