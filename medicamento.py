import numpy as np
import matplotlib.pyplot as plt

remedios = ['Remedio1', 'Remedio2', 'Remedio3']
sintomas = ['Sintoma1', 'Sintoma2', 'Sintoma3']

# Definir a matriz de eficácias (linhas: sintomas, colunas: remédios)
eficacias = np.array([
    # R1,  R2,  R3
    [0.45, 0.67, 0.32], # s1 
    [0.67, 0.75, 0.49], # s2
    [0.67, 0.76, 0.87], # s3
])

# Calcular a soma das eficácias para cada remédio
soma_eficacias = np.sum(eficacias, axis=0)

# Encontrar o índice do remédio com a maior soma de eficácias 
indice_melhor_remedio = np.argmax(soma_eficacias) 

melhor_remedio = remedios[indice_melhor_remedio] 

print(f"O melhor remédio para tratar a maioria dos sintomas é: {melhor_remedio}")

fig, ax = plt.subplots()
barras = ax.bar(remedios, soma_eficacias, color=['blue', 'orange', 'green'])

ax.set_xlabel('Remédios')
ax.set_ylabel('Soma das Eficácias')
ax.set_title('Eficácia Total')

for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2., altura,
            f'{altura:.2f}', ha='center', va='bottom')

plt.show()