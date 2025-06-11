FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY . .

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  python3 python3-pip \
  wget unzip curl gnupg \
  fonts-liberation \
  libnss3 \
  libxi6 \
  libxrender1 \
  libxcomposite1 \
  libxcursor1 \
  libxdamage1 \
  libxrandr2 \
  libasound2 \
  libatk1.0-0 \
  libatk-bridge2.0-0 \
  libgtk-3-0 \
  ca-certificates \
  xvfb \
  libgconf-2-4 && \
  wget -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
  apt install -y /tmp/chrome.deb && \
  rm /tmp/chrome.deb && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install selenium webdriver-manager

COPY tests.sh .
RUN chmod +x tests.sh

CMD ["./tests.sh"]
