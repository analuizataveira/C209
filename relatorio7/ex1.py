from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#Aplique HDR a alguma imagem

# Carregar a imagem
img = np.array(Image.open('cookie.jpg'))

# Normalizar os valores da imagem para [0, 1]
img_norm = img.astype(np.float64) / 255

# Encontrar o valor mais claro e o mais escuro da imagem
valor_mais_claro = np.max(img_norm)
valor_mais_escuro = np.min(img_norm)

# Calcular a razão entre o valor mais claro e o mais escuro
ratio = valor_mais_claro / valor_mais_escuro

# Aplicar a razão à imagem
img_hdr = (img_norm * ratio).astype(np.uint8)

# Calcular a média aritmética entre os valores mais claro e mais escuro
media_valores = (valor_mais_claro + valor_mais_escuro) / 2

# Salvar e exibir a imagem HDR resultante
Image.fromarray((img_hdr * 255).astype(np.uint8)).show()