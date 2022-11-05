import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Generate random people heights
heights=np.random.normal(loc=160,scale=10,size=10000)

#find the mean
height_mean=np.mean(heights)

#plot the value
ax=sns.histplot(heights,bins=50,kde=True,color="green")
ax.axvline(height_mean, 0,0.95,color="red",linewidth=4)
ax.set(title='Mean')
ax.set_xlabel("Height of people (in cm)")
plt.show()