from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#EXERCICIO1
#Utilize um método grayscale e salve a imagem resultante no disco.

img = Image.open('valac.png')
img_np = np.array(img)

(l, c, p) = img_np.shape

img_avg = np.zeros(shape=(l, c), dtype=np.uint8)
for i in range(l):
    for j in range(c):
        r = float(img_np[i, j, 0])
        g = float(img_np[i, j, 1])
        b = float(img_np[i, j, 2])
        
        img_avg[i, j] = (r + g + b) / 3

plt.imshow(img_avg, cmap='gray')
plt.show()