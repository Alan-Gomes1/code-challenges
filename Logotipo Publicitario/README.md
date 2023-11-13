# Logotipo Publicitário

A Vovó está preocupada com seu netinho que passa o dia inteiro assistindo televisão, pois ela percebeu que durante o desenho animado, aparece um logotipo publicitário na tela e ela não está muito contente com isso.

O netinho e a Vovó gravaram em seu videocassete alguns programas e agora desejam contar quantas vezes o logotipo aparece durante o desenho animado para decidir se reclamam com a emissora por propaganda abusiva.

A Vovó não quer assistir ao vídeo mais uma vez para fazer a contagem e tão pouco deseja que seu netinho o faça. Por isso ela contratou você para descobrir quantas vezes o logotipo aparece em cada vídeo gravado.

Tarefa

Dada uma matriz representando o logotipo que a Vovó deseja contar, e dadas K matrizes, cada uma representando uma imagem do vídeo gravado, seu programa deve contar quantas vezes a matriz do logotipo aparece na sequência de K matrizes. A matriz do logotipo é sempre de dimensões menores que as K matrizes do vídeo.

Entrada

A entrada possui vários casos de teste. Cada caso de teste inicia com a descrição da matriz que representa o logotipo, seguida de K matrizes, cada uma representando uma das imagens do vídeo que a Vovó gravou.

A primeira linha contém dois inteiros X e Y representando respectivamente o número de linhas e colunas da matriz do logotipo (1 <= X <= 10 e 1 <= Y <= 10). As X linhas seguintes da entrada contém cada uma Y inteiros, descrevendo o valor de cada ponto da matriz do logotipo.

Após a descricão do logotipo, são descritas as matrizes que representam as diversas imagens do vídeo gravado. A primeira linha da descrição possui três inteiros K, M e N. Onde K representa o número de matrizes de dimensão M * N que serão lidas ( 1 <= K <= 300, 1 <= M <= 320, 1 <= N  <= 240). Cada pixel é um número pi com 0 <= pi <= 255.

O final da entrada é indicado por X = Y = 0.

Saída

Para cada caso de teste, o seu programa deve produzir um número na saída. A primeira linha da saída deve conter um identificador do conjunto de teste, no formato “Logotipo n”, onde n é numerado sequencialmente a partir de 1. A seguir deve aparecer um número representando quantas vezes o logotipo aparece no vídeo gravado. Após o número deixe uma linha em branco.

Exemplo

Entrada: <br>
2 2 <br>
1 1 <br>
2 3 <br>
3 5 5 <br>
0 0 0 2 3 <br> 
0 1 1 0 0 <br>
1 3 3 0 1 <br>
3 0 0 0 2 <br>
0 0 0 1 1 <br>
0 3 0 0 0 <br>
0 0 0 1 1 <br>
0 9 0 2 3 <br>
2 3 0 0 0 <br>
1 1 8 0 0 <br>
0 1 1 1 0 <br>
0 1 0 1 0 <br>
0 1 0 1 1 <br>
0 1 0 1 3 <br>
0 1 1 1 0 <br>
1 2 <br>
9 9 <br>
2 4 4 <br>
2 9 9 2 <br>
3 3 3 8 <br>
8 7 9 9 <br>
9 9 2 9 <br>
2 6 1 3 <br>
9 2 8 9 <br>
0 3 4 0 <br>
0 0 9 9 <br>
0 0 <br>

Saída: <br>
Logotipo 1 <br>
1 <br>

Logotipo 2 <br>
4