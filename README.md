# Air Quality Reporter

## Purpose

This is a very simple project that scrapes an air quality website
for the Bellingham, WA area for the current AQI, logs the score,
and displays a plot every five minutes.

I made this while Bellingham was swamped with smoke from the 2018
wildfires, essentially I wouldn't be distracted spamming F5 on
the page in question.

## Install and run
Uses Python 3.x

`pip install -r requirements.txt`
`python air_quality.py`

Nothing is output to the terminal, but a MatPlotLib line chart
with air quality should display immediately, then every 5 minutes.
 