import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open("colors_rgb.png")
img_rgb = np.array(img)
l, c, p = img_rgb.shape

img_cmy = (255 - img_rgb) / 255

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.imshow(img_rgb)
plt.subplot(2, 1, 2)
plt.imshow(img_cmy)
plt.show()