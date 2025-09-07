while True:
    print('''Bem vindo ao sistema de atendimentos!
          Selecione uma opção:
          1- Adicionar atendimento
          2- Remover atendimento
          3- Listar atendimentos
          4- Sair
          ''')
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        print('Adicionar atendimento')
    elif opcao == '2':
        print('Remover atendimento')
    elif opcao == '3':
        print('Listar atendimentos')
    elif opcao == '4':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Tente novamente.')