# Alunos: João Pedro Braga, Rita de Cássia, Luana Teixeira de Moraes, Gabriel Luiz Garcia


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem pré-processada
imagem_pre_processada = cv2.imread('imagens/saida/pre_processada.jpg', 0)

# Definir um limiar para inferir a presença de câncer
limiar = 100

# Contar o número de pixels com valor acima do limiar
contagem_pix = np.sum(imagem_pre_processada > limiar)

# Decidir se há câncer com base na quantidade de bordas detectadas
if contagem_pix > 1000:  # Limite arbitrário
    resultado = "Câncer detectado"
else:
    resultado = "Câncer não detectado"

# Exibir o resultado
plt.imshow(imagem_pre_processada, cmap='gray')
plt.title(f'Resultado da análise: {resultado}')
plt.show()
