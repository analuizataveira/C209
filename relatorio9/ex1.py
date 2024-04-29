import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Carregar a imagem
imagem = np.array(Image.open('girl.jpg'))

# Extrair os canais de cor
canal_r = imagem[:,:,0]
canal_g = imagem[:,:,1]
canal_b = imagem[:,:,2]

# Calcular os histogramas dos canais de cor
hist_r, bins_r = np.histogram(canal_r.ravel(), bins=256, range=(0, 255))
hist_g, bins_g = np.histogram(canal_g.ravel(), bins=256, range=(0, 255))
hist_b, bins_b = np.histogram(canal_b.ravel(), bins=256, range=(0, 255))

# Calcular o histograma em escala de cinza usando o método de luminosidade
imagem_gray_luminosity = 0.2126 * canal_r + 0.7152 * canal_g + 0.0722 * canal_b
hist_gray_luminosity, bins_gray_luminosity = np.histogram(imagem_gray_luminosity.ravel(), bins=256, range=(0, 255))

# Plotar os histogramas
plt.figure(figsize=(10, 10))

# Histogramas dos canais de cor
plt.subplot(2, 1, 1)
plt.plot(hist_r, color='red', label='R')
plt.plot(hist_g, color='green', label='G')
plt.plot(hist_b, color='blue', label='B')
plt.xlabel('Valor do pixel')
plt.ylabel('Frequência')
plt.title('Histograma dos canais de cor')
plt.legend()

# Histograma em escala de cinza usando o método de luminosidade
plt.subplot(2, 1, 2)
plt.plot(hist_gray_luminosity, color='black')
plt.xlabel('Valor do pixel')
plt.ylabel('Frequência')
plt.title('Histograma em escala de cinza (Luminosidade)')

plt.tight_layout()
plt.show()