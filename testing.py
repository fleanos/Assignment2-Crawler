from scraper import *


x = requests.get('http://www.ics.uci.edu')

currentPage = urlparse('http://www.ics.uci.edu')

allLinks = extractLinks(x.content)

links = convertLinks(allLinks, 'http://www.ics.uci.edu')
print(links)

#frequencies = tokenFreq(x.content)