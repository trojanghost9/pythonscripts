# this script can be used to grab the url's for some google search result

import sys # Used to add the BeautifulSoup folder the import path
import urllib2 # Used to read the html document
import re

if __name__ == "__main__":
    ### Import Beautiful Soup
    ### Here, I have the BeautifulSoup folder in the level of this Python script
    ### So I need to tell Python where to look.
    sys.path.append("./BeautifulSoup")
    from BeautifulSoup import BeautifulSoup

    ### Create opener with Google-friendly user agent
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    ### Open page & generate soup
    ### the "start" variable will be used to iterate through 10 pages.
    for start in range(0,10):
        # url = "http://www.google.com/search?q=site:stackoverflow.com&start=" + str(start*10)
        # url must be set to the search
        url = "https://www.google.com/search?q=pun+memes&tbm=isch&start=" + str(start*10)
	page = opener.open(url)
        # print page
        soup = BeautifulSoup(page)
        # print soup

        ### Parse and find
        ### Looks like google contains URLs in <cite> tags.
        ### So for each cite tag on each page (10), print its contents (url)
        list = []
        for text in soup.findAll('img'):
            pattern = r'src="(http\S{1,})"'
	    link = re.findall(pattern, str(text))
	    # this needs work, prints out in ugly format and leaves brackets
            # may also wanna look at using this https://developers.google.com/custom-search/json-api/v1/overview?csw=1
            print link
	    list += link

    # print list
