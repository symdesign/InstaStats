# Saves a CSV file <accountname>.csv which contains the 
# current date, posts, followers, following.

# Usage: python <this-filename>.py <accountname>

import sys
import requests
import csv
import time

from bs4 import BeautifulSoup
from pyvirtualdisplay import Display 
from selenium import webdriver

account = sys.argv[1]
url = 'https://www.instagram.com/' + account

# set up chrome driver to read react-generated page

# display = Display(visible=0, size=(1024, 768))
# display.start()

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--dns-prefetch-disable')
options.add_argument('--no-sandbox')
options.add_argument('--lang=en-US')

service_log_path = "./chromedriver.log"
service_args = ['--verbose']

browser = webdriver.Chrome("./chromedriver",chrome_options=options, service_args=service_args, service_log_path=service_log_path)
browser.implicitly_wait(25)
browser.get(url)

# get the data
soup = BeautifulSoup(browser.page_source,"html.parser")

numbers = soup.find('header').find('section').find('ul').find_all('li')

posts = numbers[0].find('span').find('span').contents[0]
followers = numbers[1].find('span').contents[0]
following = numbers[2].find('span').contents[0]

date = time.strftime("%Y-%m-%d")

# write the data
f = csv.writer(open(account+'.csv', 'a')) # open file in append mode
f.writerow([date,posts,followers,following]) # write to the file
