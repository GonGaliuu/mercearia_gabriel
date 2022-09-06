listaprodutos = {}
def codigoselecao():
    while True:
        print(f'|Escolha a opção desejada|')
        print(f'|-----------------------|')
        print(f'| 1 | Cadastrar Produto |')
        print(f'| 2 | Consultar Produto |')
        print(f'| 3 |  Remover Produto  |')
        print(f'|-----------------------|')
        codigo = input('Digite o código desejado de acordo com a tabela acima: ')
        try:
            codigo = int(codigo)
        except:
            print('Valor inválido, por favor, verifique a tabela.')
            continue
        if codigo == 1:
            cadastrarproduto()
        elif codigo == 2:
            consultarproduto()
        elif codigo == 3:
            removerprodutododicionario()

def consultartodososprodutos():
    for i in listaprodutos:
        mostrarproduto(i)

def mostrarproduto(valor):
    testedeerro = listaprodutos[valor]
    print(f'Código     =     {valor}')
    print(f'Nome       =     {listaprodutos[valor]["Nome"]}')
    print(f'Fabricante =     {listaprodutos[valor]["Fabricante"]}')
    print(f'Valor      =     {listaprodutos[valor]["Valor"]}')
    print(f'------------------------------------')

def consultarprodutosporcodigo():
    while True:
        try:
            codigo = input('Por favor digite o código que deseja consultar: ')
            mostrarproduto(codigo)
        except:
            print(f'O produto não existe!')
            continue
        break

def consultarprodutosporfabricante():
    codigo = input('Por favor digite o fabricante que deseja consultar: ')
    contador = 0
    for i in listaprodutos:
        if listaprodutos[i]['Fabricante'] == codigo:
            mostrarproduto(i)
            contador = 1
    if contador == 0:
        print('Não existem produtos deste fabricante!')

def removerprodutododicionario():
    continuar = 2
    while True:
        try:
            codigo = input('Por favor digite o código que deseja remover: ')
            del listaprodutos[codigo]
            print('Removido com sucesso')
            break
        except:
            print(f'Não existe um produto com este código')
            while True:
                if continuar == 1:
                    continuar = 2
                    break
                print(f'Deseja continuar?')
                print(f'|Código|Opção|')
                print(f'|   0  | Não |')
                print(f'|   1  | Sim |')
                print(f'|------|-----|')
                continuar = input('Código: ')
                try:
                    continuar = int(continuar)
                except:
                    print(f'Valor inválido, por favor verifique a tabela! ')
                    continue
                if continuar == 0:
                    break
                elif continuar == 1:
                    continue
                else:
                    print(f'Valor inválido, por favor verifique a tabela! ')
            if continuar == 0:
                break
def mudargramatica(codigo):
    codigo  = int(codigo)
    if codigo < 10:
        codigo = '00' + str(codigo)
    elif 10 < codigo < 100:
        codigo = '0' + str(codigo)
    else:
        codigo = str(codigo)
    return codigo

def cadastrarproduto():
    print(f'Você selecionou a opção cadastrar produto')
    codigoproduto = 1
    codigoproduto = mudargramatica(codigoproduto)
    while True:
        if codigoproduto not in listaprodutos:
            break
        else:
            codigoproduto = int(codigoproduto) + 1
            codigoproduto = mudargramatica(codigoproduto)
            continue

    print(f'Codigo do Produto: {codigoproduto}')
    nomeproduto = input(f'Por favor, entre com o NOME do produto------------> ')
    fabricanteproduto = input(f'Por favor, entre com o FABRICANTE do produto------> ')
    while True:
        valorproduto = input(f'Por favor, entre com o valor do produto-----------> ')
        try:
            float(valorproduto)
        except:
            print(f'Valor inválido, por favor, utilizar numeros separados por ponto caso necessário. Ex: R$5 ou R$3.75')
            continue
        break
    listaprodutos[codigoproduto] = {'Nome': f'{nomeproduto}', 'Fabricante': f'{fabricanteproduto}', 'Valor': f'R${valorproduto}'}

def consultarproduto():
    while True:
        print(f'|Escolha a opção desejada|')
        print(f'|-Codigo-|----------------------------------|')
        print(f'|    1   |    Consultar Todos os Produtos   |')
        print(f'|    2   |    Consultar Produto Por código  |')
        print(f'|    3   | Consultar Produto por Fabricante |')
        print(f'|--------|----------------------------------|')
        codigo = input('Digite o código desejado de acordo com a tabela acima: ')
        try:
            codigo = int(codigo)
        except:
            print('Valor inválido, por favor, verifique a tabela.')
            continue
        if codigo == 1:
            consultartodososprodutos()
        elif codigo == 2:
            consultarprodutosporcodigo()
        elif codigo == 3:
            consultarprodutosporfabricante()
        else:
            print('Valor inválido, por favor verifique na tabela a opção desejada: ')
        break

print(f'Bem vindo ao controle de estoque da Mercearia Gabriel Estéfono')
while True:
    codigoselecao()
    break