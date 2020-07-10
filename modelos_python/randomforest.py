import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

inadimplencia = pd.read_csv('Credito.csv', sep = ';', encoding = 'cp860')
atributos = inadimplencia.iloc[:, 0:19].values
classificacao = inadimplencia.iloc[:, 19].values

labelencoder = LabelEncoder()
atributos[:, 0] = labelencoder.fit_transform(atributos[:, 0])
atributos[:, 2] = labelencoder.fit_transform(atributos[:, 2])
atributos[:, 3] = labelencoder.fit_transform(atributos[:, 3])
atributos[:, 5] = labelencoder.fit_transform(atributos[:, 5])
atributos[:, 6] = labelencoder.fit_transform(atributos[:, 6])
atributos[:, 8] = labelencoder.fit_transform(atributos[:, 8])
atributos[:, 9] = labelencoder.fit_transform(atributos[:, 9])
atributos[:, 11] = labelencoder.fit_transform(atributos[:, 11])
atributos[:, 13] = labelencoder.fit_transform(atributos[:, 13])
atributos[:, 14] = labelencoder.fit_transform(atributos[:, 14])
atributos[:, 16] = labelencoder.fit_transform(atributos[:, 16])
atributos[:, 18] = labelencoder.fit_transform(atributos[:, 18])

atributos_treino, atributos_teste, classificacao_treino, classificacao_teste = train_test_split(atributos, classificacao,
                                                                                                test_size = 0.3, random_state = 42)
floresta = RandomForestClassifier(n_estimators = 150)
floresta.fit(atributos_treino, classificacao_treino)
previsao = floresta.predict(atributos_teste)
taxa_acerto = accuracy_score(classificacao_teste, previsao)
taxa_erro = 1 - taxa_acerto

#apresentado desempenho de 77,3%, reduzindo para 22,6% a taxa de inadimplência