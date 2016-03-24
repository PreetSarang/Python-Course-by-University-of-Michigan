import urllib
import xml.etree.ElementTree as ET

url = raw_input("Enter URL :")
if len(url) < 1:
    url = "http://python-data.dr-chuck.net/comments_42.xml"
uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
count = 0
totalcounts = 0
counts = tree.findall('comments/comment')
for item in counts:
	x = item.find('count').text
	totalcounts = totalcounts + int(x)
	count = count + 1
print count
print totalcounts
