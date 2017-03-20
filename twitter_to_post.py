##########################################################################################
#
# File: twitter_to_post.py
# Author: Cristobal Espinosa
# Site: http://www.securityinside.info
# Source: https://github.com/security-inside
# 
##########################################################################################

# Imports ################################################################################
from bs4 import BeautifulSoup
import requests
import time
import sys
import logging
##########################################################################################

# Initial values #########################################################################
url = "https://twitter.com/security_inside"
##########################################################################################

# Header #################################################################################
print 
print '-- Twitter to post automation (' + time.strftime("%c") + ')' 
print '----------------------------------------------------------------------------------'
##########################################################################################

# Get retweet info
# ---------------------------------------------------------------------------------------
req = requests.get(url)
statusCode = req.status_code

if statusCode == 200:

    html = BeautifulSoup(req.text, "html.parser")

    for timeline in html.find_all('div', {'data-test-selector':'ProfileTimeline'}):
        for oltag in timeline.find_all('ol', {'id':'stream-items-id'}):
            for litag in oltag.find_all('li'):
                for div in litag.find_all('div', {"class" : "tweet"}):
                    try:
                        if div['data-retweet-id']:

                            for small in litag.find_all('small', {"class" : "time"}):
                                for a in small.find_all('a', {"class" : "tweet-timestamp"}):
                                    try:
                                        date = a['title'].encode("ascii", "ignore")

                                    except Exception as e:
                                        None

                            title = div.find('p', {'class':'TweetTextSize'}).getText().split('http')[0].encode("ascii", "ignore")

                            link = div.find('a', {'class':'twitter-timeline-link'}).getText().encode("ascii", "ignore")

                            name = div.find('span', {'class':'username'}).getText().split('@')[1].encode("ascii", "ignore")
							
                            for img in div.find_all('img'):
                                if 'avatar' in img:
                                    image = 'http://securityinside.info/wp-content/uploads/logo.png'
                                else:
                                    image = img['src'].encode("ascii", "ignore")

                            print '<tr><td style="vertical-align:middle;border:0px;margin: 0px 0px"><img class="aligncenter" src="' + image + '" alt="' + name + '" width="150"/></td>\n<td style="vertical-align:middle;border:0px;margin: 0px 0px"><strong><a href="https://twitter.com/' + name + '" target="_blank">' + date + ' @' + name + ':<br></a></strong> <a href="' + link + '" target="_blank">' + title + '</a></td></tr>'

                    except Exception as e:
                        None

else:
    print "Status Code %d" %statusCode
# ---------------------------------------------------------------------------------------

# Footer #################################################################################
print '----------------------------------------------------------------------------------'
##########################################################################################

