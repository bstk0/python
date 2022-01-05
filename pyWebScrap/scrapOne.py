from bs4 import BeautifulSoup
#from urllib.request import urlopen
#from urllib2.request import urlopen
import urllib2

#html = urlopen("https://www.python.org/")
html = urllib2.Request("https://www.python.org/");
#res = BeautifulSoup(html.read(),"html5lib");
res = BeautifulSoup(html,"html5lib");
print(res.title);