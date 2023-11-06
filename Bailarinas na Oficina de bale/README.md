# Bailarinas na Oficina de Balé

Uma academia de balé irá organizar uma Oficina de Balé Intensivo (OBI) na Semana de Balé Contemporâneo (SBC). Nessa academia, existem N bailarinas que praticam regularmente. O dono da academia, por ser experiente, consegue medir o nível de habilidade de cada uma delas por um número inteiro; nessa medição, números maiores correspondem a dançarinas mais habilidosas, e os números obtidos são todos distintos. Além disso, ele possui uma lista das bailarinas em ordem cronológica de ingresso na academia: As bailarinas que aparecem primeiro na lista estão há mais tempo na academia, e as que estão no final ingressaram mais recentemente.

O dono da academia decidiu escolher duas das bailarinas para ajudá-lo na realização do evento: uma ajudará no trabalho braçal, enquanto a outra irá exemplificar os passos de balé. Por seu perfeccionismo, ele deseja que a bailarina que exemplificará os passos de dança seja, dentre as duas meninas do par, a mais habilidosa e a que frequenta a academia há mais tempo.

Ele sabe que a Oficina será um sucesso desde que os dois critérios mencionados acima sejam satisfeitos pela dupla de dançarinas escolhidas. Com isso, ele ficou curioso para saber quantas duplas de dançarinas podem ajudá-lo na Oficina. A quantidade de dançarinas, contudo, é relativamente grande e ele não possui nem tempo nem paciência para fazer tal cálculo. Como vocês são amigos, ele pediu a sua ajuda para contar quantas duplas são válidas. Você pode ajudá-lo?

Por exemplo, digamos que a academia possua 5 dançarinas com níveis de habilidade 1, 5, 2, 4 e 3, onde a primeira, que possui nível "1", está na academia há mais tempo e a última, que possui nível "3", está há menos. Temos, então, 4 possíveis duplas que poderemos usar nesta Oficina, que são (5, 2),(5, 4),(5, 3) e (4, 3). Note que a dupla (1, 3), por exemplo, não pode ser escolhida pelo dono da academia, pois a mais habilidosa dentre as duas é também a mais nova da dupla.

Entrada

A primeira linha contém um número N, que representa a quantidade de dançarinas que estão registradas na academia. A segunda linha da entrada contém N inteiros, onde o primeiro inteiro é o nível da dançarina que está há mais tempo na academia, o segundo inteiro é o nível da próxima dançarina mais antiga na academia (mas mais nova que a dançarina anterior), e assim sucessivamente.

Saída

A saída consistirá num único número X, que representa o total de duplas de dançarinas válidas para essa Oficina, dadas as regras descritas anteriormente.

Restrições

1 ≤ N ≤ 100 000. <br>
Todas as dançarinas possuirão níveis distintos, entre 1 e 100 000. <br>
O total de pares válidos, em todos os casos, será ≤ 1 000 000. <br>


Exemplos

Entrada <br>
5 <br>
1 5 2 4 3 <br>

Saída
4 <br>

Entrada <br>
9 <br>
9 8 7 6 5 4 3 1 2

Saída <br>
35

