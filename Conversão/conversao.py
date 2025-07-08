from moedas import converter_cotaca

def menu():
    print()
    print('1- Converter Dólar em Real')
    print('2- Converter Euro em Real')
    print('3- Converter Iene em Real')
    print('4- Outra cotação')
    print('0- Sair')
    print()

opcao = 1


while opcao != 0:
    menu()
    opcao = int(input('Escolha uma opção: '))

    destino = 'BRL'
    valor = int(input('Digite o valor: '))

    match opcao:
        case 1: origem = 'USD'
        case 2: origem = 'EUR'
        case 3: origem = 'JPY'
        case 4:
            origem = input("Digite a ORIGEM: ")
            destino = input("Digite o DESTINO: ")

    if opcao:
        print()
        print('****************************************')
        print(f'{origem} para {destino}: ', converter_cotaca(origem, destino, valor))
        print('****************************************') 
        print()
                