# Primeiro Projeto em Python e R
Como atividade final de um curso realizado, foi disponibilizado um arquivo contendo dados de clientes de uma instituição financeira e me foi desafiado reduzir o nível de inadimplência da empresa. Atualmente eles operam com 35% de inadimplentes, clientes que não pagam contas ou dívidas.
Foram criadas três técnicas, dessa maneira pode-se escolher o modelo que mais atende ao que foi proposto: reduzir a taxa de inadimplência.

* 1º modelo – Árvore de decisão: Criação da uma árvore para a classificação da inadimplência, calculada a entropia, se tem a árvore completa para responder ao que lhe foi prosposto.

* 2 º modelo – Naive Bayes com seleção de atributos: Criado um modelo nos moldes Naive Bayes, se selecionou os atributos mais significantes para uma melhor precisão das respostas, chegando assim a uma classificação mais próxima da real.

* 3º modelo – Random Forest: Criação de várias árvores aleatórias, elas irão retornar o melhor modelo de acordo com as respostas combinadas dessas árvores criadas.

## Python
Depois do comando ``` export_graphviz(modelo, out_file = 'seuarquivo.dot')```, um arquivo será criado e será encontrado no mesmo caminho que se encontra o seu código .py. Para saber como ficou, abra o arquivo .dot, copie todo o código ali escrito e cole [nesse site aqui]( https://dreampuf.github.io/GraphvizOnline/) para visualizar a árvore.

## R
Segue os resultados de cada um dos modelos. 
##### **_Em “resultados_arvore” desconsidere os Data “modelo” e “modelo2”, não fazem parte do resultado do modelo_**. 
Segue a imagem de como ficou a árvore criada e a matriz de confusão da árvore de decisão. 






#### [Katharine Pires](https://www.linkedin.com/in/katharine-pires-53b849155/)
