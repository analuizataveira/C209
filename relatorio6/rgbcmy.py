import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open("colors_rgb.png")
img_rgb = np.array(img)
l, c, p = img_rgb.shape

img_cmy = np.zeros(shape=img_rgb.shape, dtype=np.float64)
for i in range(l):
    for j in range(c):
        r = img_rgb[i, j, 0]
        g = img_rgb[i, j, 1]
        b = img_rgb[i, j, 2]
        
        img_cmy[i, j, 0] = (255 - r) / 255 # C
        img_cmy[i, j, 1] = (255 - g) / 255 # M
        img_cmy[i, j, 2] = (255 - b) / 255 # Y

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.imshow(img_rgb)
plt.subplot(2, 1, 2)
plt.imshow(img_cmy)
plt.show()


# Verificação:
img_cmy_verify = np.array(img.convert('CMYK'))[:, :, :3]

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.imshow(img_cmy)
plt.subplot(2, 1, 2)
plt.imshow(img_cmy_verify)
plt.show()