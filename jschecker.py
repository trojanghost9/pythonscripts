import requests
from bs4 import BeautifulSoup

def demscripts():
    """
    alows user to paste a url and will print out any js if the site resolves
    :return:
    """
    url = raw_input('Please enter the reported url: ')
    print url
    r = requests.get(url)
    status = list(str(r.status_code))

    if status[0] not in ['4', '5']:
        # souce code for site
        source = r.text

        # soup it up!
        soup = BeautifulSoup(source)

        # use for if statment to look for js
        if soup.script is None:
            print 'No javascript here brah'
        else:
            # print out any js on the site
            for script in soup.script:
                print script
                print '' 
    else:
        print 'doesnt resolve brah'

if __name__ == "__main__":
    demscripts()
