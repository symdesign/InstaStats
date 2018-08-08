# Displays a CSV file <accountname>.csv which contains the 
# current date, posts, followers, following.

# Usage: python <this-filename>.py <accountname>

import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import numpy as np

# Read Instagram account file
account = sys.argv[1]
dates, posts, followers, followings = np.loadtxt( account+'.csv', 
                                                delimiter=',', 
                                                unpack=True, 
                                                converters={ 0: mdates.strpdate2num('%Y-%m-%d')}
                                              ) 


ax = plt.axes()

# X axis
ax.xaxis.set_major_formatter( mdates.DateFormatter('%a %d.%m') )
ax.xaxis.set_major_locator( ticker.MultipleLocator(1) )
ax.tick_params(axis='x', colors='#333333')


# Y axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(100)) # steps
ax.axhline(100, color='#333333', alpha=0.2, linewidth=0.5)
ax.axhline(200, color='#333333', alpha=0.2, linewidth=0.5)
ax.tick_params(axis='y', colors='#e0e0e0')


# Styling
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(False)

ax.spines['bottom'].set_linewidth(0.5)
ax.spines['bottom'].set_color('#efefef')


# Plots
plt.bar(dates, followers, 0.1, color='blue', align='center')
plt.title("Instagram Growth")
# plt.ylabel("Amount")

# annotation with arrow
# ax.annotate('Test', (dates[2],followers[2]), xytext=(0,1), textcoords='axes fraction', arrowprops=dict( facecolor='grey', color='grey' ))

i = 0
while i < len(dates):
    ax.annotate( followers[i], (dates[i], followers[i]), xytext=(dates[i], followers[i]))
    i += 1

fig = plt.figure(1)
fig.autofmt_xdate()


# Render
plt.show()