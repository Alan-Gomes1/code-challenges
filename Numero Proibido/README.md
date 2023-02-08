# ****Número Proibido****

Os números proibidos são números que possuem alguma representação problemática, por exemplo, número do azar, de algo ruim, e até números que são senhas do governo.
O número proibido mais conhecido é um número primo[1] que foi descoberto em 2001 e representa o arquivo binário da versão compactada do código C que implementa o algoritmo DeCSS, que pode ser utilizado para lograr o sistema de proteção do DVD.
Luan, um rapaz que tem muito receio de ser procurado por agências espiãs internacionais coletou um conjunto de números ilegais e está filtrando esses números de todos os seus arquivos no computador. <br>
Infelizmente, Luan ainda não sabe programar muito bem e pediu a sua ajuda para implementar um programa que receba um conjunto de números ilegais e responda se um outro conjunto de números fazem parte dos números ilegais.
[1]http://en.wikipedia.org/wiki/Illegal_prime <br>
**** 

****Entrada**** <br>
A entrada é composta por um único caso teste que possui diversas linhas. A primeira linha possui um número **N** ( 1 <= **N** <= 140000 ) que representa a quantidade de números proibidos existentes. A segunda linha do caso de teste possui **N** números **Pi** ( 0 <= **Pi** <= 231 ) representando os números proibidos.
Depois existirão diversas linhas contendo um único número que se quer saber se é proibido ou não.
A entrada termina em EOF. <br>
********

****Saída**** <br>
Para cada número da consulta deve-se imprimir uma única linha contendo a palavra **sim** se o número for proibido, ou **nao** caso o número não seja proibido. <br>
****Exemplo**** <br>

**Entrada:** <br>
7 <br>
10 0 50 25 121 0 3000 <br>
1 <br>
2 <br>
3 <br>
10 <br>
0 <br>

**Saída:** <br>
nao <br>
nao <br>
nao <br>
sim <br>
sim