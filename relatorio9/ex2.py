import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Carregar a imagem em escala de cinza
imagem_gray = np.array(Image.open('hill.jpg'))

# Calcular o histograma da imagem
hist_gray, bins_gray = np.histogram(imagem_gray.ravel(), bins=256, range=(0, 255))

# Calcular a função de densidade cumulativa (histograma cumulativo)
fdc = np.cumsum(hist_gray)

# Aplicar a técnica de equalização de histograma
l, c = imagem_gray.shape
imagem_equalizada = np.zeros_like(imagem_gray)
for intensidade in range(256):
    novo_valor = np.round((fdc[intensidade] - np.min(fdc)) / ((l * c) - np.min(fdc)) * 255)
    imagem_equalizada[imagem_gray == intensidade] = novo_valor

# Exibir a imagem original e a imagem equalizada
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagem_gray, cmap='gray')
plt.title('Imagem original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(imagem_equalizada, cmap='gray')
plt.title('Imagem equalizada')
plt.axis('off')

plt.show()