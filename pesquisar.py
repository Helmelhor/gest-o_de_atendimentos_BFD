from atendimentos import atendimentos

def pesquisar_atendimento():
    termo = input("Digite o nome ou serviço para pesquisar: ").lower()
    encontrados = []
    for atendimento in atendimentos:
        if termo in atendimento["nome"].lower() or termo in atendimento["servico"].lower():
            encontrados.append(atendimento)
    if encontrados:
        print("\nAtendimentos encontrados:")
        for a in encontrados:
            print(f"ID: {a['id_atendimento']} | Nome: {a['nome']} | Serviço: {a['servico']} | Valor: {a['valor']}")
    else:
        print("Nenhum atendimento encontrado com esse termo.")