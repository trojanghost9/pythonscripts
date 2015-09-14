import re


def ip_grabbing():
    """
    Reads list.txt and returns any IP's in that list that exist 2 or more times.
    Will print out to the IP and the count for times occurred.
    :return: prints IP's with dupes and the counts
    """
    pattern = re.compile(r"((([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])[ (\[]?(\.|dot)[ )\]]?)"
                         r"{3}[0-9]{1,3})")

    with open('list.txt', 'r') as f:
        ip_dictionary = {}
        for l in f:
            ips = [match[0] for match in re.findall(pattern, l)]
            for ip in ips:
                if ip in ip_dictionary:
                    ip_dictionary[ip] += 1
                else:
                    ip_dictionary[ip] = 1

    # sorting IP results based on number of occurrence
    ips_sorted = sorted(ip_dictionary.items(), key=lambda item: item[1])

    with open('ips.txt', 'w+') as ips_file:
        for k, v in ips_sorted:
            if v > 1:
                print str(k) + " count: " + str(v)
                ips_file.write(str(k) + " count: " + str(v) + "\n")

    print "All done! please check ips.txt for your results :-)"

if __name__ == '__main__':
    ip_grabbing()
