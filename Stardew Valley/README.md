# Stardew Valley: Desafio da colheita

Você está participando do desafio da colheita do Stardew Valley, e deseja organizar sua lojinha com os itens colhidos. Você possui um terreno de M x N (M linhas e N colunas), onde cada célula representa uma plantação. Cada célula pode ter um valor entre 0 e 9, que representa a quantidade de frutas/vegetais colhidos naquele local.

Sua tarefa é: Calcular a soma de todos os valores de uma linha específica L ou de uma coluna específica C. Por exemplo, se o jogador deseja calcular a soma dos valores da linha 3, ele deve somar todos os valores da terceira linha.

Entrada <br>
A primeira linha deve conter dois números inteiros M e N separados por espaço, representando o número de linhas e colunas do terreno de cultivo, respectivamente. As próximas M linhas contém N inteiros V, separados por espaço, representando os valores de cada célula do terreno de cultivo. A última linha contém um caractere que pode ser "L" ou "C", seguido por um número inteiro X, representando a linha ou coluna que o jogador deseja calcular a soma. Saiba que 1 <= M, N <= 100, 0 <= V <= 9 e 1 <= X <= M, N.

Saída <br>
A saída deve conter um único número inteiro, que representa a soma dos valores da linha L ou coluna C, conforme especificado na entrada.
| Entrada 	| Saída  |
| ----------| -------|
| 3 3       | 9      |
| 2 4 6     |        |
| 1 3 5     |        |
| 7 8 9     |        |
| L 2       |        |
|           |        |
| 2 5       | 11     |
| 2 4 6 3 5 |        |
| 1 3 5 7 2 |        |
| C 3       |        |
  