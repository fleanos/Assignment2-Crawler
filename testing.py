from scraper import *
import readability
import requests  #for testing links
import lxml

"""
x = requests.get('http://www.ics.uci.edu')

if not path.exists("parsedData.txt"): parsedUrls = [dict(), set()]
else: parsedUrls = pickle.load(open("parsedData.txt", "rb"))

print(len(x.content))
frequencies = tokenFreq(x.content)
if contentSimilar(parsedUrls, frequencies):
    print("Content Sim.")

storeData(parsedUrls, 'http://www.ics.uci.edu', frequencies)

allLinks = extractLinks(x.content)
links = convertLinks(allLinks, 'http://www.ics.uci.edu')
print(links)

"""
print()

y = requests.get("http://flamingo.ics.uci.edu/.DS_Store")

if not path.exists("parsedData.txt"): parsedUrls = [dict(), set()]
else: parsedUrls = pickle.load(open("parsedData.txt", "rb"))

print(len(y.content))
content = Document(y.content)
try:
  contentSummary = content.summary()
except readability.readability.Unparseable:
  storeFileLink("http://flamingo.ics.uci.edu/.DS_Store")
  print("Doesn't error when not html")
frequencies = tokenFreq(contentSummary)
if contentSimilar(parsedUrls, frequencies):
    print("Content Sim.")

storeData(parsedUrls, "http://flamingo.ics.uci.edu/.DS_Store", frequencies)

allLinks = extractLinks(y.content)
links = convertLinks(allLinks, "http://flamingo.ics.uci.edu/.DS_Store")
print(links)

if not path.exists("parsedData.txt"): parsedUrls = [dict(), set()]
else: parsedUrls = pickle.load(open("parsedData.txt", "rb"))
print(parsedUrls)

print()

#false
print(is_valid("http://www.ics.uci.edu"))

#false
print(is_valid("https://www.ics.uci.edu/ugrad/sao/index"))

#false
print(is_valid("https://www.google.com/"))

#false
print(is_valid("https://communications.uci.edu/documents/pdf/UCI_14_map_campus.pdf"))

#true
print(is_valid("http://www.ics.uci.edu/ugrad/QA_Graduation"))

#handle_failures="discard"