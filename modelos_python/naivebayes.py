import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest

inadimplencia = pd.read_csv('Credito.csv', sep = ';', encoding = 'cp860')
P = inadimplencia.iloc[:, 0:19].values
C = inadimplencia.iloc[:, 19].values

labelencoder = LabelEncoder()
P[:, 0] = labelencoder.fit_transform(P[:, 0])
P[:, 2] = labelencoder.fit_transform(P[:, 2])
P[:, 3] = labelencoder.fit_transform(P[:, 3])
P[:, 5] = labelencoder.fit_transform(P[:, 5])
P[:, 6] = labelencoder.fit_transform(P[:, 6])
P[:, 8] = labelencoder.fit_transform(P[:, 8])
P[:, 9] = labelencoder.fit_transform(P[:, 9])
P[:, 11] = labelencoder.fit_transform(P[:, 11])
P[:, 13] = labelencoder.fit_transform(P[:, 13])
P[:, 14] = labelencoder.fit_transform(P[:, 14])
P[:, 16] = labelencoder.fit_transform(P[:, 16])
P[:, 18] = labelencoder.fit_transform(P[:, 18])

P_treino, P_teste, C_treino, C_teste = train_test_split(P, C, test_size = 0.25, random_state = 42)

modelo1 = GaussianNB()
modelo1.fit(P_treino, C_treino)
previsao = modelo1.predict(P_teste)
taxadeacerto = accuracy_score(C_teste, previsao)
taxadeerro = 1 - taxadeacerto

#Seleção de atributos
selecao = SelectKBest(chi2, k = 5)
P_novo = selecao.fit_transform(P, C)

P_novo_treino, P_novo_teste, C_novo_treino, C_novo_teste = train_test_split(P_novo, C, 
                                                                            test_size = 0.15, random_state = 42)

modelo2 = GaussianNB()
modelo2.fit(P_novo_treino, C_novo_treino)
previsao2 = modelo2.predict(P_novo_teste)
taxa_acerto = accuracy_score(C_novo_teste, previsao2)
taxa_erro = 1 - taxa_acerto

#com seleção de atributos: apresenta desempenho de 76%, reduzindo para 24% a taxa de inadimplência
#sem seleção de atributos: apresenta desempenho de 72,4%, reduzindo para 27,6% a taxa de inadimplência