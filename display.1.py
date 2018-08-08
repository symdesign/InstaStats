# Displays a CSV file <accountname>.csv which contains the 
# current date, posts, followers, following.

# Usage: python <this-filename>.py <accountname>

import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


account = sys.argv[1]

source_csv = open(account+'.csv', 'r').read().decode()
numbers_data = []

split_source = source_csv.split('\n')

for line in split_source:
    numbers_data.append(line)

date, posts, followers, following = np.loadtxt( numbers_data, delimiter=',', unpack=True, converters={0: bytespdate2num('%Y-%m-%d')} )



# Create a new figure of size 8x6 points, using 100 dots per inch
plt.figure(figsize=(8,6), dpi=80)

# Create a new subplot from a grid of 1x1
axes = gca()
axes.set_xlim(0,4)
axes.set_ylim(0,3)
axes.set_xticklabels([])
axes.set_yticklabels([])


plt.plot(date, posts, color='orange', linewidth=1.0, linestyle='--')
plt.plot(date, followers, color='blue', linewidth=2.0, linestyle='-')
plt.plot(date, following, color='green', linewidth=1.0, linestyle='--')


plt.xticks()

plt.show()