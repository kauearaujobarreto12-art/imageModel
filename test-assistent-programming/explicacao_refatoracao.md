# Explicação da refatoração

O código original tinha nomes pouco descritivos e lógica de agregação escrita de forma manual. A refatoração transformou o bloco em uma função explícita e melhorou a legibilidade geral.

## Mudanças realizadas

- Renomeei a função `c` para `summarize_numbers`.
- Renomeei o parâmetro `l` para `numbers` e as variáveis `t`, `m`, `mx`, `mn` para `total`, `average`, `maximum`, `minimum`.
- Adicionei um docstring para explicar o propósito da função.
- Converti o iterável em lista usando `values = list(numbers)` para suportar qualquer coleção e medir seu tamanho.
- Adicionei uma validação para lançar `ValueError` quando a sequência estiver vazia.
- Usei `sum(values)` em vez de um laço manual para calcular o total.
- Usei `max(values)` e `min(values)` em vez de percorrer a lista manualmente para encontrar os valores máximo e mínimo.
- Adicionei o bloco `if __name__ == "__main__":` para isolar a execução de exemplo quando o módulo é importado.

## Benefícios

- O código ficou mais fácil de entender e manter.
- A lógica ficou mais declarativa, usando funções built-in do Python.
- O tratamento de erro para lista vazia evita resultados incorretos.
- A separação entre função e execução de exemplo torna o arquivo reutilizável em outros programas.