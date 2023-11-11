# Batalha de Yavin

A Batalha de Yavin, a maior batalha da Guerra Civil Galáctica, resultou na destruição da primeira Estrela da Morte. Os dois lados do confronto foram o Império Galáctico e a Aliança Rebelde. A Estrela da Morte chegou no sistema escoltada por uma frota constituída por diversas naves, dentre elas, as velozes Tie Fighters.

O Comando Rebelde estava desacreditado. Com quase todos os pilotos destruídos, o destino da batalha estava nas mãos de um jovem piloto, mas este trazia consigo uma nova esperança, afinal, esse jovem era Luke Skywalker. Ele sabia que poderia usar a dobra espacial e o poder da força para se teletransportar com sua nave muito mais rápido de um lugar para outro no espaço e, assim, conseguir destruir o máximo possível de naves inimigas.

Dadas as coordenadas de cada nave inimiga e de cada teleporte de Luke, diga quantas naves ele consegue destruir. Para cada coordenada onde Luke teleporta, ele dá apenas um tiro de Prótons que é capaz de destruir a primeira nave que esteja em sua frente. No exemplo ao lado, ao teleportar para a posição marcada como (2), ele atira e destrói somente a nave que está em sua frente. Já ao teleportar para a posição (3), ele atira mas não acerta nenhuma nave.

Entrada

A primeira linha da entrada possui um inteiro ‘N’ (3 ≤ N ≤ 100), indicando que a matriz que representa o espaço possui dimensões NxN, e um inteiro ‘M’ (1 ≤ M ≤ 1000), indicando o número de teleportes realizados por Luke. As próximas ‘N’ linhas possuem ‘N’ inteiros em cada uma, cujos valores podem ser 0 (se não existe nave naquele quadrante) ou 1 (se existe uma nave naquele quadrante). Nas próximas ‘M’ linhas serão dadas as coordenadas inteiras (L – linha C - coluna) de cada teleporte de Luke, um por linha. É garantido que Luke não aparecerá numa coordenada que possui uma nave, já que dois corpos não podem ocupar o mesmo lugar no espaço ao mesmo tempo. Os teleportes ocorrerão somente dentro do espaço dado.

Saída

A saída consiste de apenas um inteiro que é o número de naves destruídas por Luke. <br>

|Entrada 	      | Saída |
| ----------------| ------|
|8 3              | 2     |
|0 0 0 0 0 0 0 1  |       |
|1 0 0 1 0 1 0 0  |       |
|0 0 0 0 0 1 0 0  |       |
|0 0 0 1 0 0 0 0  |       |
|0 0 0 0 0 0 1 0  |       |
|0 0 1 0 0 1 0 0  |       |
|0 1 0 0 0 0 0 0  |       |
|0 0 0 0 0 0 0 0  |       |
|7 2              |       |
|3 5              |       |
|3 1              |       |
|                 |       |
|4 2              | 2     |
|0 1 0 1          |       |
|0 1 1 0          |       |
|1 0 0 0          |       |
|0 0 0 1          |       |
|3 2              |       |
|3 1              |       |
  