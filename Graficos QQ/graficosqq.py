import pandas as pd
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

#Lê apenas as 30 primeiras linhas
carregar_dados = pd.read_csv('dataset_ciencia_dados.csv', nrows=30)

print(carregar_dados.head())

#Gráficos QQ simples
stats.probplot(carregar_dados["nota_estatistica"], dist="norm", plot=plt)
#stats.probplot = Ela faz os cálculos matemáticos para comparar os seus dados com uma distribuição teórica.
#1 ordena os dados
#2 calcula quantis teóricos
#3 cria o gráfico QQ
#dist="norm" = Distribuição Normal

plt.title("QQ plot - NOtas de Estatística")

plt.grid()
plt.show()

#Gráficos QQ de outra variavel
stats.probplot(carregar_dados["horas_estudo"], dist="norm", plot=plt)

plt.title("QQ plot - Horas de Estudos")

plt.grid()
plt.show()

#Gráficos QQ manual
dados = carregar_dados["sono"]

dados_ordenados = np.sort(dados) #A função np.sort() do NumPy ordena arrays (matrizes ou vetores) de forma eficiente, permitindo organizar dados numéricos ou estruturados. Ela possibilita definir o eixo de ordenação (axis), escolher algoritmos como 'quicksort', 'mergesort' ou 'heapsort' (kind), e ordenar campos específicos em arrays estruturados (order).

n = len(dados) #len = tamnho/quantidades de dados

probabilidades = [(i - 0.5)/n for i in range(1, n+1)] #range = gera uma sequencia imutavel de numeros inteiros

quantis_teoricos = stats.norm.ppf(probabilidades)

plt.scatter(quantis_teoricos, dados_ordenados)

plt.title("QQ plot manual Das horas de Sono")
plt.xlabel("Quantis téoricos")
plt.ylabel("Quantis da Amostra")

plt.grid()
plt.show()