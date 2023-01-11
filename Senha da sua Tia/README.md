# ****Senha da sua Tia****

Seu maior pesadelo está acontecendo: sua tia quer se cadastrar na rede social que você acessa. Comentários constrangedores, compartilhamentos desnecessários e fotos da sua infância farão parte do seu dia-a-dia, não há saída.<br>
Ela está se cadastrando, mas por motivos de segurança há algumas regras em relação à senha a ser escolhida por novos usuários. É necessário que a senha tenha no mínimo N caracteres, entre eles no mínimo M devem ser letras minúsculas, no mínimo A devem ser letras maiúsculas, e no mínimo K devem ser números.<br>
Sua tia está confusa, e pediu sua ajuda. Dada a senha que ela escolheu, diga se ela será aceita pelo site ou não.<br>
****Entrada****<br>
A entrada inicia com 4 inteiros N, M, A e K (6 ≤ N ≤ 1000, 0 ≤ M, A, K ≤ 1000, M+A+K ≤ N), conforme descrito no enunciado.
Em seguida há uma sequência de caracteres indicando a senha, com no mínimo 1 e no máximo 1000 caracteres, sendo estes letras e números, apenas.<br>
****Saída****<br>
Imprima uma linha contendo "Ok =/", se a senha atende todos os requisitos citados, ou "Ufa :)" caso contrário.<br>
****Exemplos****<br>

**Entrada:**<br>
6 1 1 1<br>
beterraba<br>

**Saída:**<br>
Ufa :)<br>

**Entrada:**<br>
6 3 1 6<br>
20Maio1994<br>

**Saída:**<br>
Ok =/<br>

**Entrada:**<br>
10 3 4 0<br>
TeenageMutantNinja<br>

**Saída:**<br>
Ufa :)<br>

**Entrada:**<br>
8 4 2 2<br>
123456<br>

**Saída:**<br>
Ufa :)