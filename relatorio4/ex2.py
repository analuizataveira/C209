from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Converta uma imagem para binária, utilizando um método de grayscale diferente do anterior. Salve-a no disco.

img = Image.open('valac.png')
img_np = np.array(img)

img_np_float64 = img_np[:, :, :3].astype(np.float64)
# Soma cada pixel das páginas 0, 1 e 2 e divide por 3.
# Obs.: Lembrar de converter para np.uint8!
img_avg3 = ((img_np_float64[:, :, 0] + img_np_float64[:, :, 1] + img_np_float64[:, :, 2]) / 3).astype(np.uint8)
plt.imshow(img_avg3, cmap='gray')
plt.show()