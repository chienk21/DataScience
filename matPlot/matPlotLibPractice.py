#Matplotlib

import matplotlib.pyplot as plt

# k = [1.1, 2.3,4.5,10,11]
# plt.plot(k)
# plt.ylabel("Y axis")
# plt.xlabel("X axis")
# plt.show()

#triangle dots "^"
#dots "o"
#line "-"
#this gets you the points and the color of the data points
plt.plot([1,2,3,4], [1,4,9,16], "k+")

# format for axis min and max is [xmin, xmax, ymin, ymax]
plt.axis([0,10,0,30])
plt.ylabel("high (inches)")
plt.xlabel("time (seconds)")
plt.title("bhaddie")
plt.show()




