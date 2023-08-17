# **[Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)**

Você recebe uma matriz de inteiros `nums` que consiste em `n` elementos e um inteiro `k`.

Encontre um subarray contíguo cujo **comprimento seja igual ao** `k` que tenha o valor médio máximo e retorne *esse valor* . Qualquer resposta com erro de cálculo menor que será aceita. `10-5`

**Exemplo 1:**

```
Entrada: nums = [1,12,-5,-6,50,3], k = 4
Saída: 12,75000
Explicação: A média máxima é (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12,75
```

**Exemplo 2:**

```
Entrada: nums = [5], k = 1
Saída: 5,00000
```

**Restrições:**

- `n == nums.length`
- `1 <= k <= n <= 105`
- `104 <= nums[i] <= 104`