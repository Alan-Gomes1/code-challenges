# Torre de Xadrez

Xadrez é sem dúvida um dos jogos mais famosos e que exige grande capacidade intelectual e estratégica. São várias peças que possuem diferentes tipos de movimentos no tabuleiro. A torre, por exemplo, move-se em uma linha ou em uma coluna, como pode ser observado na figura acima, onde as posições marcadas com um X destacam aquelas onde a torre pode ir. Havendo uma peça inimiga a sua frente, esta peça pode ser derrotada pela torre, é o caso do peão na figura acima. Porém, se houver uma peça aliada a frente, a torre poderá se mover até a posição imediatamente anterior a peça aliada, é o caso do cavalo na figura acima. Sendo assim, você foi escolhido para desenvolver um programa que diz quantas peças inimigas a torre poderá possivelmente derrotar, a partir de uma posição X, Y no tabuleiro que indica onde a torre está. <br>

Entrada <br>

A entrada será primeiramente uma grade de tamanho ‘8 x 8’, representando o tabuleiro de xadrez. Cada uma das ‘8’ linhas do tabuleiro possuirá ‘8’ inteiros ‘Q’ (0 <= Q <= 2), separados por espaço. Portanto, cada posição do tabuleiro possuirá 3 valores possíveis: 0 – para indicar que naquela posição não tem peça; 1 – para indicar uma peça aliada; 2 – para indicar que naquela posição há uma peça inimiga. Por fim, serão dados dois inteiros ‘X’ e ‘Y’ (0 <= X, Y <= 7), representando a coordenada inicial da torre, sendo que ‘X’ representa uma linha e ‘Y’ representa uma coluna. Além disso, na posição X – Y terá o valor 1, pois representa a própria torre. <br>

Saída <br>

Você deverá imprimir a quantidade de peças inimigas no caminho da torre. <br>

|Entrada 	     |Saída      |
-----------------|-----------|
|0 0 0 0 0 0 0 0 |2          |
|0 0 0 0 0 0 0 0 |           |
|2 0 1 1 2 0 0 0 |           |
|0 0 0 0 0 0 0 0 |           |
|0 0 0 0 0 0 0 0 |           |
|0 0 0 0 0 0 0 0 |           |
|0 0 2 0 0 0 0 0 |           |
|0 0 2 0 0 0 0 0 |           |
|2 2             |           |
