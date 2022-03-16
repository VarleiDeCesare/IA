import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

aluguel = pd.read_csv("../aluguel.csv", sep=";")

#1
# print(aluguel.shape)

# 2
# print(len(aluguel['Tipo'].unique()))

#3
# print(len(aluguel.Bairro.unique()))

#4
# print("Quarto, média: ", aluguel.Quartos.mean(), " mediana: ", aluguel.Quartos.median(), " desvio padrão de qualidade ", aluguel.Quartos.std())
# print("Vagas, média: ", aluguel.Vagas.mean(), " mediana: ", aluguel.Vagas.median(), " desvio padrão de qualidade ", aluguel.Vagas.std())
# print("Suites, média: ", aluguel.Suites.mean(), " mediana: ", aluguel.Suites.median(), " desvio padrão de qualidade ", aluguel.Suites.std())
# print("Área, média: ", aluguel.Area.mean(), " mediana: ", aluguel.Area.median(), " desvio padrão de qualidade ", aluguel.Area.std())
# print("Valor, média: ", aluguel.Valor.mean(), " mediana: ", aluguel.Valor.median(), " desvio padrão de qualidade ", aluguel.Valor.std())
# print("Condominio, média: ", aluguel.Quartos.mean(), " mediana: ", aluguel.Quartos.median(), " desvio padrão de qualidade ", aluguel.Quartos.std())
# print("IPTU, média: ", aluguel.IPTU.mean(), " mediana: ", aluguel.IPTU.median(), " desvio padrão de qualidade ", aluguel.IPTU.std())

#5
#sim tem colunas categoricas, bairro e tipo

#6
#Sim tem outliers
# sns.boxplot(aluguel.Valor)

#7
# bairros = aluguel.groupby(by=["Bairro"]).mean().Valor.sort_values
# bairros.plot(kind='hist')

#8
# aluguel.groupby(by=["Tipo"]).mean().Valor.sort_values(ascending = False).head(1)

# aluguel.groupby(by=["Tipo"]).mean().Valor.sort_values(ascending = False).tail(1)


#9
# print(aluguel.query("Tipo == 'Apartamento'"));

#10
# print(aluguel.query("Tipo == 'Apartamento' or Tipo == 'Casa'"));


#11
# print(aluguel.query("Area >= 60 and Area <= 100"));

#12
#Condominio e Aluguel tem coorelação enquanto Aluguel e IPTU não tem coorelação.
# plt.figure(figsize=(12, 6))
# plt.scatter(aluguel["Condominio"], aluguel["Valor"], alpha=0.2)
# plt.xlabel("Aluguel")
# plt.ylabel("IPTU")

#13
#sim contem dados faltantes
# print(aluguel[aluguel.isna().any(axis=1)])

#14
#Sim é possivel a base é suficiente, pois tem uma boa quantidade de dados e os dados possuem uma varieidade e uma coorelação que permite um bom entendimento do conteúdo em si.

plt.show()