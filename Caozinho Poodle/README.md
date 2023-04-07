# **Cãozinho Poodle**

Maria vive perdendo coisas dentro de casa. Desde pequena, tudo em que ela põe a mão desaparece. Isso acontece porque ela é muito desorganizada, deixa tudo espalhado pela casa, tornando humanamente impossível localizar algum objeto no meio de tanta confusão. Ela sempre contou com a ajuda infalível de seu cãozinho Poodle, que consegue localizar seus objetos perdidos. Uma vez ela queria me mostrar a eficiência do seu Poodle. Escondeu propositalmente uma bola em um dos quartos, e gritou: “Pooooooodle!”. Então ela disse “Bola” e ele partiu para buscá-la. Ela ficou preocupada porque depois de 30 segundos ele ainda não tinha retornado com a bola. A surpresa foi que logo depois ele apareceu, triufante, carregando 4 bolas!!! A que Maria acabara de esconder e outras 3 de seus filhos, que ela nem se lembrava que existiam, e muito menos onde estavam!
Atualmente Maria faz pós-graduação em Computação. Seu projeto final é uma ferramenta de busca. Em homenagem a seu cãozinho que sempre buscou suas coisas, ela batizou seu projeto de Poodle. A ideia é simples: dada uma palavra, Poodle faz uma busca no disco e retorna todos os documentos que contém a dada palavra. Como no caso real da bola que comentei acima, na maioria das vezes a busca retorna bem mais resultados que o esperado. Os resultados são então exibidos agrupados em páginas. Por exemplo, se a ferramenta for configurada para exibir 10 resultados por página, e a busca retornar 143 resultados, eles serão exibidos em 15 páginas: 14 delas com 10 em cada uma, e a última com os 3 restantes. <br>
A ferramenta já está pronta, e funciona muito bem. Mas Maria teve a feliz ideia de enfeitar o trabalho na tentativa de ganhar mais pontos... ao exibir o resultado de uma busca, Poodle mostra um logotipo com o nome da ferramenta, sendo que os o's de Poodle podem ser dois ou mais, dependendo da quantidade de páginas de resultado. A ideia é que “Poodle” seja escrito com tantas letras quantas forem as páginas de resultado, repetindo o's quando necessário. No exemplo acima, o logotipo seria “Pooooooooooodle”, que contém 15 letras. <br>
Naturalmente, se a quantidade de páginas de resultados for inferior a 6, a palavra Poodle não será cortada, o logotipo será Poodle. E, para evitar que o logotipo fique tão grande que nem caiba na tela de resultados, ele será limitado a um máximo de 20 letras, mesmo que a quantidade de páginas de resultado seja superior a 20.
Sua tarefa é ajudar Maria a montar o logotipo. <br>
****

****Entrada**** <br>
Há vários casos de teste.
Cada caso de teste é uma linha contendo dois números inteiros, N e P, sendo N o número de documentos encontrados pelo Poodle, e P o número de resultados exibidos por página (1 ≤ N ≤ 1.000.000, 1 ≤ P ≤ 100). A entrada termina quando N = P = 0. <br>
****

**Saída** <br>
Para cada caso de teste da entrada seu programa deve produzir uma linha na saída contendo a palavra Poodle, ajustando a quantidade de o's de acordo com as regras descritas no enunciado. <br>
****

**Exemplos** <br>

**Entrada:** <br>
20 4 <br>
143 10 <br>
42 5 <br>
80  <br>
0 0 <br>

**Saída:** <br>
Poodle <br>
Pooooooooooodle <br>
Pooooodle <br>
Poooooooooooooooodle