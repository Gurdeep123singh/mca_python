from matplotlib import pyplot as plt
from matplotlib import patches        # this works without patches also
import numpy as np


xpoints=[1,2,3,4]
ypoints=[1,4,15,6]
s=['p1','p2','p3','p4']
plt.plot(xpoints,ypoints,'o')
for i in range(len(xpoints)):
    plt.text(xpoints[i]+0.1,ypoints[i]+0.1,s[i])
plt.show()    