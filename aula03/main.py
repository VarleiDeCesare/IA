from os import sep
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_cerveja = pd.read_csv("../consumo_cerveja.csv", sep=";")

#-------------------Qual o tamanho?
#print(df_cerveja.shape)
#Tamanho 365 linhas por 7 colunas.

#-------------------Existem dados faltantes?
#df_cerveja2 = df_cerveja.dropna(how='all', axis=0)
#print(df_cerveja.shape, df_cerveja2.shape)
# Nao tem dados faltantes

#-------------------Existem outliers? Se sim, remova-os
#O Dataframe nao tem outliers 

# De qualquer forma aqui esta a funcao para limpar possiveis outsliers.
def retiraOutLiers(coluna):
    Q1 = df_cerveja[coluna].quantile(.25)
    Q3 = df_cerveja[coluna].quantile(.75)

    IIQ = Q3 - Q1

    limite_inferior = Q1 - 1.5 * IIQ
    limite_superior = Q3 - 1.5 * IIQ

    selecao = (df_cerveja[coluna] >= limite_inferior) & (df_cerveja[coluna] <= limite_superior)
    
    return df_cerveja[selecao]

df_cerveja_sem_outliers = retiraOutLiers('consumo')

#-------------------Qual o consumo medio de cerveja?
#print(df_cerveja.consumo.mean().round(2))
# Consumo medio de 25401.37 Litros

#-------------------Qual o consumo medio em dias de chuva?
# Consumo medio de 23237.0 litros
#print(df_cerveja.query("chuva == '1'").consumo.mean())

#-------------------Qual o consumo medio quando esta frio?
#print(df_cerveja.query("temp_media <= 20").consumo.mean().round(2))
#Consumo medio de 22625.33 litros

#-------------------Entre quais colunas existe correlacao?
plt.scatter(x=df_cerveja['chuva'], y=df_cerveja['temp_max'])
plt.show()
#Existe coorelação entre chuva e consumo, quanto menos chuva, maior o consumo.

#-------------------Quais colunas são fortes preditoras para o consumo de cerveja?
#Coluna de chuva, indica fortemente que quanto menos chuva, maior é a indicação das pessoas consumirem cerveja.
