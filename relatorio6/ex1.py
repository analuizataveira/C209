import numpy as np
from PIL import Image

def rgb_to_hsv(rgb_image):
    # Normalizar os valores de R, G e B para a faixa [0, 1]
    r = rgb_image[:, :, 0] / 255
    g = rgb_image[:, :, 1] / 255
    b = rgb_image[:, :, 2] / 255
    
    # Encontrar os valores máximos e mínimos de R, G e B
    c_max = np.maximum(np.maximum(r, g), b)
    c_min = np.minimum(np.minimum(r, g), b)
    
    # Calcular delta
    delta = c_max - c_min
    
    # Inicializar arrays para H, S e V
    h = np.zeros_like(c_max)
    s = np.zeros_like(c_max)
    v = np.zeros_like(c_max)
    
    # Calcular H
    h[np.where(delta == 0)] = 0
    h[np.where(c_max == r)] = 60 * ((g[np.where(c_max == r)] - b[np.where(c_max == r)]) / delta[np.where(c_max == r)]) % 6
    h[np.where(c_max == g)] = 60 * ((b[np.where(c_max == g)] - r[np.where(c_max == g)]) / delta[np.where(c_max == g)] + 2)
    h[np.where(c_max == b)] = 60 * ((r[np.where(c_max == b)] - g[np.where(c_max == b)]) / delta[np.where(c_max == b)] + 4)
    
    # Calcular S
    s[np.where(c_max != 0)] = delta[np.where(c_max != 0)] / c_max[np.where(c_max != 0)]
    
    # Calcular V
    v = c_max
    
    # Converter H para a faixa [0, 1] (ou [0, 255] para np.uint8)
    h = h / 360
    
    # Converter H, S e V para [0, 255]
    h *= 255
    s *= 255
    v *= 255
    
    # Criar matriz HSV
    hsv_image = np.zeros_like(rgb_image)
    hsv_image[:, :, 0] = h.astype(np.uint8)
    hsv_image[:, :, 1] = s.astype(np.uint8)
    hsv_image[:, :, 2] = v.astype(np.uint8)
    
    return hsv_image

# Carregar a imagem RGB de entrada
img = Image.open("colors_rgb.png")
img_rgb = np.array(img)
l, c, p = img_rgb.shape

# Converter RGB para HSV
img_hsv = rgb_to_hsv(img_rgb)

# Exibir a imagem HSV resultante
Image.fromarray(img_hsv, mode='HSV').convert('RGB').show()
