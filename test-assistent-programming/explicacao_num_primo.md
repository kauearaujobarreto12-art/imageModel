Read [](file:///c%3A/Users/KAUEAMORIM/Desktop/ProjetoSiteComReconhecimentoJoia/test-assistent-programming/num_primo.py)

## Explicação Técnica e Didática do Código em num_primo.py

Vou explicar o código linha a linha, de forma técnica (focando em conceitos de programação e algoritmos) e didática (usando analogias simples e exemplos quando possível). O código implementa uma função para verificar se um número é primo, com otimizações para eficiência, validação de entrada e uma seção de testes separada, seguindo princípios de clean code.

### Parte 1: Constantes e Imports
```python
# Constantes para otimização
PASSO_DIVISORES = 6
```
- **Linha 1-2:** Define uma constante `PASSO_DIVISORES` com valor 6.  
  - **Técnico:** Constantes evitam "números mágicos" no código, melhorando legibilidade e manutenção. Aqui, representa o passo para pular divisores na forma 6k ± 1.  
  - **Didático:** É como nomear uma configuração: "Usamos 6 como passo porque primos seguem esse padrão, e agora fica claro no código."
- **Imports:** Neste código não é necessário importar nada. O Python já fornece `input()` e `int()` para ler e converter a entrada do usuário.

### Parte 2: Definição da Função Principal
```python
def eh_primo(n: int) -> bool:
```
- **Linha 4:** Define a função `eh_primo`.  
  - **Técnico:** Mesmo que antes, mas agora com validação e docstring mais detalhada.  
  - **Didático:** A "máquina" principal, agora mais robusta.

```python
    """
    Verifica se um número é primo usando um algoritmo otimizado.

    Args:
        n (int): O número a ser verificado.

    Returns:
        bool: True se n for primo, False caso contrário.

    Raises:
        ValueError: Se n não for um inteiro não negativo.
    """
```
- **Linhas 5-14:** Docstring detalhada no formato Google/NumPy.  
  - **Técnico:** Descreve argumentos, retorno e exceções, facilitando uso e documentação automática.  
  - **Didático:** "Agora a etiqueta explica tudo: o que entra, o que sai e possíveis erros."

```python
    if not isinstance(n, int) or n < 0:
        raise ValueError("O número deve ser um inteiro não negativo.")
```
- **Linhas 15-16:** Validação de entrada.  
  - **Técnico:** Garante que `n` seja inteiro não negativo, lançando `ValueError` se não for. Previne bugs.  
  - **Didático:** "Antes de processar, verificamos se o input faz sentido – como checar se a porta está certa antes de entrar."

### Parte 3: Verificações Iniciais (Casos Base)
```python
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
```
- **Linhas 18-22:** Mesmas verificações que antes, mas agora com validação prévia.  
  - **Técnico:** Casos base otimizados.  
  - **Didático:** "Descartamos casos óbvios rapidamente, como antes."

### Parte 4: Loop de Verificação (Algoritmo Otimizado)
```python
    # Verifica divisores da forma 6k ± 1 até sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += PASSO_DIVISORES

    return True
```
- **Linhas 24-31:** Loop com comentário explicativo e uso da constante.  
  - **Técnico:** Comentário inline explica a lógica. Usa `PASSO_DIVISORES` em vez de 6.  
  - **Didático:** "O loop agora tem uma nota dizendo o que faz, e usa a constante para clareza."

### Parte 5: Função de Testes
```python
def executar_testes():
    """Executa testes unitários para a função eh_primo."""
```
- **Linhas 33-34:** Função opcional para testes automatizados.  
  - **Técnico:** Separa responsabilidades: uma função para lógica, outra para testes. Facilita reutilização.  
  - **Didático:** "Os testes têm sua própria sala para verificar a função sem afetar a execução principal."

```python
    testes = [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (16, False),
        (17, True),
        (18, False),
        (19, True),
        (97, True),
        (100, False),
    ]

    for numero, esperado in testes:
        try:
            resultado = eh_primo(numero)
            status = "OK" if resultado == esperado else "ERRO"
            print(f"{numero}: {resultado} (esperado: {esperado}) -> {status}")
        except ValueError as e:
            print(f"{numero}: ERRO - {e}")
```
- **Linhas 35-52:** Lista de testes com tratamento de exceções.  
  - **Técnico:** `try-except` captura erros de validação.  
  - **Didático:** "Testamos cada caso e mostramos se deu certo ou não."

### Parte 6: Entrada do Usuário
```python
def solicitar_numero() -> int:
    """Solicita um número inteiro ao usuário e retorna o valor convertido."""
```
- **Nova função:** Lê a entrada com `input()` e converte para `int`.  
  - **Técnico:** Usa repetição até o usuário fornecer um inteiro não negativo válido.  
  - **Didático:** "Pede o número, verifica se é um inteiro e só segue quando a entrada estiver correta."

```python
if __name__ == "__main__":
    main()
```
- **Linhas finais:** Executa a função principal que solicita o número e imprime se ele é primo ou não.  
  - **Técnico:** Padrão Python para fazer o script funcionar como programa principal.  
  - **Didático:** "Quando o usuário roda o arquivo, ele pergunta o número e devolve o resultado imediato."
### Resumo Geral
- **Clean Code Aplicado:** Constantes para números mágicos, funções pequenas e focadas, validação de entrada, docstrings detalhadas, comentários explicativos, tratamento de erros.
- **Algoritmo:** Mesmo otimizado, agora mais legível e robusto.
- **Boas Práticas:** Separação de responsabilidades, nomes descritivos, testes isolados.
- **Limitações:** Ainda para números pequenos/médios; para grandes, use algoritmos avançados.

Se quiser executar os testes ou ajustar mais, avise!