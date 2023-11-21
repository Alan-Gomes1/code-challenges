# Dominó

Jogar dominó em Salvador é algo tão ou mais famoso do que ir atrás do trio no Carnaval. O pessoal aposta alto nesse jogo, tem muita gente que aposta o próprio abadá, para vocês verem a paixão do soteropolitano por esse jogo. Como ninguém quer ser passado para trás, constantemente eles estão contando e verificando as peças já em jogo, até mesmo para calcular melhor as probabilidades. Como você é jogador fanático desse jogo também, terá que verificar quantas peças já estão em jogo.

Entrada

Será dada uma matriz de inteiros de tamanho 7x7, onde as posições na matriz podem ter os valores 0 ou 1. Sendo 1, significa que aquela peça identificada pela coordenada (x ; y) está em jogo, ou seja, se na coordenada (1 ; 2) tivermos o valor 1, então a peça 1|2 do dominó está em campo, que é a mesma peça 2|1 na coordenada (2 ; 1). Note, portanto, que para as peças com valores iguais dos dois lados, teremos uma única representação na matriz.

Saída

Imprima simplesmente quantas peças do dominó estão em campo. <br>
|Entrada      	| Saída |
| ------------- | ----- |
|0 1 1 0 0 0 1  | 8     |
|1 0 0 0 0 0 1  |       |
|1 0 0 1 0 0 0  |       |
|0 0 1 0 0 1 0  |       |
|0 0 0 0 0 1 0  |       |
|0 0 0 1 1 0 1  |       |
|1 1 0 0 0 1 0  |       |
|               |       |
|0 1 0 0 0 0 1  | 9     |
|1 0 1 0 0 1 0  |       |
|0 1 0 1 1 0 0  |       |
|0 0 1 0 1 0 0  |       |
|0 0 1 1 0 1 0  |       |
|0 1 0 0 1 0 1  |       |
|1 0 0 0 0 1 0  |       |
|               |       |
|0 0 0 0 0 0 0  | 3     |
|0 0 0 1 0 0 0  |       |
|0 0 1 0 1 0 0  |       |
|0 1 0 0 0 0 0  |       |
|0 0 1 0 0 0 0  |       |
|0 0 0 0 0 0 0  |       |
|0 0 0 0 0 0 0  |       |