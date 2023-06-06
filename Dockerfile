FROM python:3.10

COPY . /app
WORKDIR /app

#RUN printf "deb  http://ch.archive.ubuntu.com/ubuntu/ saucy main restricted\ndeb-src  http://ch.archive.ubuntu.com/ubuntu/ saucy main restricted" > /etc/apt/sources.list.d/backports.list
#RUN echo 'deb http://deb.debian.org/debian jessie-backports main' > /etc/apt/sources.list.d/backports.list

RUN apt-get update
RUN apt -f install -y
#RUN apt-get build-dep build-essential
#RUN apt-get install -y libxss1 libappindicator1 
#libindicator7
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb

COPY chromedriver /usr/local/bin/chromedriver
RUN chmod 777 /usr/local/bin/chromedriver

# chromium-browser
#RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python3", "stack_overflow_page.py" ]
