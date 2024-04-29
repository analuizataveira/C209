import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Mais uma forma de aplicar threshold:
def threshold(img, thresh):
    out = img.copy()
    out[img >  thresh] = 255
    out[img <= thresh] = 0
    return out

img1 = np.array(Image.open("img1.jpg"))[:, :, :3]
img2 = np.array(Image.open("img2.jpg"))[:, :, :3]

bin1 = threshold(img1, 63)
bin2 = threshold(img2, 63)

bin1_not = np.bitwise_not(bin1)
bin2_not = np.invert(bin2)

#------------------XOR-------------------------
bin_xor = np.bitwise_xor(bin1, bin2)
# Ou:
#bin_or = bin1 ^ bin2

bin_xor_2 = bin1_not ^ bin2_not
# Ou:
#bin_or_2 = np.bitwise_xor(bin1_not, bin2_not)

plt.figure(figsize=(16, 16))
plt.subplot(3, 2, 1)
plt.imshow(bin1, cmap='gray')
plt.subplot(3, 2, 2)
plt.imshow(bin1_not, cmap='gray')

plt.subplot(3, 2, 3)
plt.imshow(bin2, cmap='gray')
plt.subplot(3, 2, 4)
plt.imshow(bin2_not, cmap='gray')

plt.subplot(3, 2, 5)
plt.imshow(bin_xor, cmap='gray')
plt.subplot(3, 2, 6)
plt.imshow(bin_xor_2, cmap='gray')
plt.show()

#--------------------OR----------------------------------------------------
bin_or = np.bitwise_or(bin1, bin2)
# Ou:
#bin_or = bin1 | bin2

bin_or_2 = bin1_not | bin2_not
# Ou:
#bin_or_2 = np.bitwise_or(bin1_not, bin2_not)

plt.figure(figsize=(16, 16))
plt.subplot(3, 2, 1)
plt.imshow(bin1, cmap='gray')
plt.subplot(3, 2, 2)
plt.imshow(bin1_not, cmap='gray')

plt.subplot(3, 2, 3)
plt.imshow(bin2, cmap='gray')
plt.subplot(3, 2, 4)
plt.imshow(bin2_not, cmap='gray')

plt.subplot(3, 2, 5)
plt.imshow(bin_or, cmap='gray')
plt.subplot(3, 2, 6)
plt.imshow(bin_or_2, cmap='gray')
plt.show()

#----------------------AND----------------------
bin_and = np.bitwise_and(bin1, bin2)
# Ou:
#bin_and = bin1 & bin2

bin_and_2 = bin1_not & bin2_not
# Ou:
#bin_and_2 = np.bitwise_and(bin1_not, bin2_not)

plt.figure(figsize=(16, 16))
plt.subplot(3, 2, 1)
plt.imshow(bin1, cmap='gray')
plt.subplot(3, 2, 2)
plt.imshow(bin1_not, cmap='gray')

plt.subplot(3, 2, 3)
plt.imshow(bin2, cmap='gray')
plt.subplot(3, 2, 4)
plt.imshow(bin2_not, cmap='gray')

plt.subplot(3, 2, 5)
plt.imshow(bin_and, cmap='gray')
plt.subplot(3, 2, 6)
plt.imshow(bin_and_2, cmap='gray')
plt.show()