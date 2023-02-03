from urllib.parse import urlparse
from urllib.parse import urljoin

from collections import defaultdict
from os import path
import re
import pickle #for storing all info

#packages that needed to be installed
from bs4 import BeautifulSoup  #extracting links
import readability
from readability import Document #getting main body text and cleaning it
import nltk; nltk.download('punkt')
from nltk.tokenize import word_tokenize  #for word counter function
import lxml

def scraper(url, resp):
  links = extract_next_links(url, resp)
  return [link for link in links if is_valid(link)]

#returns set with all links found in page
def extractLinks(respContent: bytes) -> set:
  soup = BeautifulSoup(respContent, "html.parser")
  return set(link["href"] for link in soup.find_all("a", href = True))

#cleaning html content and tokenizing it, returning token frequencies
def tokenFreq(contentSummary) -> dict:
  cleanedContent = BeautifulSoup(contentSummary, "html.parser")

  tokens = word_tokenize((cleanedContent.get_text()).lower())

  freqDict = defaultdict(int)
  for token in tokens: 
      freqDict[token] += 1
  
  return dict(freqDict)

#determing if current page is unqiue enough compared to prev. pages
def contentSimilar(allPagesFreq: list, currentFreq: dict) -> float:
  #used slightly modded Jaccard Sim. from https://www.statology.org/jaccard-similarity-python/
  def jaccard(set1, set2):
    intersection = len(set(set1).intersection(set2))
    union = (len(set1) + len(set2)) - intersection
    return float(intersection) / union

  currentTokens = set(currentFreq.keys())
  for i in (allPagesFreq[0]).values():
    if jaccard(set(i[0].keys()), currentTokens) >= 0.9: return True
  return False

#handling of relative links - inputs all links set & page, returns list of links
def convertLinks(links: set, url) -> list:
  extractedLinks = []
  for link in links:
    parsedUrl = urlparse(link)
    if not parsedUrl.netloc:
      extractedLinks.append(urljoin(url, link))
    else:
      extractedLinks.append(link)
  return extractedLinks

def storeData(parsedUrls: list, url: str, freq: dict) -> None:
  pageLen = sum(freq.values())
  parsedUrls[0][url] = (freq, pageLen)
  pickle.dump(parsedUrls, open("parsedData.txt", "wb"))

def storeEncounteredUrl(parsedUrls: list, url: str):
  parsedUrls[1].add(url)
  pickle.dump(parsedUrls, open("parsedData.txt", "wb"))
  
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

  parsedUrl = urlparse(resp.url)
  url = parsedUrl.scheme + "://" + parsedUrl.netloc + parsedUrl.path
  
  if not path.exists("parsedData.txt"): parsedUrls = [dict(), set()]
  else: parsedUrls = pickle.load(open("parsedData.txt", "rb"))

  #already parsed url and page
  if url in parsedUrls[1]: return []
    
  storeEncounteredUrl(parsedUrls, url)
  
  #unsuccessful request
  if resp == None: return []
  if resp.status != 200: return []
  if resp.raw_response == None: return []
  if resp.raw_response.content == None: return []
  
  #extracting freq of tokens
  content = Document(resp.raw_response.content)
  
  try:
    contentSummary = content.summary()
  except readability.readability.Unparseable:
    return []

  frequencies = tokenFreq(contentSummary)

  #testing similarity of current page to pages found before
  if (len(frequencies) < 10) or contentSimilar(parsedUrls, frequencies):
    return []

  #save url & freq. dict
  storeData(parsedUrls, url, frequencies)
  
  #if page isn't too similar to previous pages extract links
  allLinks = extractLinks(resp.raw_response.content)

  #handle relative links
  links = convertLinks(allLinks, url)

  return links


"""
*.ics.uci.edu/*
*.cs.uci.edu/*
*.informatics.uci.edu/*
*.stat.uci.edu/
"""

def is_valid(url):
  # Decide whether to crawl this url or not.
  # If you decide to crawl it, return True; otherwise return False.
  # There are already some conditions that return False.
      
  try:
    parsed = urlparse(url)
    if parsed.scheme not in set(["http", "https"]):
      return False
      
    domains = [".ics.uci.edu",".cs.uci.edu",".informatics.uci.edu",".stat.uci.edu"]
    
    tot = 0
    for i in domains:
      tot += parsed.netloc.lower().find(i)
    
    if tot == -4: return False
    
    if url.find("/files/pdf") != -1 or url.find("/wp-content/uploads") != -1:
      return False
    
    if url.endswith(".DS_Store"):
      return False
      
    return not re.match(
      r".*\.(css|js|bmp|gif|jpe?g|ico" + r"|png|tiff?|mid|mp2|mp3|mp4" +
      r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf" +
      r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names" +
      r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso" +
      r"|epub|dll|cnf|tgz|sha1" + r"|thmx|mso|arff|rtf|jar|csv" +
      r"|rm|smil|wmv|swf|wma|zip|rar|gz|war|mpg)$", parsed.path.lower())

  except TypeError:
    print("TypeError for ", parsed)
    raise
