import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def blend(img1, img2, c):
    blended_image = (c * img1) + ((1 - c) * img2)
    return blended_image.astype(np.uint8)

# Carregar as duas imagens
img1 = np.array(Image.open('1.jpg'))
img2 = np.array(Image.open('2.jpg'))

# Definir o coeficiente de blending
coeficiente = 0.5

# Realizar o blending
imagem_blending = blend(img1, img2, coeficiente)

# Salvar e exibir a imagem resultante
plt.imshow(imagem_blending)
plt.show()

#Aumente (ou diminua, caso prefira) a iluminação da imagem gerada acima. Salve o resultado no disco.

# Ajustar a iluminação (aumentar neste caso)
imagem_ajustada = np.clip(imagem_blending * 1.5, 0, 255).astype(np.uint8)

# Salvar a imagem ajustada no disco
Image.fromarray(imagem_ajustada).save('imagem_blending_ajustada.png')

# Exibir as imagens
plt.figure(figsize=(16, 16))

plt.subplot(2, 2, 1)
plt.imshow(imagem_ajustada)
plt.title("Imagem com iluminação aumentada")

plt.subplot(2, 2, 2)
plt.imshow(imagem_blending)
plt.title("Imagem original do blending")

plt.show()