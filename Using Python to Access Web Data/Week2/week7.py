import re
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
sum1=0
total =0
dignum = 0
for line in handle:
	line = line.rstrip()
	y = re.findall('([0-9]+)',line)
	if len(y)>0:
		dignum = dignum + len(y)
		linetotal = sum(map(int,y))
		total = total + linetotal
print total



