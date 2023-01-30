from bs4 import BeautifulSoup
import re

import testHtml.html

def extractLinks(resp):
  soup = BeautifulSoup(resp)
  
  #links starting with https://
  httpsLinks = {link for link in soup.find_all('a', attrs={'href': re.compile("^https://")})}

  #links starting with www.
  wwwLinks = {link for link in soup.find_all('a', attrs={'href': re.compile("^//www.")})}

  return httpsLinks + wwwLinks

for i in extractLinks(testHtml.html):
  print(i, type(i))