import re
from urllib.parse import urlparse

from difflib import SequenceMatcher  #for similarity function
from bs4 import BeautifulSoup  #extractLinks
from readability import Document #getting main body text and cleaning it
from nltk.tokenize import word_tokenize  #for word counter function
import requests  #for testLinks
from collections import defaultdict


def scraper(url, resp):
  links = extract_next_links(url, resp)
  return [link for link in links if is_valid(link)]


def extractLinks(resp): #returns set with all links found in page
  soup = BeautifulSoup(resp.raw_response.content)
  return {i["href"] for i in soup.find_all("a", href = True)}

"""
import requests

#testing whether each link in the set is broken or not by requesting it
#returns a set of only valid links
#assuming that all links will be in string
def testLinks(setLinks):
  for link in setLinks:
    try:
      response = requests.get('link')
      if response != '200':
        print(link, "was invalid:", response)
    except:
      print(link, "was invalid")
  

#some links are not full links
def convertLinks(links):
  pass
  

2. fuc for determining similarity between two urls - prob. use sequence matcher - inputs - html content, percentage threshold

#check if the urls are gonna be in string(!)

def similarity(url1, url2):
  threshold = 0.95 #95% threshold
  similarity = SequenceMatcher(None, url1, url2)
  print(similarity.ratio()) #prints out the similarity ratio
  if similarity.ratio() >= threshold: #check if the ratio passes the threshold
    return similarity.ratio()
  
3.fuc to parse and count all words - inputs - html content, use ntlk for tokenizer

from nltk.tokenize import word_tokenize

def wordCounter (<html content1>, <html content2>): #reminder to actually input the parameters
  firstTokens = word_tokenize(<html content1>)
  secondTokens = word_tokenize(<html content2>)
  count = 0
  
  for t in firstTokens:
    if word in secondTokens:
      count += 1  
  return count 

      
def tokenFreq(resp):
  content = Document(resp.raw_response.content)
  cleanedContent = BeatifulSoup(content.summary(), "html.parser")

  tokens = word_tokenize(cleanedContent.get_text())

  freqDict = defaultdict(int)
  for token in tokens: 
      freqDict[token] += 1
  
  return dict(freqDict)
  
  
def extract_next_links(url, resp):
  links = {}
  parsedPages = load data file
  currentPage = urlparse(resp.url)

  if resp.status != 200: #unsuccessful request
    return []

  if currentPage in parsedPages["pages"]: #already parsed url and page
    return []

  #extracting freq of tokens
  frequency = tokenFreq(resp)

  
  
  #testing similarity of current page to pages found before
  




  #if page isn't too similar to previous pages extract and filter links
  
  allLinks = extractLinks(resp) #set with all links in html content
"""


def extract_next_links(url, resp):
  # Implementation required.
  # url: the URL that was used to get the page
  # resp.url: the actual url of the page
  # resp.status: the status code returned by the server. 200 is OK, you got the page. Other numbers mean that there was some kind of problem.
  # resp.error: when status is not 200, you can check the error here, if needed.
  # resp.raw_response: this is where the page actually is. More specifically, the raw_response has two parts:
  #         resp.raw_response.url: the url, again
  #         resp.raw_response.content: the content of the page!
  # Return a list with the hyperlinks (as strings) scrapped from resp.raw_response.content

  return list()


"""
initally filter out any links not containing: - can use regex or find()

*.ics.uci.edu/*
*.cs.uci.edu/*
*.informatics.uci.edu/*
*.stat.uci.edu/

prob - keep a set of all links previously visited
make sure current link hasnt been visited before

idk to check for similarities for all previous links here or not - would slow this fuc down a lot tho 
"""


def is_valid(url):
  # Decide whether to crawl this url or not.
  # If you decide to crawl it, return True; otherwise return False.
  # There are already some conditions that return False.
  try:
    parsed = urlparse(url)
    if parsed.scheme not in set(["http", "https"]):
      return False
    return not re.match(
      r".*\.(css|js|bmp|gif|jpe?g|ico" + r"|png|tiff?|mid|mp2|mp3|mp4" +
      r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf" +
      r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names" +
      r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso" +
      r"|epub|dll|cnf|tgz|sha1" + r"|thmx|mso|arff|rtf|jar|csv" +
      r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

  except TypeError:
    print("TypeError for ", parsed)
    raise
