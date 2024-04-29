import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def conv(image, kernel):
    m, n = kernel.shape
    assert m == n, "Kernel deve ser uma matriz quadrada."
    l, c = image.shape
    new_l = l - m + 1
    new_c = c - n + 1
    new_image = np.zeros(shape=(new_l, new_c))
    for i in range(new_l):
        for j in range(new_c):
            new_image[i, j] = np.sum(image[i:i + m, j:j + n] * kernel)
    
    return new_image

museum_rgb = np.array(Image.open("museum.jpg"))[:, :, :3]
l, c, p = museum_rgb.shape

# Converter para escala de cinza:
museum_gray = np.zeros(shape=(l, c), dtype=np.uint8)
for i in range(l):
    for j in range(c):
        r = float(museum_rgb[i, j, 0])
        g = float(museum_rgb[i, j, 1])
        b = float(museum_rgb[i, j, 2])
        
        museum_gray[i, j] = (r + g + b) / 3

# Filtro de média:
kernel = np.ones((3, 3)) / 9

# Aplicar a convolução:
museum_conv = conv(museum_gray / 255, kernel)

# Exibir a imagem resultante:
plt.figure(figsize=(16, 16))
plt.imshow(museum_conv, cmap='gray')
plt.show()
