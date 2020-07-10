library(rpart)

inandimplencia = read.csv(file.choose(), sep = ';', header = T)
head(inandimplencia)
dim(inandimplencia)
inandimplencia$CLASSE = as.factor(inandimplencia$CLASSE)

amostra = sample(2, 1000, replace = T, prob = c(0.75, 0.25))
previsores = inandimplencia[amostra == 1, ]
resposta = inandimplencia[amostra == 2, ]

arvore = rpart(CLASSE ~ . , previsores, method = 'class')
plot(arvore)
text(arvore, une.n = T, all = T, cex=.8)

previsao = predict(arvore, resposta)
inandimplentes = cbind(resposta, previsao)
fix(inandimplentes)
inandimplentes['RESULTADO'] = ifelse(inandimplentes$ruim >= 0.5, 'ruim', 'bom')

matriz_confusao = table(inandimplentes$CLASSE, inandimplentes$RESULTADO)
plot(matriz_confusao)
taxa_acerto = (matriz_confusao[1] + matriz_confusao[4]) / sum(matriz_confusao)
taxa_erro = (matriz_confusao[2] + matriz_confusao[3]) / sum(matriz_confusao)

#desenpenho de 74,7%, reduzindo para 25,3% a taxa de inadimplência