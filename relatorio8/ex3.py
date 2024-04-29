import numpy as np
from PIL import Image

#Realize uma operação de threshold nas imagens e repita as operações acima.

# Carregar as imagens dos lados 3, 4 e 6
side_3 = np.array(Image.open('three.png'))
side_4 = np.array(Image.open('four.png'))
side_6 = np.array(Image.open('six.png'))

# Calcular as faces faltantes (1, 2 e 5) utilizando operações lógicas
# Face 1 = Lado 3 OR Lado 4
side_1 = np.logical_or(side_3, side_4).astype(np.uint8) * 255

# Face 2 = Lado 4 OR Lado 6
side_2 = np.logical_or(side_4, side_6).astype(np.uint8) * 255

# Face 5 = NOT(Lado 6)
side_5 = np.logical_not(side_6).astype(np.uint8) * 255

# Salvar as imagens resultantes
Image.fromarray(side_1).save('side_1.png')
Image.fromarray(side_2).save('side_2.png')
Image.fromarray(side_5).save('side_5.png')