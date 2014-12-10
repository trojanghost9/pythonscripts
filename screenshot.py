from pyvirtualdisplay import Display
from selenium import webdriver
import urllib2

url = raw_input('please enter a website: ')

display = Display(visible=0, size=(800, 600))
display.start()

browser = webdriver.Firefox()
browser.get(url)
browser.save_screenshot('test.png')

browser.quit()

display.stop()

usock = urllib2.urlopen(url)
data = usock.read()
usock.close()

with open('test.txt', "wb") as file:
    file.write(data)



