from scraper import *


x = requests.get('http://www.ics.uci.edu')

allLinks = extractLinks(x.content)
print(allLinks)

frequencies = tokenFreq(x.content)
print(frequencies)