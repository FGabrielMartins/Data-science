import pandas as pd
import numpy as np

np.random.seed(10)

n = 1000

dados = pd.DataFrame({
    "idade": np.random.randint(18, 35, n),
    "horas_estudo": np.random.normal(4.5, 1.5, n).round(1),
    "sono": np.random.normal(7, 1, n).round(1),
    "projetos": np.random.randint(0, 6, n),
    "cafe": np.random.randint(0, 5, n)
})

dados["nota_estatistica"] = (dados["horas_estudo"]*1.2 +
                             dados["sono"]*0.5 +
                             np.random.normal(0,1,n)).round(1)

dados["nota_python"] = (dados["horas_estudo"]*1.4 +
                        dados["projetos"]*0.8 +
                        np.random.normal(0,1,n)).round(1)

dados["aprovado"] = ((dados["nota_estatistica"] +
                      dados["nota_python"]) > 14).astype(int)

dados.to_csv("dataset_ciencia_dados.csv", index=False)

print(dados.head())