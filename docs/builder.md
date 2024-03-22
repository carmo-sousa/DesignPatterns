# Builder

Usar o padrão builder só faz sentido quando seus produtos são bem complexos
requerem configuração extensiva. Os dois produtos a seguir são relacionados,
embora eles não tenham uma interface em comum.

## Aplicabilidade

- Use o padrão `Builder` para se livrar de um "construtor telescópico".
- Use o padrão Builder quando você quer que seu código seja capaz de criar
  diferentes representaçãoes do mesmo produto (por exemplo, casas de pedra e madeira).
- Use o `Builder` para construir árvores `Composite` ou outros objetos complexos.

::: src.builder
