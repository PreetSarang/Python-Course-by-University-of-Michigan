import json
import urllib
url = raw_input("Enter URL :")
if len(url) < 1:
    url = "http://python-data.dr-chuck.net/comments_42.json"
uh = urllib.urlopen(url)
data = uh.read()
#print data
info = json.loads(data)
count = []

comments = info["comments"]
for comment in comments:
	count.append(comment['count'])
#counts = info.findall('comments/comment')

	
print sum(count)