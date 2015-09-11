import re

pattern = re.compile(r"((([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])[ (\[]?(\.|dot)[ )\]]?)"
                      r"{3}[0-9]{1,3})")

"""
you can write these results out to a file (ips.txt)
for now i can then use the following command to sort the results by the biggest talkers: 
sort -t " " -k 3 -n ips.txt > orderedfile.txt
"""


with open('list.txt', 'r') as f:
    ipdic = {}
    for l in f:
        ips = [match[0] for match in re.findall(pattern, l)]
        # [match[0] for match in pattern.findall(l.split('\t')[6])]
        for ip in ips:
            if ip in ipdic:
                ipdic[ip] += 1
            else:
                ipdic[ip] = 1
            #print ip

for k,v in ipdic.iteritems():
    if v > 1:
        print str(k) + " count: " + str(v)
