**Coleira Eletrônica Inquebrável**

Demasi é um terrorista e mafioso italiano que tentou escapar vindo para o Brasil. Mas Demasi não contava com a astúcia de nossa polícia, e acabou sendo preso aqui também.
Por ser mafioso, Demasi conseguiu contratar advogados muito bons, que através de muitos recursos na justiça, acabaram conseguindo uma liberdade condicional para ele.
Nessa liberdade condicional, Demasi deve permanecer a uma certa distância da delegacia de polícia responsável por ele. Para monitorá-lo melhor, eles instalaram nele uma coleira eletrônica inquebrável que, minuto a minuto, envia para uma central as movimentações de Demasi naquele momento.
A informação da coleira é enviada indicando uma direção e uma distância. Por exemplo, em quatro minutos chegam as quatro linhas de informação abaixo:

N 30
O 44
S 22
L 10

Isso significa que no primeiro minuto Demasi se deslocou 30 metros para o norte (letra N), no minuto seguinte andou 44 metros para o oeste (letra O), no outro minuto andou 22 metros para o sul (letra S) e no quarto minuto se deslocou 10 metros para o leste (letra L). Para poder dar um castigo ao terrorista, o juiz decidiu que Demasi só poderia andar nas quatro direções citadas acima. Ou seja, Demasi nunca se movimenta na direção noroeste, por exemplo. Neste problema, você pode supor que todos os movimentos de Demasi ocorrem sobre um plano cartesiano.
A polícia precisa estar sempre atenta à movimentação dele, e pede a sua ajuda para verificar se em algum momento o italiano se desloca a uma distância da delegacia maior do que a permitida. A distância considerada para esta medida é a distância euclidiana.
********

****Tarefa****
Sua missão é criar um programa que receba as informações da coleira de Demasi e diga se em algum momento Demasi esteve a uma distância maior do que a permitida.
Você deve assumir que no instante 0 (zero) Demasi está dentro da delegacia (ou seja, a uma distância zero).
********

****Entrada****
A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado).
A primeira linha da entrada contém dois inteiros N e M (2 ≤ N ≤ 500.000, 1 ≤ M ≤ 1.000.000) representando o número de registros enviados pela coleira de Demasi e a distância máxima que ele pode ficar da delegacia, respectivamente. As N linhas seguintes contêm os registros da coleira, em ordem de envio. Cada linha contém um caractere C (’N’, ’S’, ’L’ ou ’O’, como especiﬁcados acima) e um inteiro D (1 ≤ D ≤ 1.000) representando a distância percorrida no minuto.
****

****Saída****
Seu programa deve imprimir, na saída padrão, o valor 1 se em algum momento Demasi se afastou da delegacia além da distância permitida, ou o valor 0 caso contrário.
****Exemplos****

**Entrada**
5 10
N 2
L 3
S 4
O 4
O 3

**Saída**
0

**Entrada**
5 10
N 6
L 8
S 15
O 5
O 4

**Saída**
1