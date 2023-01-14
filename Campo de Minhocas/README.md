# ****Campo de Minhocas****

Minhocas são muito importantes para a agricultura e como insumo para produção de ração animal. A Organização para Bioengenharia de Minhocas (OBM) é uma entidade não governamental que promove o aumento da produção, utilização e exportação de minhocas.
Uma das atividades promovidas pela OBM é a manutenção de uma fazenda experimental para pesquisa de novas tecnologias de criação de minhocas. Na fazenda, a área destinada às pesquisas é de formato retangular, dividida em células quadrangulares de mesmo tamanho. As células são utilizadas para testar os efeitos, na produção de minhocas, de variações de espécies de minhocas, tipos de terra, de adubo, de tratamento, etc. Os pesquisadores da OBM mantêm um acompanhamento constante do desenvolvimento das minhocas em cada célula, e têm uma estimativa extremamente precisa da produtividade em cada uma das células. A figura abaixo mostra um mapa da fazenda, mostrando a produtividade estimada de cada uma das células.<br>

![https://congenial.com.br/wp-content/uploads/2021/08/minhoca.png](https://congenial.com.br/wp-content/uploads/2021/08/minhoca.png)<br>

Um pesquisador da OBM inventou e construiu uma máquina colhedeira de minhocas, e quer testá- la na fazenda. A máquina tem a largura de uma célula, e em uma passada pelo terreno de uma célula colhe todas as minhocas dessa célula, separando-as, limpando-as e empacotando-as. Ou seja, a máquina eliminara uma das etapas mais intensivas de mão de obra no processo de produção de minhocas. A máquina, porém, ainda está em desenvolvimento e tem uma restrição: não faz curvas, podendo movimentar-se somente em linha reta.
Decidiu-se então que seria efetuado um teste com a máquina, de forma a colher o maior número possível de minhocas em uma unica passada, em linha reta, de lado a lado do campo de minhocas. Ou seja, a máquina deve colher todas as minhocas de uma ‘coluna’ ou de uma ‘linha’ de células do campo de minhocas (a linha ou coluna cuja soma das produtividades esperadas das células é a maior possível).<br>
****

****Tarefa****<br>
Escreva um programa que, fornecido o mapa do campo de minhocas, descrevendo a produtividade estimada em cada célula, calcule o número esperado total de minhocas a serem colhidas pela máquina durante o teste, conforme descrito acima.<br>
********

****Entrada****<br>
A primeira linha da entrada contém dois números inteiros N e M, representando respectivamente o número de linhas (1 <= N <= 100) e o número de colunas (1 <= M <= 100) de células existentes no campo experimental de minhocas. Cada uma das N linhas seguintes contém M inteiros, representando as produtividades estimadas das células correspondentes a uma linha do campo de minhocas.<br>
********

****Saída****<br>
A saída deve ser composta por uma unica linha contendo um inteiro, indicando o número esperado total de minhocas a serem colhidas pela máquina durante o teste.<br>
****Exemplo****<br>

**Entrada:**<br>
4 1<br>
100<br>
110<br>
0<br>
100<br>

**Saída:**<br>
310<br>

**Entrada:**<br>
3 4<br>
81 28 240 10<br>
40 10 100 240<br>
20 180 110 35<br>

**Saída:**<br>
450<br>

****Restrições****<br>
1 <= N <= 1001 <= M <= 1000 <= *Produtividade de uma célula* <= 5000 <= *Produtividade de uma linha ou coluna de células* <= 50000