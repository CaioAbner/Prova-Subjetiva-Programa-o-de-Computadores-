def campoObrigatorio(valor):
    while True:
        resultado = input(valor).strip()

        if (not resultado):
            print(f"Erro! O campo não pode estar vazio!")
            continue
        
        try:
            return float(resultado)
        except ValueError:
            print(f"O valor digitado não foi um número. Por favor digite apenas números.")

def depositarValor(valor):
    if (valor <= 0):
        print(f"Não é possível realizar a operação, pois o valor digitado é menor que zero.")
    else:
        resultado = saldo_usuario + valor
        return resultado

def sacarValor(valor):
    if (valor > saldo_usuario or valor <= 0):
        print(f"Não é possível realizar a operação, pois o valor digitado é maior que o saldo ou é igual a zero.")
    else:
        resultado = saldo_usuario - valor
        return resultado
        
historico_saldos = []
saldo_usuario = campoObrigatorio("Digite o saldo: ")
historico_saldos.append({"operacao":"Saldo inicial", "valor": saldo_usuario})

while True:
    menu = int(input("Digite a operação que deseja realizar: \n1 - Consultar saldo\n2 - Depositar\n3 - Sacar\n4 - Histórico de Transações\n0 - Encerrar programa\n: "))

    if (menu == 0):
        print(f"O caixa está sendo fechado...")
        break
    elif (menu == 1):
        print(f"O valor do seu saldo é de: R$ {saldo_usuario}")
    elif (menu == 2):
        valor_depositado = campoObrigatorio("Digite o valor que deseja depositar: ")
        saldo_usuario = depositarValor(valor_depositado)
        historico_saldos.append({"operacao": "Depósito", "valor" : valor_depositado})
    elif (menu == 3):
        valor_sacado = campoObrigatorio("Digite o valor que deseja sacar: ")
        saldo_usuario = sacarValor(valor_sacado)
        historico_saldos.append({"operacao": "Saque", "valor": valor_sacado})
    elif (menu == 4):
        print(f"Eis seu histórico de transações:\n{historico_saldos}")
    else:
        print(f"Digite uma opção válida.")
        continue