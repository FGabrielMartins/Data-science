import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

carregar_arquivos_csv = pd.read_csv ('dataset_ciencia_dados.csv') 

#exibir as primeiras linhas
print(carregar_arquivos_csv.head())

#Gráficos de disperção unidimencional de muitos valores
#dotplot básico
plt.scatter( #scatter espalhar
    carregar_arquivos_csv.index,
    carregar_arquivos_csv["idade"]
)

plt.title("Dotplot - Nota de Estatistica")
plt.xlabel("Tamanho do ROL")
plt.ylabel("Idade")

plt.show()

#dotplot melhor
plt.figure(figsize=(8, 4))

plt.scatter( #espalhar
    carregar_arquivos_csv["idade"],
    [1]*len(carregar_arquivos_csv),
    alpha = 0.6
)

plt.yticks([])
plt.xlabel("Notas Estatisticas")
plt.ylabel("Dotplot das notas")

plt.show()

#dotplot com duas variaveis
plt.scatter(
    carregar_arquivos_csv["idade"],
    carregar_arquivos_csv["horas_estudo"]
)

plt.xlabel("Idade")
plt.ylabel("Horas de estudos")
plt.title("Dotplot: Idade vs Horas de estudos")

plt.show()

#dotplot usando Seaborn
sns.stripplot( 
    x = carregar_arquivos_csv["nota_estatistica"]
)

plt.title("Distribuição de notas")

plt.show()