import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread('imagens/entrada/cancer_de_mama.jpg')

# Converter para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplicar suavização (blur)
imagem_suavizada = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)

# Detecção de bordas usando Canny
bordas = cv2.Canny(imagem_suavizada, 50, 150)

# Salvar a imagem pré-processada
cv2.imwrite('imagens/saida/pre_processada.jpg', bordas)

# Exibir as imagens
plt.subplot(1, 2, 1)
plt.imshow(imagem_cinza, cmap='gray')
plt.title('Imagem em Escala de Cinza')

plt.subplot(1, 2, 2)
plt.imshow(bordas, cmap='gray')
plt.title('Imagem Pré-processada (Bordas)')

plt.show()