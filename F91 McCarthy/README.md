# F91 de McCarthy

McCarthy é um teórico famoso de ciência da computação. No seu trabalho, ele definiu uma função recursiva, chamada f91, que recebe como entrada um inteiro N e retorna um inteiro positivo definido como a seguir:

    Se N ≤ 100, então f91 (N) = f91 (f91 (N + 11));
    Se N ≥ 101, então f91 (N) = N - 10.

Escreva um programa que computa a função f91 de McCarthy.

Entrada

O arquivo de entrada consiste de uma série de inteiros positivos, cada inteiro é no máximo 1.000.000. Há no máximo 250.000 casos de teste. Cada linha possui somente um número. O fim da entrada é alcançada quando o número 0 é encontrado. O número 0 não deve ser considerado como parte do conjunto de teste.

Saída <br>

O programa deve imprimir cada resultado em uma linha, seguindo o formato fornecido no exemplo de saída.

Exemplo

Entrada: <br>
500 <br>
91 <br>
0

Saída: <br>
f91(500) = 490 <br>
f91(91) = 91
