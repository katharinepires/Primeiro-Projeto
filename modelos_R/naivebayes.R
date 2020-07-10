library(e1071)
library(rpart)
library(klaR)
library(FSelector)

inadimplencia = read.csv(file.choose(), sep = ';', header = T)
inadimplencia$CLASSE = as.factor(inadimplencia$CLASSE)

#sem seleção de traibutos:
amostragem = sample(2, 1000, replace = T, prob = c(0.80, 0.20))
P_treino = inadimplencia[amostragem == 1, ]
C_teste = inadimplencia[amostragem == 2, ]

modelo1 = naiveBayes(CLASSE ~ . , P_treino)
modelo1
previsao1 = predict(modelo1, C_teste)

matriz_confusao1 = table(C_teste$CLASSE, previsao1)
taxa_de_acerto1 = (matriz_confusao1[1] + matriz_confusao1[4]) / sum(matriz_confusao1)
taxa_de_erro1 = (matriz_confusao1[2] + matriz_confusao1[3]) / sum(matriz_confusao1)

#seleção de atributos:
random.forest.importance(CLASSE ~ . , inadimplencia)

modelo2 = naiveBayes(CLASSE ~ CHEQUEESPECIAL + USO_CREDITO + HISTORICO_CREDITO + BALANCO_ATUAL + BALANCO_MEDIO_CREDITO + IDADE, P_treino)
previsao2 = predict(modelo2, C_teste)

matriz_confusao2 = table(C_teste$CLASSE, previsao2)
taxa_de_acerto2 = (matriz_confusao2[1] + matriz_confusao2[4]) / sum(matriz_confusao2)
taxa_de_erro2 = (matriz_confusao2[2] + matriz_confusao2[3]) / sum(matriz_confusao2)

#sem atributos: nível de inadimplência cai para 24%, tem desempenho de 75,9%
#com atributos: nível de inadimplência cai para 23%, tem desempenho de 76,9%