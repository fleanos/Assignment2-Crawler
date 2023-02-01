from difflib import SequenceMatcher 
from urllib.parse import urlparse

def urlSimilarity(url1, url2):
  #threshold = 0.95 95% threshold
  similarity = SequenceMatcher(None, url1, url2)
  print(similarity.ratio()) #prints out the similarity ratio
  return similarity.ratio()

link1 = urlparse("http://archive.ics.uci.edu/ml/00315")
link2 = urlparse("http://archive.ics.uci.edu/ml/00615")
if link1.netloc == link2.netloc:
  if urlSimilarity(link1.path, link2.path) > 0.95:
    print("url1: ", link1.path, "url2: ", link2.path)



"""
2023-02-01 04:20:51,508 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/hill-valley, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:20:52,056 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00315, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:20:52,608 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00615, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:20:53,158 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00596, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:20:53,712 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00304, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:20:54,269 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00269, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:20:54,822 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00322, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:20:55,369 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00359, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:20:55,919 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00261, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:20:56,487 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00439, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:20:57,036 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00427, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:20:57,588 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00302, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:20:58,136 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00486, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:20:58,685 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00435, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:20:59,236 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/nursery, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:20:59,786 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00370, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:21:00,337 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00585, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:21:00,888 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/semeion, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:21:01,436 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00265, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:21:01,984 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/heart-disease, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:21:02,532 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/00376, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:21:03,082 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/spambase, status <404>, using cache ('styx.ics.uci.edu', 9005).
2023-02-01 04:21:03,634 - Worker-0 - INFO - Downloaded http://archive.ics.uci.edu/ml/led-display-creator, status <404>, using cache ('styx.ics.uci.edu', 9005).

"""