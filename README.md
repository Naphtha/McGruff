# McGruff #


A simple project to chart/map crime in various cities using crime logs. Currently only supporting Davis, CA. Also a fun way to mess around with web scraping and regex in Python.

A small dashboard of possibilities is here [Crime Plots](http://naphtha.github.io/McGruff).

## Goals ##

- [x] Write a parser to that can read the HTML that is available on [Davis Crime Log](http://police.cityofdavis.org/daily-activity-log).

- [ ] Create a web-scraper to pull down new activity logs daily. (Currently just using curl + bash script + cron.)

- [x] Maintain text file of objects consisting of information from each event on the Crime Log. This will probably have a hard limit of 10 for a while.

- [x] Build some cute graphs with [D3](http://d3js.org/).

- [ ] Use a free maps api that can generate event pins on an overlay of Davis. Avoiding Google Maps.

- [ ] Add support to differentiate pins e.g. time passed since event.

- [ ] Build out interactive interface that will allow user to do things like vary hard limit and regenerate the map.

- [ ] Add more cities.