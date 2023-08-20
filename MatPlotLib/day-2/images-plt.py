import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open('.\Apple3.jpg'))
print(repr(img))

plt.imshow(img)
plt.title('APPLE COMPUTER 3')
plt.show()

img = Image.open('.\Apple3.jpg')
img.thumbnail((64, 64))  # resizes image in-place
imgplot = plt.imshow(img)
plt.show()


img = np.asarray(Image.open('.\Apple3.jpg'))
lum_img = img[:, :, 0]
plt.imshow(lum_img)
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')
plt.show()
