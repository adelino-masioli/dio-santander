saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

# TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.


def atualizar_saldo(saldo_atual, valor_deposito, valor_retirada):
    saldo_atual += valor_deposito
    saldo_atual -= valor_retirada
    return f"Saldo atualizado na conta: {round(saldo_atual, 1)}"

# TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).


# Exemplos de entrada e saída
print(atualizar_saldo(saldo_atual, valor_deposito, valor_retirada))
