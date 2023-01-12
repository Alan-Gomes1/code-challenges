# Chuva Acumulada
Bob trabalha no OBM (Órgão Brasileiro de Metereologia), que é a organização responsável pela medição dos índices pluviométricos (quantidade de chuva acumulada) em todo o país. Eles são muito eficientes no que fazem, mas estão com um problema: eles não sabem como proceder para calcular a quantidade acumulada de chuva que caiu em cada região em dois períodos consecutivos, muito embora eles saibam os dados de cada período separadamente.<br>

Como a chefia do Órgão estava muito ocupada, acabou ficando a cargo de Bob, o estagiário, a tarefa de implementar um programa que some, para cada região, a quantidade de chuva acumulada em dois períodos consecutivos.<br>

O mapa que o OBM usa é dividido em N×N regiões, sendo que para cada região, a cada período, é determinado um número inteiro indicando a quantidade de chuva acumulada. A quantidade de chuva acumulada total em cada região em dois períodos consecutivos é a soma das quantidades de chuva em cada um dos períodos.<br>

Mas como Bob é só um estagiário e não está acostumado a fazer nada mais do que tirar cópias de documentos, ele pediu sua ajuda para implementar o programa que calcula a quantidade de chuva acumulada total nos dois períodos para cada uma das regiões, dadas as quantidades de chuva acumulada em cada período para cadaregião.<br>


Entrada<br>
A primeira linha da entrada contém um inteiro N indicando a dimensão dos dois mapas que devem ser lidos. Nas próximas 2N linhas são dados os dois mapas, cada mapa indicando a quantidade de chuva acumulada nas regiões em um período. Cada mapa é descrito em N linhas consecutivas, cada linha contendo N inteiros, sendo que cada inteiro indica a quantidade de chuva acumulada, no período, em uma região.<br>


Saída<br>
A saída deverá conter N linhas, com N inteiros em cada linha, indicando a quantidade de chuva acumulada total em cada uma das regiões nos dois períodos considerados.<br>


Restrições<br>
1 ≤ N ≤ 100.<br>
0 ≤ quantidade de chuva acumulada em cada região de cada mapa ≤ 100.<br>

Exemplos<br>
Entrada<br>
2<br>
1 2<br>
3 4<br>
10 11<br>
12 13<br>

Saída<br>
11 13<br>
15 17<br>

Entrada<br>
3<br>
1 1 1<br>
1 2 2<br>
1 2 3<br>
3 2 1<br>
2 2 1<br>
1 1 1<br>

Saída<br>
4 3 2<br>
3 4 3<br>
2 3 4