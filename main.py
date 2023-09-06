# Identificação
print('Bem-vindo ao Controle de Estoque da Bicicletaria de Adriana C. G. Thume RU 1902469')
# Declaração de lista
listaPecas = []

codigoPeca = 0
# Início da função cadastrarPeca
def cadastrarPeca(codigo):
    print('Bem-vindo ao menu de Cadastrar Peças')
    print('Código da Peça: {}'.format(codigo))

    nome = input('Entre com o nome da peça: ')
    fabricante = input('Entre com o fabricante da peça: ')
    valor = float(input('Entre com o valor(R$) da peça: '))

    # Armazenando os dados no dicionário
    dicionario_pecas = {'codigo': codigoPeca, 'nome': nome,
                        'fabricante': fabricante, 'valor': valor}

    # Copiando os dados do dicionário para a lista
    listaPecas.append(dicionario_pecas.copy())

# Início da função consultarPeca
def consultarPeca():
    print('Bem-vindo ao menu de Consultar Peças')
    while True:
        opcao_consultar = input('\nEscolha a opção desejada:\n' +
                                '1 - Consultar Todas as Peças\n' +
                                '2 - Consultar Peças por Código\n' +
                                '3 - Consultar Peças por Fabricante\n' +
                                '4 - Retornar\n' +
                                '>>')
        if opcao_consultar == '1':
            print('Você escolheu a opção Consultar Todas as Peças')
            for peca in listaPecas:  # Percorrendo a lista
                print('______________________')
                for key, value in peca.items():
                    print('{}: {}'.format(key, value))
                print('______________________')

        elif opcao_consultar == '2':
            print('Você escolheu a opção Consultar Peças por Código')
            valor = int(input('Entre com o código desejado: '))
            for peca in listaPecas:
                if peca['codigo'] == valor:
                    print('______________________')
                    for key, value in peca.items():
                        print('{}: {}'.format(key, value))
                    print('______________________')

        elif opcao_consultar == '3':
            print('Você escolheu a opção Consultar Peças por Fabricante')
            valor = input('Entre com o fabricante desejado: ')
            for peca in listaPecas:
                if peca['fabricante'] == valor:
                    print('______________________')
                    for key, value in peca.items():
                        print('{}: {}'.format(key, value))
                    print('______________________')

        elif opcao_consultar == '4':
            return  # Sai da função

        else:
            print('Opção inválida. Tente novamente.')
            continue  # Volta para o início do while

# Início da função removerPeca
def removerPeca():
    print('Bem-vindo ao menu de Remover Peças')
    valor = int(input('Entre com o código do produto que deseja remover: '))
    for peca in listaPecas:
        if peca['codigo'] == valor:
            listaPecas.remove(peca)
            print('Produto removido com sucesso.')


while True:
    opcaoMenu = input('\nEscolha a opção desejada:\n' +
                      '1 - Cadastrar Peças\n' +
                      '2 - Consultar Peças\n' +
                      '3 - Remover Peças\n' +
                      '4 - Sair\n' +
                      '>>')
    if opcaoMenu == '1':
        codigoPeca = codigoPeca + 1  # Contador como parâmetro
        cadastrarPeca(codigoPeca)

    elif opcaoMenu == '2':
        consultarPeca()

    elif opcaoMenu == '3':
        removerPeca()

    elif opcaoMenu == '4':
        break

    else:
        print('Opção inválida. Tente novamente.')
        continue  # Volta para o início do while