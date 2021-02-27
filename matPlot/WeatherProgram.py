import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['1973', '1975', '1977', '1979', '1981', '1983', '1985', '1987', '1989', '1991', '1993', '1995', '1997', '1999', '2001', '2003', '2007', '2009', '2011', '2013', '2015', '2017', '2019']
temp_max = [24.7, 25.9, 26.4, 24.9, 25.8, 24.2, 25.4, 25.9, 25.4, 25.8, 25.3, 26, 23.8, 26.9, 25.1, 26.1, 25.9, 26.2, 27.4, 26, 26.1, 28.1, 25.9]
temp_mins = [12.8, 12, 12, 10.9, 11.7, 11.1, 12.1, 11.8, 11.8, 12.3, 12.2, 12.2, 13.3, 14.7, 12.8, 12.7, 14.1, 12.9, 13.7, 12.5, 13.4, 14.7, 13]


# function np.arange() returns an array with the number of elements as the length of the parameter
# ie. np.arnage(3) -> [0, 1, 2]
x = np.arange(len(labels))  # the label locations
# print(x)
width = 0.35  # the width of the bars


#using variable ax for single a Axes
#x - width/2 is the x coordinates of the bar
# ax.bar(x, height, width)
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, temp_max, width, label='Max temp')
rects2 = ax.bar(x + width/2, temp_mins, width, label='Min temp')

#legned box uses automatic detection of elements in legend from labels
ax.legend()

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Temperaturee in F')
ax.set_title('Average annual max and min temperatures')
# sets x axis tick locations
ax.set_xticks(x)
#labels x tick marks labels
ax.set_xticklabels(labels)
ax.set_xlabel('Years')



#the bar number label, displays the exact number 
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def autolabel_two(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(5, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel_two(rects2)

# automatically adjusts subplot params so that the subplot(s) fits in to the figure area
fig.tight_layout()

plt.show()