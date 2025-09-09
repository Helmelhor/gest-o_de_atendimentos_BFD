from atendimentos import atendimentos

def editar_atendimento():
    if not atendimentos:
        print("Nenhum atendimento cadastrado para editar.")
        return

    try:
        print(atendimentos)
        id_editar = int(input("Digite o ID do atendimento que deseja editar: "))
    except ValueError:
        print("ID inválido.")
        return

    atendimento = next((a for a in atendimentos if a["id_atendimento"] == id_editar), None)
    if not atendimento:
        print("Atendimento não encontrado.")
        return
    print(atendimento)
    print("O que deseja editar?")
    print("1 - Nome")
    print("2 - Serviço")
    print("3 - Valor")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_nome = input("Digite o novo nome: ")
        atendimento["nome"] = novo_nome
        print("Nome atualizado com sucesso!")
    elif opcao == "2":
        novo_servico = input("Digite o novo serviço: ")
        atendimento["servico"] = novo_servico
        print("Serviço atualizado com sucesso!")
    elif opcao == "3":
        while True:
            novo_valor_str = input("Digite o novo valor: ")
            try:
                novo_valor = float(novo_valor_str.replace(",", "."))
                atendimento["valor"] = novo_valor
                print("Valor atualizado com sucesso!")
                break
            except ValueError:
                print("Valor inválido! Digite novamente (ex: 100 ou 100,50).")
    else:
        print("Opção inválida.")