# **Telescópios**

Telescópios são instrumentos que auxiliam a observação do céu, melhorando e aumentando o aspecto das estrelas, planetas e outros objetos brilhantes. Existem diversos tipos de telescópios, sendo os tipos mais comuns os de lentes objetivas (refratores) e os de espelhos (refletores).
A maneira como os telescópios melhoram a nossa percepção dos astros no céu é aumentando a quantidade de luz captada que chega aos nossos olhos. Toda luz que entra pelos nossos olhos entra por um orifício chamado pupila. Tal controla a quantidade de luz que entra nos olhos, aumentando o diâmetro quando o ambiente está escuro (e portanto precisamos obter mais luz para identificar os objetos) e diminuindo quando o ambiente está claro. Num ambiente muito escuro, a pupila pode atingir um diâmetro de 8 mm.
Cada objeto celeste (estrela, planeta, nebulosa, etc) emite uma quantidade de luz (fótons) que é homogeneamente distribuída quando chega na Terra. Por exemplo, a estrela A emite luz que pode ser captada a um fluxo de 40.000 fótons por segundo por milímetro quadrado. Isso é, a cada segundo, é possível captar 40.000 fótons provenientes da estrela A numa área de 1 mm&sup. Ou seja, uma pupila de 10 mm² de área captaria 400.000 fótons provenientes da estrela A por segundo.
Para que nosso cérebro consiga interpretar que existe um objeto ali, porém, ele precisa receber 40.000.000 fótons por segundo. Assim, podemos utilizar um telescópio com lente (ou espelho) de 100 mm² de área, que vai captar a quantidade necessária de fótons provenientes da estrela A e encaminhá-los até nossa pupila, fazendo assim com que nosso cérebro perceba a presença da estrela ali. <br>
****

****Tarefa**** <br>
Dada uma lista com estrelas no céu, o fluxo de fótons que cada uma delas emite, e área de abertura de um telescópio, dizer quantas estrelas serão perceptíveis usando tal telescópio. <br>
****

**Entrada** <br>
A primeira linha da entrada terá um inteiro A (1 ≤ A ≤ 10.000) representando a área de abertura do telescópio (em milímetros quadrados) a ser considerado. A segunda linha possui um inteiro N (1 ≤ N ≤ 10.000) representando o número de estrelas a serem estudadas. As N linhas seguintes terão, cada uma, um inteiro F (1 ≤ F ≤ 20.000) representando o fluxo de fótons que cada uma das N estrelas emitem (em fótons por segundo por milímetro quadrado). <br>
****

**Saída** <br>
Imprima um inteiro representando a quantidade de estrelas que serão percebidas ao se utilizar o telescópio em questão. <br>
**Exemplo** <br>

**Entrada** <br>
10000 <br>
3 <br>
4000 <br>
3500 <br>
5100 <br>
 
**Saída** <br>
2 <br>

**Entrada** <br>
5869 <br>
3 <br>
3975 <br>
14234 <br>
8569 <br>

**Saída** <br>
2 <br>

**Entrada** <br>
2967 <br>
9 <br>
18650 <br>
16338 <br>
2400 <br>
17702 <br>
14619 <br>
13934 <br>
7979 <br>
16316 <br>
1053 <br>

**Saída** <br>
6