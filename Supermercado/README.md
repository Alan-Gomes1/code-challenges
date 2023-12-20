# Supermercado

A rede de supermercados BemBom, da cidade de Planalto, decidiu reformular o armazenamento de seus estoques. No sistema atual, cada uma das lojas da rede possui espaço para armazenar um pequeno estoque, sendo freqüentemente necessário transportar mercadorias de uma loja para outra. Para racionalizar o transporte e aumentar a capacidade de estoque, a direção da rede Bem-Bom decidiu instalar um depósito central. De forma a diminuir os custos com transporte, ﬁcou deﬁnido que o novo depósito deve ser localizado em um quarteirão que minimize a soma das distâncias dele até todas as lojas da rede.

Por ser uma cidade planejada, Planalto possui uma característica muito peculiar. Todas as suas ruas são orientadas na direção leste-oeste ou norte-sul, e todos os quarteirões são do mesmo tamanho. Veja uma parte do mapa de Planalto na ﬁgura abaixo. Os quarteirões em Planalto são identiﬁcados pelo número de quadras, em cada direção, que os separam da localização da prefeitura (0,0). Localizações a leste e a norte da prefeitura são identiﬁcadas por coordenadas positivas, e localizações a oeste e a sul por coordenadas negativas.

Parte do mapa de Planalto
[](https://congenial.com.br/img-problem/supermercado.jpg)

Tarefa

A sua tarefa é, dadas as coordenadas dos quarteirões onde estão localizados todos os supermercados da rede, determinar o quarteirão onde deve ser instalado o novo depósito. A localização deste depósito deve ser tal que a soma das distâncias entre o depósito e as lojas, em número de quarteirões em ambas as direções, seja a menor possível. A distância entre dois quarteirões é dada pela distância entre eles na direção leste-oeste mais a distância na direção norte-sul. Por exemplo, a distância entre os quarteirões (2,-1) e (4, 3) é 2 + 4 = 6.

Entrada

A entrada é composta de vários conjuntos de teste. A primeira linha de cada conjunto de teste contém um número inteiro S que é o número de supermercados da rede. A seguir, são dadas S linhas, cada uma contendo dois números inteiros X e Y, representando as coordenadas do quarteirão onde se situa um dos supermercados. X representa a coordenada na direção leste-oeste e Y represetna a coordenada na direção norte-sul. O ﬁnal da entrada é dado por um conjunto de teste com S = 0.

Saída

Para cada conjunto de teste, o seu programa deve escrever três linhas na saída. A primeira linha deve conter um identiﬁcador do conjunto de teste, no formato “Teste n”, onde n é numerado sequencialmente a partir de 1. A segunda linha deve conter as coordenadas X e Y do quarteirão onde deve ser instalado o novo depósito, separadas por um espaço em branco. Se mais de um quarteirão puder ser escolhido como localização do depósito, seu programa pode imprimir qualquer um deles. A terceira linha deve ser deixada em branco. O formato do exemplo de saída abaixo deve ser seguido rigorosamente.

Exemplo

Entrada: <br>
4 <br>
1 2 <br>
-3 -3 <br>
4 -1 <br>
-5 0 <br>
5 <br>
1 3 <br>
7 13 <br>
25 13 <br>
15 14 <br>
25 1 <br>
0

Saída: <br>
Teste 1
1 0

Teste 2
15 13


Restrições

0 <= S <= 1000 (S = 0 apenas para indicar o ﬁnal da entrada)
-1000 <= X <= 1000
-1000 <= Y <= 1000