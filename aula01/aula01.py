#------------------Exercicio Aula 01----------- 
import pandas as pd 

csv = pd.read_csv("ratings.csv")

#--------------Analisar as primeiras linhas do arquivo bem como o shape do dataframe
#print(csv.head())

#----------------Sobrescrever os nomes das colunas
#renomeado = csv.rename({"rating": "rateio"}, axis=1)
#print(renomeado)

#----------------Analisar os valores únicos da coluna que contém a nota
#print(csv['rating'].unique)


#-----------------Contar a quantidade de notas aplicadas para cada valor único de nota (value_counts())
#print(csv["rating"].value_counts())

#-----------------Analisar a média das notas dos filmes
print(csv["rating"].mean())