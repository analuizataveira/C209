import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#Abra as imagens mustache.jpg e shrek.png, retire o canal alpha se necessário, exiba essas imagens e mostre o formato de cada uma

mustache = np.array(Image.open("ProvasPassadas\P2\mustache.jpg"))[:,:,:3]
shrek = np.array(Image.open("ProvasPassadas\P2\shrek.png"))[:,:,:3]

plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.imshow(mustache)
plt.subplot(2,2,2)
plt.imshow(shrek)

print(mustache.shape)
print(shrek.shape)
plt.show()


#Crie uma função que realize a reflexão no eixo x, essa função deve receber uma imagem como parâmetro
#e retornar uma imagem refletida no eixo x. 
#Aplique essa função na imagem "mustache" aberta na questão anterior e mostre o resultado.

def reflex_x(img):
    (l,c,p) = img.shape
    img_reflex = np.zeros(shape=img.shape, dtype=np.uint8)
    
    for i in range(l):
        for j in range(c):
            new_y = -i #Espelha o valor de x
            new_x = -j #Espelha o valor de y
            img_reflex[new_y, new_x] = img[i, j]
            
    return img_reflex

mustache_reflex = reflex_x(mustache)

plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.imshow(mustache_reflex)
plt.show()

#Realize a operação lógica NOT com a imagem da questão anterior e mostre o resultado
mustache_not = ~ mustache_reflex

plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.imshow(mustache_not)
plt.show()

# Crie uma função que realize o escalonamento de uma imagem que receba como parâmetro uma 
#**imagem, sx e sy**, sendo sx e sy os fatores de escalonamento e 
#**retorne a imagem escalonada**, em seguida aplique o escalonamento na imagem "shrek" para que fique do mesmo tamanho da imagem da questão anterior. Exiba o resultado.

def amplify_img(img,sx,sy):
    (l, c ,p) = img.shape

    (ls, cs) = (l*sx,c*sy)

    sc_image = np.zeros(shape=(ls, cs, p), dtype=np.uint8)

    #Aplica o nearest neighbor
    for i in range(ls):
        for j in range(cs):
            new_x= int(np.floor(i * (l / ls)))
            new_y = int(np.floor(j * (c / cs)))

            sc_image[i, j] = img[new_x, new_y]
            
    return sc_image

shrek_sc = amplify_img(shrek, 2, 2)
plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.imshow(shrek_sc)
plt.show()


#E entre as imagens anteriores
shrek_final = mustache_not & shrek_sc

plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.imshow(shrek_final)
plt.show()

#Crie uma função para aplicar um método grayscale de sua escolha, 
#que receba como parâmetro uma imagem e retorne uma imagem em greyscale. 
#Aplique essa função na imagem resultante da questão anterior e mostre o resultado.

def grey_scale(img):
    res = (img[:,:,0] * 0.2126 + 
          img[:,:,1] * 0.7152 + 
          img[:,:,2] * 0.0722).astype(np.uint8)
    
    return res

res_grey = grey_scale(shrek_final)
    
plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.imshow(res_grey, cmap="gray")
plt.show()


#Crie uma função que realize uma rotação com interpolação, a função deve receber como parâmetro 
#uma imagem e o ângulo alpha com que deve ser rotacionada** e **retornar uma imagem rotacionada com o angulo alpha. Modifique o algoritmo de rotação para que funcione se necessário. Aplique a função na imagem resultante da questão anterior com **ângulo de 60°** e mostre o resultado.
def rotation(img,alpha):
    (l , c) = img.shape
    ls, cs = int(l * np.sqrt(2)), int(c * np.sqrt(2))
    img_rot = np.zeros((ls, cs), dtype=np.uint8)
    
    for i in range(ls):
        for j in range(cs):
            cx = j - (ls / 2)
            cy = i - (cs / 2)
        
            new_x = int( cx * np.cos(alpha) + cy * np.sin(alpha) + l / 2)
            new_y = int(-cx * np.sin(alpha) + cy * np.cos(alpha) + c / 2)
        
            if 0 <= new_x < c and 0 <= new_y < l:
                img_rot[i, j] = img[new_y, new_x]
    
    return img_rot

alpha = np.pi / 3 # 60°

res_rotate = rotation(res_grey,alpha)
plt.figure(figsize=(8, 8))
plt.imshow(res_rotate, cmap="gray")
plt.show()

#Salve a imagem da questão anterior no disco com o nome "resultado.jpg
Image.fromarray(res_rotate).save("resultado.jpg")