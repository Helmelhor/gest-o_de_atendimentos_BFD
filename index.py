import atendimentos

while True:
    print('''Bem vindo ao sistema de atendimentos!
          Selecione uma opção:
          1- Adicionar atendimentos
          2- Pesquisar atendimentos
          3- Editar atendimentos
          4- Remover atendimentos
          ''')
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        print('Adicionar atendimentos')
    elif opcao == '2':
        print('Pesquisar atendimentos')
    elif opcao == '3':
        print('Editar atendimentos')
    elif opcao == '4':
        print('Remover atendimentos')
    else:
        print('Opção inválida. Tente novamente.')