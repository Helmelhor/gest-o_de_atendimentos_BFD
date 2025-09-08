from atendimentos import atendimentos as lista_atendimentos

def adicionar_atendimento():
    print("\n=== Adicionar Atendimento ===")
    nome = input("Digite o nome do cliente: ")
    servico = input("Digite o serviço realizado: ")
    while True:
        valor_str = input("Digite o valor do atendimento: ")
        try:
            valor = float(valor_str.replace(",", ".")) 
            break
        except ValueError:
            print(" Valor inválido! Digite novamente (ex: 100 ou 100,50).")


    atendimento = {
        "id_atendimento": len(lista_atendimentos) + 1,
        "nome": nome,
        "servico": servico,
        "valor": valor
    }

    lista_atendimentos.append(atendimento)
    print(f" Atendimento de {nome} adicionado com sucesso!")