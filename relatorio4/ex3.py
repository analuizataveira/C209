from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


#3. Converta uma imagem para algum espectro monocromático utilizando um método de grayscale diferente dos anteriores. Exiba-a com o matplotlib.
img = Image.open('valac.png')
img_np = np.array(img)

img_avg2 = np.average(img_np[:, :, :3], axis=2).astype(np.uint8)
plt.imshow(img_avg2, cmap='gray')
plt.show() 