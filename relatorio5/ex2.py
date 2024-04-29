from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

#Escolha uma imagem qualquer e realize um cisalhamento nela, sendo os fatores de sua escolha.

# Carregar a imagem do Mario
mario = np.array(Image.open('mario.png'))[:, :, :3]
(l, c, p) = mario.shape

(cx,cy) = (0.3,0.2)

sh_img = np.zeros(shape=(int(l*(1+cy)),int(c*(1+cx)),p),dtype=np.uint8)

for i in range(l):
    for j in range(c):
        new_x = int(i + j*cy)
        new_y = int(j + i*cx) 
        sh_img[new_x,new_y] = mario[i,j]
        
plt.title('Imagem com cisalhamento')        
plt.imshow(sh_img)  
plt.show()