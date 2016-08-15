import socket
import datetime

"""
checks @ record for domain
make sure to incluse subdomain if required
"""

# domain to search
domain = "paypal.com"

# sets file name to the date it was checked
filename = str(datetime.datetime.now()).replace(" ",".") + ".txt"

# checks for host ip based on domain
results = socket.getaddrinfo(domain, 80, 0, 0, socket.IPPROTO_TCP)
splitstuff = str(results).split("'")
ip = splitstuff[3]

print ip

# write results to filename based on time
with open(filename, 'w+') as f:
    f.write(ip)
