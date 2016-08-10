import time
from urllib import FancyURLopener
import urllib2
import simplejson

# Define search term
searchTerm = "meme"

# Replace spaces ' ' in search term for '%20' in order to comply with request
searchTerm = searchTerm.replace(' ', '%20')


# Start FancyURLopener with defined version
class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11)' \
              ' Gecko/20071127 Firefox/2.0.0.11'

myopener = MyOpener()


def capture():
    """
    Uses defined search term to grab related image urls from google.
    """

    # Set count to 0, used for file names
    count = 0

    for start in range(0, 15):
        # the "start" variable will be used to iterate through 15 pages
        url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
               'v=1.0&q='+searchTerm+'&start='+str(start*4)+'&userip=MyIP')
        # printing out the url for testing
        # print url
        request = urllib2.Request(url, None, {'Referer': 'testing'})
        response = urllib2.urlopen(request)
        print response

        # Get results using JSON
        results = simplejson.load(response)
        print results
        data = results['responseData']
        datainfo = data['results']

        # Iterate for each result and get unescaped url
        for myUrl in datainfo:
            print myUrl['unescapedUrl']
            # count += 1
            # use if you want to save a copy of the image
            # myopener.retrieve(myUrl['unescapedUrl'],str(count)+'.jpg')

        # Sleep for one second to prevent IP blocking from Google
        time.sleep(1)

if __name__ == "__main__":
    capture()
