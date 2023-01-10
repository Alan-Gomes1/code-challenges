# Eu Posso Adivinhar a Estrutura de Dados!
Existe uma estrutura de dados do tipo sacola, suportando duas operações:

1x Jogue um elemento x na sacola.

2 Tire um elemento da sacola.

Dada uma sequencia de operações que retornam valores, você vai adivinhar a estrutura de dados. É uma pilha (último-dentro, primeiro-fora), uma fila (primeiro-dentro, primeiro-fora), uma fila de prioridade (sempre tire os elementos grandes por primeiro) ou qualquer outra coisa que você dificilmente consegue imaginar!

## **Entrada**

Existem muitos casos de testes. Cada caso de teste começa com a linha contando um único inteiro **n** (1 <= **n** <= 1000). Cada uma das seguintes **n** linhas é um comando do tipo 1, ou um número inteiro 2, seguido de um número inteiro **x**. Isso significa que depois de executar um comando do tipo 2, obtemos um elemento **x** *sem erros*. O valor de **x** é sempre um número inteiro, positivo e não maior do que 100. O final da entrada é determinado pelo final do arquivo (EOF). O tamanho do arquivo de entrada não excede 1MB.

## **Saída**

Para cada caso de teste, mostre um dos seguintes:

stack

É definitivamente uma pilha.

queue

É definitivamente uma fila.

priority queue

É definitivamente uma fila de prioridade.

impossible

Não pode ser uma pilha, uma fila ou uma fila de prioridade.

not sure

Pode ser mais de uma das três estruturas mencionadas acima.

| Entrada | Saída |
| --- | --- |
| 6
1 1
1 2
1 3
2 1
2 2
2 3
6
1 1
1 2
1 3
2 3
2 2
2 1
2
1 1
2 2
4
1 2
1 1
2 1
2 2
7
1 2
1 5
1 1
1 3
2 5
1 4
2 4 | queue
not sure
impossible
stack
priority queue |