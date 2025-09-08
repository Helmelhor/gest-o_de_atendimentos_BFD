import adicionar
import atendimentos
import editar
from atendimentos import atendimentos as lista_atendimentos
import pesquisar
import remover

while True:
    print('''Bem vindo ao sistema de atendimentos!
          Selecione uma opção:
          1- Adicionar atendimentos
          2- Pesquisar atendimentos
          3- Editar atendimentos
          4- Remover atendimentos
          5- Sair
          ''')
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        adicionar.adicionar_atendimento()
    elif opcao == '2':
        pesquisar.pesquisar_atendimento()
    elif opcao == '3':
        editar.editar_atendimento()
    elif opcao == '4':
        remover.remover_atendimento()
    elif opcao == '5':
        break
    else:
        print('Opção inválida. Tente novamente.')
