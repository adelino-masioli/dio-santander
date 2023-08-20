valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

# TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.


def calcular_valor_final(valor_inicial, taxa_juros, periodo):
    # ** é usado para representar a exponenciação
    valor_final = valor_inicial * (1 + taxa_juros)**periodo
    valor_final = round(valor_final, 2)  # Arredonda para duas casas decimais
    return valor_final


valor_final = calcular_valor_final(valor_inicial, taxa_juros, periodo)

print("Valor final do investimento: R$", valor_final)
