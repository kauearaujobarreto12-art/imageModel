# Constantes para otimização
PASSO_DIVISORES = 6

def eh_primo(n: int) -> bool:
    """Verifica se um número é primo usando um algoritmo otimizado.

    Args:
        n (int): Número a ser verificado. Deve ser um inteiro não negativo.

    Returns:
        bool: True se `n` for primo, False caso contrário.

    Raises:
        ValueError: Se `n` não for um inteiro não negativo.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("O número deve ser um inteiro não negativo.")

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Verifica divisores da forma 6k ± 1 até sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += PASSO_DIVISORES

    return True

def executar_testes():
    """Executa testes unitários para a função eh_primo."""
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


def solicitar_numero() -> int:
    """Solicita um número inteiro ao usuário e retorna o valor convertido."""
    while True:
        entrada = input("Digite um número inteiro para verificar se ele é primo: ").strip()
        if entrada == "":
            print("Entrada vazia. Por favor, informe um número inteiro.")
            continue
        try:
            numero = int(entrada)
            if numero < 0:
                print("Por favor, insira um inteiro não negativo.")
                continue
            return numero
        except ValueError:
            print("Valor inválido. Digite um número inteiro válido.")


def main():
    numero = solicitar_numero()
    if eh_primo(numero):
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")


if __name__ == "__main__":
    main()
