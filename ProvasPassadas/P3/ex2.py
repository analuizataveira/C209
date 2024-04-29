import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#Abra as imagens e retire o canal alpha se necessário
#Exiba as imagens e mostre o formato de cada uma 

horse = np.array(Image.open("ProvasPassadas\P3\horse.jpg"))[:,:,:3]
landscape = np.array(Image.open("ProvasPassadas\P3\landscape.jpg"))[:,:,:3]

plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.imshow(horse)
plt.subplot(2,2,2)
plt.imshow(landscape)

print(horse.shape)
print(landscape.shape)


#Escalonamento com uma função 
def amplify_img(img,sx,sy):
    (l, c ,p) = img.shape

    (ls, cs) = (l*sx,c*sy)

    sc_image = np.zeros(shape=(ls, cs, p), dtype=np.uint8)

    for i in range(ls):
        for j in range(cs):
            new_x= int(np.floor(i * (l / ls)))
            new_y = int(np.floor(j * (c / cs)))

            sc_image[i, j] = img[new_x, new_y]
            
    return sc_image

landscape_big = amplify_img(landscape,2,2)
plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.imshow(landscape_big)
plt.show()

#Grayscale
def grey_scale(img):
    res = (img[:,:,0] * 0.2126 + 
          img[:,:,1] * 0.7152 + 
          img[:,:,2] * 0.0722).astype(np.uint8)
    
    return res

horse_grey = grey_scale(horse)

plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.imshow(horse_grey,cmap="gray")
plt.show()


#Greysclae em binária
def binary(img,thresh):
    (l,c) = img.shape
    res = np.zeros(shape=(l,c,3),dtype=np.uint8)
    
    for i in range(l):
        for j in range(c):
            if img[i,j] > thresh: 
                res[i,j,:] = 255 
            else: 
                res[i,j,:] = 0
    return res

bin_horse = binary(horse_grey,135)    
plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.imshow(bin_horse)
plt.show()

#NOT
horse_not = ~ bin_horse

plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.imshow(horse_not)
plt.show()

#E
op_and = horse_not & landscape_big

plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.imshow(op_and)
plt.show()


#Cisalhamento
def shearing(img, cx, cy):
    (l, c, p) = img.shape
    img_shear = np.zeros((int(l * (1.1 + cy)), int(c * (1.1 + cx)), p), dtype=np.uint8)
    for i in range(l):
        for j in range(c):
            new_x = int(j + cx * i)
            new_y = int(cy * j + i)
        
            img_shear[new_y, new_x] = img[i, j]
            
    return img_shear

res_shear = shearing(op_and, 0.3, 0.2)

plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
plt.imshow(res_shear)
plt.show()


Image.fromarray(res_shear).save("resultado.jpg")