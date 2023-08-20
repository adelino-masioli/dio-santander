# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.


def realizar_saque(saldo_total, valor_saque):
    if saldo_total >= valor_saque:
        saldo_total -= valor_saque
        return True, saldo_total
    else:
        return False, saldo_total


sucesso, novo_saldo = realizar_saque(saldo_total, valor_saque)
if sucesso:
    print(f"Saque realizado com sucesso. Novo saldo: {novo_saldo}")
else:
    print("Saldo insuficiente. Saque nao realizado!")
