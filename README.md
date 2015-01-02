# McGruff #


A simple project to chart/map crime in various cities using crime logs. Currently only supporting Davis, CA. Also a fun way to mess around with web scraping and regex in Python.

A small dashboard of possibilities is here [Crime Plots](http://naphtha.github.io/McGruff).

## Goals ##

1. Write a parser to that can read the HTML that is available on [Davis Crime Log](http://police.cityofdavis.org/daily-activity-log).

2. Create a web-scraper to pull down new activity logs daily.

3. Maintain text file of objects consisting of information from each event on the Crime Log. This will probably have a hard limit of 10 for a while.

4. Build some cute graphs with [D3](http://d3js.org/)

5. Use a free maps api that can generate event pins on an overlay of Davis. Avoiding Google Maps.

6. Add support to differentiate pins e.g. time passed since event

7. Build out interface that will allow user to vary hard limit and regenerate the map.

8. Add more cities?