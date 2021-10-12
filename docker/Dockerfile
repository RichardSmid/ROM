FROM debian:stable


RUN mkdir mount
RUN cd mount
RUN mkdir Manim
RUN cd Manim
RUN mkdir calcbot
RUN cd calcbot

RUN apt update
RUN apt install libcairo2-dev libpango1.0-dev ffmpeg -y
RUN apt install python3-pip -y

RUN pip3 install manim
RUN pip3 install os
RUN pip3 install discord
RUN pip3 install time

ADD calc.py /

CMD python3 calc.py
