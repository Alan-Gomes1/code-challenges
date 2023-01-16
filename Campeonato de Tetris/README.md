****Campeonato de Tetris**** 

A sua turma do colégio resolveu organizar um campeonato de tetris. Após discussão sobre as regras, ﬁcou deﬁnido que cada aluno jogaria um total de 12 partidas. Das 12 pontuações obtidas por um aluno, a maior e a menor são descartadas, e as demais são somadas, resultando na pontuação ﬁnal do aluno. <br>
****Tarefa**** <br>
Como você possui conhecimentos de programação, acabou sendo designado pela turma para escrever um programa para imprimir a classiﬁcação ﬁnal do campeonato, a partir das pontuações de cada jogador. <br>
****Entrada**** <br>
A entrada é composta de vários conjuntos de teste. A primeira linha de um conjunto de testes contém um número inteiro J, que indica o número de jogadores que participaram do campeonato. A seguir, para cada jogador há duas linhas na entrada: a primeira possui o nome do jogador (formado apenas por letras, sendo apenas a inicial em maiúscula, e com no máximo 15 letras), e a segunda possui as 12 pontuações que o jogador obteve, separadas por espaço. As pontuações são inteiros entre 0 e 1000. O ﬁnal da entrada é indicado por um conjunto de teste com J = 0. <br>
****Saída**** <br>
Para cada conjunto de teste, o seu programa deve escrever uma linha contendo o identiﬁcador do conjunto de teste, no formato “Teste n”, onde n é numerado seqüencialmente a partir de 1. A seguir, o seu programa deve escrever a classiﬁcação ﬁnal no campeonato, utilizando uma linha para cada participante. Cada linha deve conter três informações, separadas por um espaço em branco: a classiﬁcação do jogador, a sua pontuação ﬁnal, e o seu nome. A classiﬁcação de um jogador é igual a 1 mais o número de jogadores que obtiveram pontuação maior do que a sua. Em caso de empate, os jogadores devem ser ordenados em ordem alfabética. Depois de toda a classiﬁcação, deve ser deixada uma linha em branco. O formato do exemplo de saída abaixo deve ser seguido rigorosamente. <br>
****Exemplo**** <br>

**Entrada:** <br>
4 <br>
Zezinho <br>
100 123 133 333 400 300 129 200 360 340 200 600 <br>
Luizinho <br>
60 50 120 250 170 190 190 220 260 270 290 300 <br>
Carlinhos <br>
10 10 20 10 10 10 10 20 20 20 20 20 <br>
Joaozinho <br>
200 300 400 400 500 500 500 600 650 650 700 810 <br>
3 <br>
Pedrinho <br>
100 100 200 200 300 300 400 400 500 500 600 600 <br>
Huguinho <br>
50 100 200 200 300 300 500 500 400 400 600 700 <br>
Zezinho <br>
100 100 100 100 100 100 100 100 100 100 100 100 <br>
0 <br>

**Saída:** <br>
Teste 1 <br>
1 5200 Joaozinho <br>
2 2518 Zezinho <br>
3 2020 Luizinho <br>
4 150 Carlinhos <br>

Teste 2 <br>
1 3500 Huguinho <br>
1 3500 Pedrinho <br>
3 1000 Zezinho <br>

****Restrições**** <br>
0 <= J <= 1000 (J = 0 apenas para indicar ﬁnal da entrada) <br>
0 <= pontuação em uma partida <= 1000 <br>
1 <= tamanho dos nomes, em número de letras <= 15