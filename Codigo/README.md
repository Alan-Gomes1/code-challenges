# Código (OBI 2015)

Gabriel inventou um código para representar números naturais, usando uma sequência de zeros e uns. Funciona assim, o número natural é representado pela quantidade de vezes que o padrão "100" aparece na sequência. <br>

Por exemplo, na sequência 11101001010011110, o padrão aparece duas vezes e na sequência 11101010111110111010101 ele não aparece nenhuma vez. Você deve ajudar Gabriel implementar um programa que, dada a sequência de zeros e uns, calcule quantas vezes o padrão "100" aparece nela.<br>

### Entrada <br>

A primeira linha da entrada contém um inteiro N*N*, o tamanho da sequência. A segunda linha contém a sequência de N*N* zeros e uns, separados por espaço em branco. <br>

### Saída <br>

Seu programa deve imprimir um inteiro, quantas vezes o padrão "100" aparece na sequência. <br>

### Restrições <br>

- 1 ≤ *N* ≤ $10^4$ <br>
| Entrada | Saída |
|---------|-------|
| 17<br>1 1 1 0 1 0 0 1 0 1 0 0 1 1 1 1 0 | 2 |
| 8<br>1 1 1 1 0 1 1 1 | 0 |
| 3<br>1 0 0 | 1 |
| 3<br>0 1 0 | 0 |