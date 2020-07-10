import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix

inadimplencia = pd.read_csv('Credito.csv', sep = ';', encoding = 'cp860')
#separação entre atributos previsores e atributos de classificação
previsores = inadimplencia.iloc[:, 0:19].values
classe = inadimplencia.iloc[:, 19].values
#tranformar as categorias para realizar as codificações
labelencoder = LabelEncoder()
previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 2])
previsores[:, 3] = labelencoder.fit_transform(previsores[:, 3])
previsores[:, 5] = labelencoder.fit_transform(previsores[:, 5])
previsores[:, 6] = labelencoder.fit_transform(previsores[:, 6])
previsores[:, 8] = labelencoder.fit_transform(previsores[:, 8])
previsores[:, 9] = labelencoder.fit_transform(previsores[:, 9])
previsores[:, 11] = labelencoder.fit_transform(previsores[:, 11])
previsores[:, 13] = labelencoder.fit_transform(previsores[:, 13])
previsores[:, 14] = labelencoder.fit_transform(previsores[:, 14])
previsores[:, 16] = labelencoder.fit_transform(previsores[:, 16])
previsores[:, 18] = labelencoder.fit_transform(previsores[:, 18])

previsores_treino, previsores_teste, classe_treino, classe_teste = train_test_split(previsores, 
                                                                                     classe, 
                                                                                     test_size = 0.20, 
                                                                                     random_state = 42)

modelo = DecisionTreeClassifier(criterion = 'entropy')
modelo.fit(previsores_treino, classe_treino)
export_graphviz(modelo, out_file = 'Árvore.dot')
previsao = modelo.predict(previsores_teste)
taxa_acerto = accuracy_score(classe_teste, previsao)
taxa_erro = 1 - taxa_acerto

#achado um desempenho de 72,5%, a taxa de inadimplência caiu para 27,5%