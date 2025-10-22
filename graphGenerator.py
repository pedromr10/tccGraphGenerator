import pandas as pd
import matplotlib.pyplot as plt

#GRAFICO EMOCOES:
#mostra a quantidade de informacoes retiradas e quantas estavam certas:
df = pd.DataFrame({
    'Emotion': ["sad", "angry", "happy", "neutral"],
    'Total emotions': [100, 120, 130, 150],
    'Correct emotions': [80, 90, 110, 140]
})
#cria um grafico de barras:
df.plot(x='Emotion', kind='bar', y=['Total emotions', 'Correct emotions'], title='Comparison Between Total and Correctly Detected Emotions')
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
values = [200, 170] #total / certas
plt.figure(figsize=(6,4))
plt.bar(labels, values, color=['skyblue', 'lightgreen'])
plt.title('Comparison Between Total and Correctly Detected Objects')
plt.ylabel('Number of Identifications')
plt.tight_layout()
plt.savefig('grafico_identificacao_yolo.png')
#plt.show()