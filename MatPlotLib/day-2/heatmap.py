import numpy as np
import matplotlib.pyplot as plt
import numpy.random


temp = np.random.randn(4096)
anger = np.random.randn(4096)

heatmap, xedges, yedges = np.histogram2d(temp, anger, bins=(64, 64))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plt.clf()
plt.ylabel('Anger')
plt.xlabel('Temp')
plt.imshow(heatmap, extent=extent)
plt.show()
