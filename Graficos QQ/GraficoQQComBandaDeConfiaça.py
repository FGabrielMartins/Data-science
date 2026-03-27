import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset_ciencia_dados.csv', nrows=50)

print(df.head())

#Criando o gráfico com a bibl Seaborn
sns.regplot(x = "nota_estatistica", y = "nota_python", data=df,
            ci= 95, #Nível de confiança (95%)
            scatter_kws= {'alpha':0.7}, #Opacidade dos pontos
            line_kws={'color':'green'})

plt.title("Gráfico QQ Com banda ") 

plt.grid()
plt.show()
