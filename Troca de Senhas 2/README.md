# Troca de senhas 2

João e Maria estão sempre contando segredos um ao outro. Para tanto, eles precisam compartilhar uma senha comum, que é usada para criptografar uma mensagem ou decifrar uma mensagem codificada recebida. O protocolo de criptografia exige que a senha seja modificada periodicamente, o que requer passar a senha de um para o outro. No passado, eles haviam estabelecido um protocolo para que a troca de senha pudesse ser feita de forma segura, mesmo passando o valor da senha na mensagem sem usar criptografia. Maria, no entanto, resolveu melhorar o protocolo, tornando-o mais robusto. Ela combinou a seguinte estratégia com João:

• A senha é passada numa matriz quadrada de dimensão n × n, contendo valores inteiros positivos.

• Deve-se eliminar todos os valores n²-1 valores da matriz por etapas. A cada eliminação, a matriz reduz uma linha e uma coluna.

• Numa dada etapa de eliminação de valores, a linha a ser eliminada é dada pelo resto da divisão da soma dos valores contidos na diagonal da matriz pelo número de linhas.

• De forma semelhante, a coluna a ser eliminada é dada pela soma dos valores contidos na diagonal secundária pelo número de colunas.

• O valor restante na matriz resultante após todas as eliminações é o valor da senha. Ajude João e Maria fornecendo um programa para que a senha seja seguramente transmitida. Seu programa deve usar uma função que recebe a matriz M e retorna a senha.

Entrada

Uma matriz com n linhas e n colunas, contendo valores inteiros positivos (2 ≤ n ≤ 1000). Cada valor contido na matriz não é maior que 1000.

Saída

A saída é um inteiro positivo, presente na matriz original.
|Entrada 	   | Saída |
---------------|-------|
|1 2 3         | 9     |
|4 5 6         |       |       
|7 8 9         |       |
|              |       |
|27 32 12      | 45    |
|45 83 100     |       |
|207 15 213    |       |
|              |       |
|41 170 961 245| 82    |
|117 16 23 229 |       |
|91 82 997 655 |       |
|346 298 98 111|       |