# ****João e o Pé de Feijão****

João foi ao mercado vender uma vaca, a pedido de sua mãe. Chegando lá, um estranho lhe propôs trocar a vaca por cinco feijões mágicos e João aceita a oferta. A mãe dele, porém, fica furiosa com isso e joga os feijões pela janela e o coloca de castigo.
Durante a noite, os feijões germinam e se transformam em gigantescos pés de feijão. Quando João acorda, ele escala os pés de feijão e chega numa terra mágica acima das nuvens, habitada por um gigante que se alimenta de seres humanos. Felizmente, para João, o gigante não estava com fome e, em vez de degustá-lo logo de cara, o gigante o prendeu em uma cela até o jantar.
A cela é mantida trancada por um complicado mecanismo. Para destravá-lo, é preciso entrar com uma senha numérica, um processo extremamente tedioso e lento. A esposa do gigante simpatizou com João e lhe forneceu todas as informações que sabe sobre a tranca: a senha que a destrava é um número inteiro menor ou igual a 41001 e esse número é um número de Kaprekar.
Um *número de Kaprekar* é um inteiro positivo cujo quadrado, em sua representação decimal, pode ser dividido em duas partes que individualmente são inteiros positivos e que quando somadas são iguais ao número original. Por exemplo:
• 297 é um número de Kaprekar porque 2972 = 88209 e 88+209=297;
• 999 é um número de Kaprekar porque 9992 = 998001 e 998+001=999;
• 100 **não é** um número de Kaprekar. 1002=10000 pode ser escrito como 100+00=100, mas 00=0 não é um inteiro positivo.
Por definição, 1 é um número de Kaprekar, ainda que ele não atenda ao critério acima. Mais formalmente, um inteiro n é um número de Kaprekar se: <br>
n = q+r <br>
n^2 = q·10m+r <br> 
Para algum m ≥ 1, q ≥ 0 e 0 ≤ r < 10m inteiros, com n ≠ 10a para todo a>=1 inteiro. <br>
Entrar com uma senha errada no mecanismo faz com que ele fique inacessível por 5 minutos. Assim, se João tentar todos os números possíveis, ele muito provavelmente não conseguirá escapar antes da hora do jantar. João desconfia, porém, que apenas poucos valores sejam números de Kaprekar, de forma que seja possível testar todos esses antes do gigante retornar.
Sua tarefa é ajudar João: dado um inteiro, determine se ele é ou não um número de Kaprekar. <br>
****

****Entrada**** <br>
A entrada possui vários casos de teste. Cada caso de teste é dado numa linha que contém um inteiro n (0 < n ≤ 41001). A entrada termina com n=0, que não deve ser processado. <br>
********

****Saída**** <br>
Para cada caso de teste, imprima uma linha na saída no formato N: A, onde N é o número analisado no caso de teste e A é S se n é um número de Kaprekar ou N se ele não for. <br>
****Exemplos**** <br>

**Entrada:** <br>
1 <br>
2 <br>
3 <br>
4 <br>
9 <br>
45 <br>
50 <br>
38962 <br>
0 <br>

**Saída:** <br>
1: S <br>
2: N <br>
3: N <br>
4: N <br>
9: S <br>
45: S <br>
50: N <br>
38962: S