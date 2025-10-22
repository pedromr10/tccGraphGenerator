import pandas as pd
import matplotlib.pyplot as plt

#GRAFICO EMOCOES:
#mostra a quantidade de informacoes retiradas e quantas estavam certas:
df = pd.DataFrame({
    'Emotion': ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"],
    'Total emotions': [0, 0, 0, 0, 0, 0, 0],
    'Correct emotions': [0, 0, 0, 0, 0, 0, 0]
})
#cria um grafico de barras:
df.plot(x='Emotion', kind='bar', y=['Total emotions', 'Correct emotions'], title='Detected vs. Correctly Detected Emotions - Insira o nome aqui')
#ajuste de layout:
plt.ylabel('Number of images')
plt.xticks(rotation=0)
plt.tight_layout()
#salva como imagem:
plt.savefig('grafico_emocoes.png')
#plt.show()

#GRAFICO IDENTIFICACAO YOLO:
#mostra a quantidade de informacoes retiradas e quantas estavam certas:
labels = ['Total object identifications', 'Correct object identifications']
values = [100, 83] #total / certas
plt.figure(figsize=(6,4))
plt.bar(labels, values, color=['skyblue', 'lightgreen'], width=0.4)
plt.title('Detected vs. Correctly Detected Objects - Insira o nome aqui')
plt.ylabel('Number of Identifications')
plt.tight_layout()
plt.savefig('grafico_identificacao_yolo.png')
#plt.show()