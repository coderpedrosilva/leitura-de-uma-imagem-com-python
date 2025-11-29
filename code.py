#Leitura de uma imagem
# Importar bibliotecas
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Leitura da imagem
img = cv2.imread('imagem.png')
 
# Apresentação da imagem na tela
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
