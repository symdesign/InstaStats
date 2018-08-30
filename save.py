#!/bin/python

# Saves a CSV file <accountname>.csv which contains the 
# current date, posts, followers, following.

# Usage: python <this-filename>.py <accountname>

import os
import sys
import requests
import csv
import time

from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from selenium import webdriver

account = sys.argv[1]
url = 'https://www.instagram.com/' + account
path = os.path.realpath(__file__)
path = os.path.dirname(path)

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

print('Starting Chrome ...')
browser = webdriver.Chrome(chrome_options=options, service_args=service_args, service_log_path=service_log_path)
browser.set_page_load_timeout(60) 
browser.implicitly_wait(25) 
browser.get(url)

print('')
print('------')
print('>>',url)
print('------')
print('')


# get the data
print('Starting to scrape the data from',account)
soup = BeautifulSoup(browser.page_source,"html.parser")

numbers = soup.select('header.vtbgv ul li')

posts = numbers[0].find('span').find('span').contents[0]
followers = numbers[1].find('span').contents[0]
following = numbers[2].find('span').contents[0]


# format numbers
posts = posts.replace(',','')
followers = followers.replace(',','')
following = following.replace(',','')

date = time.strftime("%Y-%m-%d")


# write the data

print('')
print('Writing', date, posts, followers, following, 'to', path+'/'+account+'.csv',)

f = csv.writer(open(path+'/'+account+'.csv', 'a')) # open file in append mode
f.writerow([date,posts,followers,following]) # write to the file

# sleep a while for crontab & screen debugging
# time.sleep(60)