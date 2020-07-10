library(randomForest)

inadimplencias = read.csv(file.choose(), sep = ';', header = T)
amostras = sample(2, 1000, replace = T, prob = c(0.75, 0.25))
atributos_treino = inadimplencias[amostras == 1, ]
atributos_teste = inadimplencias[amostras == 2, ]

floresta = randomForest(CLASSE ~ . , atributos_treino, ntree = 100, proximity = T)
previsao = predict(floresta, atributos_teste)

floresta$importance

matriz_confusao = table(atributos_teste$CLASSE, previsao)
taxa_de_acerto = (matriz_confusao[1] + matriz_confusao[4]) / sum(matriz_confusao)
taxa_de_erro = (matriz_confusao[2] + matriz_confusao[3]) / sum(matriz_confusao)

#nível de inadimplêmcia cai para 21,9%, tem desempenho de 78%