import cv2
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread('imagens/entrada/cancer_de_mama.jpg')

# Separar os canais de cor
canal_vermelho = imagem.copy()
canal_vermelho[:, :, 1] = 0  # Zera o canal verde
canal_vermelho[:, :, 2] = 0  # Zera o canal azul

canal_verde = imagem.copy()
canal_verde[:, :, 0] = 0  # Zera o canal vermelho
canal_verde[:, :, 2] = 0  # Zera o canal azul

canal_azul = imagem.copy()
canal_azul[:, :, 0] = 0  # Zera o canal vermelho
canal_azul[:, :, 1] = 0  # Zera o canal verde

# Salvar os canais como imagens
cv2.imwrite('imagens/saida/canal_vermelho.jpg', canal_vermelho)
cv2.imwrite('imagens/saida/canal_verde.jpg', canal_verde)
cv2.imwrite('imagens/saida/canal_azul.jpg', canal_azul)

# Exibir as imagens
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(canal_vermelho, cv2.COLOR_BGR2RGB))
plt.title('Canal Vermelho')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(canal_verde, cv2.COLOR_BGR2RGB))
plt.title('Canal Verde')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(canal_azul, cv2.COLOR_BGR2RGB))
plt.title('Canal Azul')

plt.show()