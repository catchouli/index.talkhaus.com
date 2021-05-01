# index.talkhaus.com
the index page for talkhaus sites

## data-gatherer

Requirements:
* Grab a binary for geckodriver from <a href="https://github.com/mozilla/geckodriver/releases">here</a> and put it in /usr/local/bin (check it's runnable)
* Install firefox (e.g. ```sudo apt install firefox```)
* Install selenium (```pip3 install selenium```) 
* Run ```python3 data-gatherer.py``` to fill in the screenshots and _sites directory

## site

It's just a standard jekyll site, so after running the data gatherer just use ```jekyll build``` or ```jekyll serve```
