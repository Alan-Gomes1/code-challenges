Sudoku
Mostrar detalhes

O jogo de Sudoku espalhou-se rapidamente por todo o mundo, tornando-se hoje o passatempo mais popular em todo o planeta. Muitas pessoas, entretanto, preenchem a matriz de forma incorreta, desrespeitando as restrições do jogo. Sua tarefa neste problema é escrever um programa que verifica se uma matriz preenchida é ou não uma solução para o problema.

A matriz do jogo é uma matriz de inteiros 9 x 9. Para ser uma solução do problema, cada linha e coluna deve conter todos os números de 1 a 9. Além disso, se dividirmos a matriz em 9 regiões 3 x 3, cada uma destas regiões também deve conter os números de 1 a 9. O exemplo abaixo mostra uma matriz que é uma solução do problema.

Entrada

São dadas várias instâncias. O primeiro dado é o número n > 0 de matrizes na entrada. Nas linhas seguintes são dadas as n matrizes. Cada matriz é dada em 9 linhas, em que cada linha contém 9 números inteiros.

1 3 2 | 5 7 9 | 4 6 8 <br>
4 9 8 | 2 6 1 | 3 7 5 <br>
7 5 6 | 3 8 4 | 2 1 9 <br>
------+-------+------ <br>
6 4 3 | 1 5 8 | 7 9 2 <br>
5 2 1 | 7 9 3 | 8 4 6 <br>
9 8 7 | 4 2 6 | 5 3 1 <br>
------+-------+------ <br>
2 1 4 | 9 3 5 | 6 8 7 <br>
3 6 5 | 8 1 7 | 9 2 4 <br>
8 7 9 | 6 4 2 | 1 5 3 <br>


Saída

Para cada instância seu programa deverá imprimir uma linha dizendo Instancia k, onde k é o número da instância atual. Na segunda linha, seu programa deverá imprimir SIM se a matriz for a solução de um problema de Sudoku, e NAO caso contrário. Imprima uma linha em branco após cada instância.

Exemplo

Entrada:
2<br>
1 3 2 5 7 9 4 6 8 <br>
4 9 8 2 6 1 3 7 5 <br>
7 5 6 3 8 4 2 1 9 <br>
6 4 3 1 5 8 7 9 2 <br>
5 2 1 7 9 3 8 4 6 <br>
9 8 7 4 2 6 5 3 1 <br>
2 1 4 9 3 5 6 8 7 <br>
3 6 5 8 1 7 9 2 4 <br>
8 7 9 6 4 2 1 5 3 <br>
1 3 2 5 7 9 4 6 8 <br>
4 9 8 2 6 1 3 7 5 <br>
7 5 6 3 8 4 2 1 9 <br>
6 4 3 1 5 8 7 9 2 <br>
5 2 1 7 9 3 8 4 6 <br>
9 8 7 4 2 6 5 3 1 <br>
2 1 4 9 3 5 6 8 7 <br>
3 6 5 8 1 7 9 2 4 <br>
8 7 9 6 4 2 1 3 5 <br>

Saída: <br>
Instancia 1 <br>
SIM <br>

Instancia 2 <br>
NAO

