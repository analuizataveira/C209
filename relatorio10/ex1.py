import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def converter_para_escala_de_cinza(imagem_rgb):
    l, c, _ = imagem_rgb.shape
    imagem_gray = np.zeros(shape=(l, c), dtype=np.uint8)
    for i in range(l):
        for j in range(c):
            r = float(imagem_rgb[i, j, 0])
            g = float(imagem_rgb[i, j, 1])
            b = float(imagem_rgb[i, j, 2])
            imagem_gray[i, j] = (r + g + b) / 3
    return imagem_gray

def detect_normals(image):
    # Calcular as derivadas parciais
    dx = np.diff(image.astype(np.float64), axis=1, append=255)
    dy = np.diff(image.astype(np.float64), axis=0, append=255)
    
    # Calcular o gradiente
    gradient = np.sqrt(dx**2 + dy**2)
    
    # Calcular os componentes r, g e b das normais
    r = (-dx + 255) / 2
    g = (dy + 255) / 2
    b = 255 - gradient
    
    # Juntar os componentes em uma imagem RGB
    normals = np.stack([r, g, b], axis=-1).astype(np.uint8)
    
    return normals

# Carregar a imagem de entrada
imagem_rgb = np.array(Image.open('museum.jpg'))

# Converter a imagem para escala de cinza
imagem_gray = converter_para_escala_de_cinza(imagem_rgb)

# Aplicar o método de detecção de normais
normals = detect_normals(imagem_gray)

# Salvar e exibir a imagem resultante
plt.imshow(normals)
plt.show()
