import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure 
notas = pd.read_csv("../ratings.csv")

#1)
#notas["rating"].plot(kind='hist')

#2)
#sns.boxplot(notas["rating"])

#3)
#print(notas["rating"].describe)

#4)
filmes = pd.read_csv("../movies.csv")

#5)
filmes = filmes.rename({"movieId": "FilmeID", "title": "Titulo", "genres": "genero"}, axis=1)

#6)
#print(filmes.query("FilmeID==1 or FilmeID==2"))

#7)
#print(notas.query("movieId==1 or movieId==2")['rating'].mean())

#8)
#print(notas.groupby("movieId")["rating"].mean())

#9)
#notas.groupby("movieId")["rating"].mean().plot(kind='hist')

#10)
#sns.boxplot(notas.groupby("movieId")["rating"].mean())

#11)
#sns.displot(notas.groupby("movieId")["rating"].mean())

#12)
#sns.displot(notas.groupby("movieId")["rating"].mean(), bins=10)

#13)
#plt.hist(notas.groupby("movieId")["rating"].mean())
#plt.title("Título Teste")

#14)
plt.figure(figsize=(10,10))
plt.hist(notas.groupby("movieId")["rating"].mean())
plt.title("Título Teste")
plt.show()