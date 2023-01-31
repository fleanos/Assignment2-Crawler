from scraper import *


x = requests.get('http://www.ics.uci.edu')

if not path.exists("parsedData.txt"): parsedUrls = dict()
else: parsedUrls = pickle.load(open("parsedData.txt", "rb"))

frequencies = tokenFreq(x.content)
if contentSimilar(parsedUrls, frequencies):
    print("Content Sim.")

storeData(parsedUrls, 'http://www.ics.uci.edu', frequencies)

allLinks = extractLinks(x.content)
links = convertLinks(allLinks, 'http://www.ics.uci.edu')
print(links)


print()

y = requests.get("https://www.ics.uci.edu/ugrad/sao/index")

if not path.exists("parsedData.txt"): parsedUrls = dict()
else: parsedUrls = pickle.load(open("parsedData.txt", "rb"))

frequencies = tokenFreq(y.content)
if contentSimilar(parsedUrls, frequencies):
    print("Content Sim.")

storeData(parsedUrls, "https://www.ics.uci.edu/ugrad/sao/index", frequencies)

allLinks = extractLinks(y.content)
links = convertLinks(allLinks, "https://www.ics.uci.edu/ugrad/sao/index")
print(links)

if not path.exists("parsedData.txt"): parsedUrls = dict()
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
