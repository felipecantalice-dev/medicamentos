import numpy as np
import matplotlib.pyplot as plt

remedios = ['RemedioA', 'RemedioB', 'RemedioC']
sintomas = ['Sintoma1', 'Sintoma2', 'Sintoma3', 'Sintoma4']

# Definir a matriz de eficácias (linhas: sintomas, colunas: remédios)
eficacias = np.array([
    [0.5, 0.5, 0.5, 0.5],  
    [0.5, 0.5, 0.5, 0.5], 
    [0.5, 0.5, 0.5, 0.5],  
])

# Calcular a soma das eficácias para cada remédio
soma_eficacias = np.sum(eficacias, axis=1)

# Encontrar o índice do remédio com a maior soma de eficácias 
indice_melhor_remedio = np.argmax(soma_eficacias) 

melhor_remedio = remedios[indice_melhor_remedio] 

print(f"O melhor remédio para tratar a maioria dos sintomas é: {melhor_remedio}")

fig, ax = plt.subplots()
barras = ax.bar(remedios, soma_eficacias, color=['blue', 'orange', 'green'])

ax.set_xlabel('Remédios')
ax.set_ylabel('Soma das Eficácias')
ax.set_title('Eficácia Total dos Remédios no Tratamento dos Sintomas')

for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2., 1.05*altura,
            f'{altura:.2f}', ha='center', va='bottom')

plt.show()