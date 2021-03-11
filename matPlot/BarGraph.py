import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
temp_max = [20, 34, 30, 35, 27]
temp_mins = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars


#the legened box
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, temp_max, width, label='Max temp')
rects2 = ax.bar(x + width/2, temp_mins, width, label='Min temp')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Temperaturee in F')
ax.set_title('Average annual max and min temperatures')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

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


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()