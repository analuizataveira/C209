import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def bilinear_interpolation(image, output_shape):
    # Obter dimensões da imagem de entrada e da imagem de saída
    input_height, input_width = image.shape[:2]
    output_height, output_width = output_shape
    
    # Fatores de escala
    scale_height = input_height / output_height
    scale_width = input_width / output_width
    
    # Criar imagem de saída
    output_image = np.zeros((output_height, output_width, image.shape[2]), dtype=np.uint8)
    
    # Iterar sobre os pixels da imagem de saída
    for y_out in range(output_height):
        for x_out in range(output_width):
            # Calcular coordenadas na imagem de entrada
            y_in = y_out * scale_height
            x_in = x_out * scale_width
            
            # Calcular os índices dos pixels vizinhos na imagem de entrada
            y0 = int(np.floor(y_in))
            x0 = int(np.floor(x_in))
            y1 = min(y0 + 1, input_height - 1)
            x1 = min(x0 + 1, input_width - 1)
            
            # Calcular as diferenças entre as coordenadas atuais e os índices dos pixels vizinhos
            dy = y_in - y0
            dx = x_in - x0
            
            # Interpolação bilinear
            interpolated_value = (1 - dy) * (1 - dx) * image[y0, x0] + \
                                 dy * (1 - dx) * image[y1, x0] + \
                                 (1 - dy) * dx * image[y0, x1] + \
                                 dy * dx * image[y1, x1]
            
            # Atribuir o valor interpolado à imagem de saída
            output_image[y_out, x_out] = interpolated_value.astype(np.uint8)
    
    return output_image

# Carregar a imagem do Mario
mario = np.array(Image.open('mario.png'))[:, :, :3]
(l, c, p) = mario.shape

# Definir as dimensões da imagem de saída desejada
new_height, new_width = 300, 300

# Aplicar interpolação bilinear
rescaled_mario = bilinear_interpolation(mario, (new_height, new_width))

# Exibir a imagem resultante
plt.imshow(rescaled_mario)
plt.title("Imagem do Mario após Interpolação Bilinear")
plt.axis('off')  # Desabilitar os eixos
plt.show()
