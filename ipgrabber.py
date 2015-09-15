import re
import os
import webbrowser


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

    with open('ips.html', 'w+') as ips_file:
        html_start_message = '''<!doctype html><head><script language="JavaScript">''' + \
                       '''function myFunction() { window.open("http://replygif.net/i/202.gif");}''' + \
                       '''</script></head><body><button onclick="myFunction()">HOORAY!''' + \
                       '''</button><br/><table border="1"><tr><th>IP</th><th>Count</th></tr>'''
        html_end_message = '''</table></body></html>'''
        ips_file.write(html_start_message)

        for k, v in ips_sorted:
            if v > 1:
                print str(k) + " count: " + str(v)
                ips_file.write("<tr><td>" + str(k) + "</td><td>" + str(v) + "</td></tr>")

        ips_file.write(html_end_message)

    print "All done! :-)"
    filename = os.getcwd() + '/ips.html'
    webbrowser.open_new_tab(filename)

if __name__ == '__main__':
    ip_grabbing()
