from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Crie uma função `mirror`, que recebe `img` (`np.array`), `reverse_x` (`bool`) e `reverse_y` (`bool`) 
# retorna uma nova imagem, onde caso `reverse_EIXO` seja verdadeiro, esta deve ser `img` espelhada em EIXO. Em seguida, teste sua função com uma imagem de sua escolha.


def mirror(img, reverse_x=False, reverse_y=False):
    l, c, p = img.shape
    new_img = np.zeros(shape=img.shape, dtype=np.uint8)
    
    if reverse_x:
        new_img = img[::-1, ::1]
        plt.imshow(new_img)
        plt.title("Reflexão Horizontal (Mirror)")
        plt.show()
    
    if reverse_y:
        new_img = img[:, ::-1]
        plt.imshow(new_img)
        plt.title("Reflexão Vertical (Mirror)")
        plt.show()
    
    return new_img

# Função para reflexão vertical
def reflection_y(img):
    l, c, p = img.shape
    img_refl_y = np.zeros(shape=img.shape, dtype=np.uint8)
    for i in range(l):
        for j in range(c):
            new_x = -j
            new_y = i
            img_refl_y[new_y, new_x] = img[i, j]
    plt.imshow(img_refl_y)
    plt.show()
    return img_refl_y

# Função para reflexão horizontal
def reflection_x(img):
    l, c, p = img.shape
    img_refl_x = np.zeros(shape=img.shape, dtype=np.uint8)
    img_refl_x[::-1, ::1] = img
    plt.imshow(img_refl_x)
    plt.show()
    return img_refl_x

# Carregar a imagem do Mario
mario = np.array(Image.open('./mario.png'))[:, :, :3]
(l, c, p) = mario.shape

# Reflexão vertical usando a função reflection_y
mario_refl_y_function = reflection_y(mario)

# Reflexão horizontal usando a função reflection_x
mario_refl_x_function = reflection_x(mario)