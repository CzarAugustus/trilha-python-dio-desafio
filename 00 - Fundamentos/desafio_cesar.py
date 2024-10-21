#importando a função que registra a data e a hora
import datetime

#criando uma função para armazenar o valor, a hora e a data do depósito
def registrar_deposito(valor_deposito):
    data_hora_dep = datetime.datetime.now()
    return valor_deposito, data_hora_dep

#criando uma função para armazenar o valor, a hora e a data do saque
def registrar_saque(valor_saque):
    data_hora_saq = datetime.datetime.now()
    return valor_saque, data_hora_saq

menu = """
[d] Depositar
[s] Sacar
[e] Saldo / Extrato
[q] Sair
=> """

saldo = 0
limite = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor_deposito = float(input("Informe o valor do depósito: "))  # informando o valor de depósito
        if valor_deposito > 0:
            # a função registrar_deposito é chamada para registrar o valor a hora e a data do mesmo
            valor_deposito, data_hora_dep = registrar_deposito(valor_deposito)
            saldo += valor_deposito  # atualizando o saldo
            # registrando a movimentação no extrato
            extrato += f"Depósito: R$ {valor_deposito:.2f} em {data_hora_dep.strftime('%d/%m/%Y %H:%M:%S')}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))  # informando o valor de saque
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor_saque > 0:  # se saque válido, chama a função registrar saque para armazenar o valor, a data e a hora do mesmo
            valor_saque, data_hora_saque = registrar_saque(valor_saque)
            saldo -= valor_saque  # saldo atualizado
            # registrando a movimentação no extrato
            extrato += f"Saque: R$ {valor_saque:.2f} em {data_hora_saque.strftime('%d/%m/%Y %H:%M:%S')}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
