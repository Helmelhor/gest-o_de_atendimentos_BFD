from atendimentos import atendimentos

def remover_atendimento():
    print("REMOVER ATENDIMENTO")
    for atendimento in atendimentos:
        print(atendimento)
    id_remover = input("Digite o ID que deseja remover: ")
    for atendimento in atendimentos:
        if str(atendimento["id_atendimento"]) == id_remover:
            atendimentos.remove(atendimento)
            print(f"Atendimento removido com sucesso")
            break
    else:
        print("ID não encontrado.")
    print(atendimentos)
    