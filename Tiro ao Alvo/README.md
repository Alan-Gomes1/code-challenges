# ****Tiro ao Alvo****

Recentemente Juquinha ganhou de aniversário um joguinho bem clássico: Tiro ao Alvo. Ele arrumou um ótimo lugar em seu quarto para se divertir com o jogo, porém após ler todas as regras do jogo ele percebeu que precisa da sua ajuda para calcular a pontuação obtida.
Segundo as regras, o alvo do jogo é composto por *C* círculos, todos centrados na origem (0,0). Juquinha atira *T* vezes e após cada tiro informa suas coordenadas. A pontuação de cada tiro é feita da seguinte forma: para cada círculo em que o tiro estiver contido Juquinha recebe um ponto.
Considere por exemplo a figura abaixo. O tiro marcado com a letra A recebe zero pontos, pois não está contido por nenhum círculo. O tiro marcado com a letra B recebe um ponto, pois está contido por um círculo (o mais externo). O tiro marcado com a letra C recebe dois pontos, pois está contido por dois círculos (note que este caso mostra que tiros exatamente na borda de um círculo são considerados como contidos pelo círculo). Já o tiro marcado com a letra D recebe três pontos, pois está contido pelos três círculos. Considerando todos os pontos, a pontuação total de Juquinha é de 13 pontos. <br>

![https://congenial.com.br/wp-content/uploads/2021/08/tiro.jpg](https://congenial.com.br/wp-content/uploads/2021/08/tiro.jpg)

Dados os raios de *C* círculos centrados na origem e as coordenadas dos *T* tiros realizados por Juquinha, escreva um programa que calcula o total de pontos que Juquinha obteve. <br>
********

****Entrada**** <br>
A primeira linha da entrada contém dois inteiros positivos, *C* e *T*, que representam, respectivamente, o número de círculos do alvo e o número de tiros.
Cada uma das *C* linhas seguintes contém um inteiro positivo. O *i*-ésimo inteiro *Ri* representa o raio do *i*-ésimo círculo. Os raios *Ri* são fornecidos em ordem crescente.
Cada uma das *T* linhas seguintes contém um par *X*, *Y* de inteiros, que representam as coordenadas de cada tiro. <br>
********

****Saída**** <br>
Seu programa deve imprimir uma única linha, contendo apenas um inteiro, o total de pontos obtidos por Juquinha. <br>
********

****Restrições**** <br>
• 1 ≤ C ≤ 105 <br>
• 1 ≤ *Ri* ≤ 106 para 1 ≤ *i* ≤ *C* <br>
• *Ri* > *Ri*-1 para 2 ≤ *i* ≤ *C* <br>
• 1 ≤ *T* ≤ 105 <br>
• -105 ≤ *X*, *Y* ≤ 105 <br>

****Exemplos**** <br>

**Entrada** <br>
3 10 <br>
1 <br>
2 <br>
5 <br>
0 0 <br>
-2 0 <br>
0 -2 <br>
3 -4 <br>
-4 -3 <br>
3 1 <br>
6 2 <br>
-1 2 <br>
-5 -2 <br>
1 -1 <br>

**Saída** <br>
13 <br>

**Entrada** <br>
3 6 <br>
1 <br>
2 <br>
5 <br>
1 0 <br>
0 3 <br>
-5 0 <br>
0 0 <br>
-3 -3 <br>
1 1 <br>

**Saída** <br>
11