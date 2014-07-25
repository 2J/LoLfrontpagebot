LoLfrontpagebot
===============

Twitter bot for [@LoLfrontpage](http://twitter.com/lolfrontpage)

Gets the front page of reddit.com/r/leagueoflegends and puts it on Twitter

###Requirements

1. python + pip

2. twitter account (Need to have mobile authentication to change app permissions - workaround [here](http://blog.j2.io/changing-twitter-app-permissions-without-keeping-mobile-connected/))

3. Hosting where you can save files

###SETUP

1. install tweeper and requests using pip

2. Make a Twitter app [here](https://apps.twitter.com/) and change permission from read to r/w

3. Fill in the access token / consumer key(a.k.a. API key) in the script

4. Set up a cron job to run the script every few minutes

5. Set up a cron job to delte any files older than 3 days in the index folder. This will keep the folder from accumulating too much space
