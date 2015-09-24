from spam.spamhaus import SpamHausChecker  # pip install spam-blocklists


def check():
    """
    checks a list of url's against Spamhaus's SBL - urllist.txt
    the list must be full path and include http://
    GoDaddy SBL http://www.spamhaus.org/sbl/listings/godaddy.com
    :return: url's that are listed
    """
    checker = SpamHausChecker()
    with open('urllist.txt', 'r') as urllist:
        for url in urllist:
            url = url.strip()
            if checker.is_spam(url) is True:
                print url, 'is in the SBL'
            else:
                continue

if __name__ == '__main__':
    check()
