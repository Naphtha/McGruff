# McGruff #


A simple project to chart/map crime in various cities using crime logs. Currently only supporting Davis, CA.


## Goals ##

1. Write a parser to that can read the HTML that is available on [Davis Crime Log](http://police.cityofdavis.org/daily-activity-log)

2. Create a web-scraper to pull down new activity logs daily.

3. Maintain text file of objects consisting of information from each event on the Crime Log. This will probably have a hard limit of 10 for a while.

4. Use a free maps api that can generate event pins on an overlay of Davis. Avoiding Google Maps.

5. Add support to differentiate pins e.g. time passed since event

6. Build out interface that will allow user to vary hard limit and regenerate the map.

7. Add more cities?