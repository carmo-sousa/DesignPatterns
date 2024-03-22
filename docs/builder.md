# Builder

Usar o padrão builder só faz sentido quando seus produtos são bem complexos
requerem configuração extensiva. Os dois produtos a seguir são relacionados,
embora eles não tenham uma interface em comum.

## Aplicabilidade

- Use o padrão `Builder` para se livrar de um "construtor telescópico".
- Use o padrão Builder quando você quer que seu código seja capaz de criar
  diferentes representaçãoes do mesmo produto (por exemplo, casas de pedra e madeira).
- Use o `Builder` para construir árvores `Composite` ou outros objetos complexos.

## Como implementar

1. Certifique-se quer você pode definir claramente as etapas comuns de
construção para construir todas as representações do produto disponíneis. Do
contrário, você não será capaz de implemnentar o pradrão.

2. Declare essas etapas na interface builder base.

3. Crie uma classe builder concreta para cada representação do produto e
implemnente suas etapas de construção.
Não se esqueça de implementar um método para recuperar os resultados da
construção. O motivo pelo qual esse método não pode ser declarado dentro da
interface do builder é porque vários builders podem construir produtos que não
tem uma inferface comum. Portanto, você não sabe qual será o tipo de retorno
para tal método. Contudo, se você está lidando com produtos de uma única
hierarquia, o método de obtenção pode ser adicionado com segurança para a interface
base.

4. Pense em criar uma classe diretor. Ela pode encapsular várias maneiras de construir
um produto usando o mesmo objeto builder.

5. O código cliente cria tanto os objetos do builder como do diretor. Antes da construção
começar,, o cliente deve passar um objeto builder para o diretor. Geralmente o cliente
faz isso apenas uma vez, através de parâmetros do construtor do diretor. O diretor usa
o objeto builder em todas as contruções futuras. Existe uma alternativa onde o builder é
passado diretamente ao método de construção do diretor.

6. O resultado da construção pode ser obtido diretamente do diretor apenas se todos os
produtos seguirem a mesma interface. Do contrário o cliente deve obter o resultado do builder.

::: src.builder
