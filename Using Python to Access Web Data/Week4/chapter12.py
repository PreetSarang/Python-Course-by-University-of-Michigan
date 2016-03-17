import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
sum1 =0
# Retrieve all of the anchor tags
data = soup.findAll("span", {"class":"comments"})
numbers = [d.text.encode('utf-8') for d in data]
for x in numbers:
    sum1 = sum1 + int(x)
print sum1