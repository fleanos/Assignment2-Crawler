import re
from urllib.parse import urlparse

from difflib import SequenceMatcher  #for url similarity function
from bs4 import BeautifulSoup  #extracting links
from readability import Document #getting main body text and cleaning it
from nltk.tokenize import word_tokenize  #for word counter function
from collections import defaultdict
import requests  #for testing links
import pickle #for storing all info


def scraper(url, resp):
  links = extract_next_links(url, resp)
  return [link for link in links if is_valid(link)]

#returns set with all links found in page
def extractLinks(respContent: bytes) -> set:
  soup = BeautifulSoup(respContent)
  return set(link["href"] for link in soup.find_all("a", href = True))

#cleaning html content and tokenizing it, returning token frequencies
def tokenFreq(htmlContent: bytes) -> dict:
  content = Document(htmlContent)
  cleanedContent = BeautifulSoup(content.summary(), "html.parser")

  tokens = word_tokenize(cleanedContent.get_text())

  freqDict = defaultdict(int)
  for token in tokens: 
      freqDict[token] += 1
  
  return dict(freqDict)

#determing if current page is unqiue enough compared to prev. pages
def contentSimilarity(allPagesFreq: dict, currentPageFreq: dict) -> float:
  pass

#handling of relative links - inputs all links set & page, returns list of links
def convertLinks(links: set, page) -> list:
  extractedLinks = []
  for link in links:
    parsedUrl = urlparse(link)
    if not parsedLink.netloc:
      pass
    extractedLinks.append(parsedUrl)
  return extractedLinks

def storeData(parsedPages: dict, url: str, freq: dict) -> None:
  pass #thinking of storing as {"url" : (freq dict, page length)}


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

  if not path.exists("parsedPagesData.txt"): parsedPages = dict()
  else: parsedPages = pickle.load(open("parsedPagesData.txt", "rb"))
  
  currentPage = urlparse(resp.url)

  if resp.status != 200: #unsuccessful request
    return []

  if url in parsedPages: #already parsed url and page
    return []

  #extracting freq of tokens
  frequencies = tokenFreq(resp.raw_response.content)

  #testing similarity of current page to pages found before
  




  #if page isn't too similar to previous pages extract links
  allLinks = extractLinks(resp.raw_response.content)

  #handle relative links
  links = convertLinks(allLinks, currentPage)

  #save url & freq. dict
  storeData(parsedPages, url, frequencies)

  return links


"""
initally filter out any links not containing: - can use regex or find()

*.ics.uci.edu/*
*.cs.uci.edu/*
*.informatics.uci.edu/*
*.stat.uci.edu/

check for similarities for all previous links

def urlSimilarity(url1, url2):
  threshold = 0.95 #95% threshold
  similarity = SequenceMatcher(None, url1, url2)
  print(similarity.ratio()) #prints out the similarity ratio
  if similarity.ratio() >= threshold: #check if the ratio passes the threshold
    return similarity.ratio()
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
