# [Fruits into Basket](https://leetcode.com/problems/fruit-into-baskets/)

Você está visitando uma fazenda que possui uma única fileira de árvores frutíferas dispostas da esquerda para a direita. As árvores são representadas por um array inteiro `fruits` onde `fruits[i]` é o **tipo** de fruta que a árvore produz.

Você quer coletar o máximo de frutas possível. No entanto, o proprietário tem algumas regras rígidas que você deve seguir:

- Você só tem **duas** cestas e cada cesta pode conter apenas um tipo de fruta. Não há limite para a quantidade de frutas que cada cesta pode conter.
- Começando em qualquer árvore de sua escolha, você deve colher **exatamente uma fruta**
    
    de cada árvore (incluindo a árvore inicial) enquanto se move para a direita. As frutas colhidas devem caber em uma de suas cestas.
    
- Ao chegar a uma árvore com frutas que não cabem em suas cestas, você deve parar.

Dada a matriz de inteiros `fruits`, retorne *o número **máximo** de frutas que você pode colher* .

**Exemplo 1:**

```
Entrada: frutas = [1,2,1 ]
Saída: 3
Explicação: Podemos colher de todas as 3 árvores.

```

**Exemplo 2:**

```
Entrada: frutas = [0,1,2,2 ]
Saída: 3
Explicação: Podemos colher das árvores [1,2,2].
Se tivéssemos começado na primeira árvore, escolheríamos apenas entre as árvores [0,1].
```

**Exemplo 3:**

```
Entrada: frutas = [1,2,3,2,2 ]
Saída: 4
Explicação: Podemos colher das árvores [2,3,2,2].
Se tivéssemos começado na primeira árvore, só escolheríamos entre as árvores [1,2].
```

**Restrições:**

- `1 <= fruits.length <= 105`
- `0 <= fruits[i] < fruits.length`