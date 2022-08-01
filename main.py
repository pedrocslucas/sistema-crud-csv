import csv
import uteis as ut

def menu():
    print("""1 - Cadastrar
2 - Listar
3 - Editar
4 - Deletar
5 - Sair e Salvar""")

#------------------ Usuário na lista
def inList(lista):
    encontrado = False
    pos = 0
    while(True):
        try:
            user = str(input('Digite o nome de usuário:'))
            email = str(input('Digite o email:'))
            cont = 0
            for conta in lista:
                if conta[1] == user and conta[2] == email:
                    encontrado = True
                    pos = cont
                cont += 1
        except:
            print('Erro ao encontrar usuário!')
        break
    if encontrado:
        print(f'Usuário encontrado! {user} na posicao {pos}')
        return pos
    else:
        print(f'Usuário não encontrado! {user}')
        return 0

#----------------- Mesmo Nome de Usuário
def sameUser(user, lista):
    pode = True
    for conta in lista:
        if conta[1] == user:
            print('Nome de usuário já existente!')
            pode = False
    return pode

#----------------- Cadastrar
def cadastrar(lista):
    dado = []
    while True:
        try:
            while True:
                id = str(len(lista))
                nome = str(input('Digite seu nome de usuário: ')).strip().lower()
                if sameUser(nome, lista):
                    break
            
            email = str(input('Digite seu email: '))
            while True:
                senha = input('Digite sua senha: ')
                confSenha = input('Comfirme sua senha: ')
                if senha != confSenha:
                    print('As senha devem ser iguais! ')
                else:
                    break
        except:
            print('Erro ao cadastrar!')
            break
        else:
            dado = [id, nome, email, senha]
            print('Usuário CADASTRADO com sucesso!')
            break
    return dado

#------------------------- Listar os Usuários
def listar(lista):
    try:
        if(len(lista) == 1):
            print('Lista Vazia!')
        else:
            print(f'{"Lista de Contas":^30}')
            print('-'*30)
            for i in range (0, len(lista)):
                if i != 0:
                    print(f'Conta Nº {i}')
                    print(f'Id: {lista[i][0]}')
                    print(f'Nome: {lista[i][1]}')
                    print(f'E-mail: {lista[i][2]}')
                    print(f'Senha: {lista[i][3]}')
                    print('-'*30)
    except:
        print('Erro ao Listar Usuários!')


#------------------------- Editar
def editar(lista):
    return 0

#------------------------ Excluir
def excluir(lista, pos):
    user = ''
    new_lista = list()
    for i in range (0, len(lista)):
        if pos == i:
            user = lista[i][1]
    while True:
        try:
            resp = str(input(f'Tem certeza que deseja remover o usuário {user}?(s/n) ')).strip().lower()
            if resp == 's' or resp == 'sim' or resp == 'si' or resp == 'yes':
                lista.pop(pos)
                new_lista = lista
                print('Usuário REMOVIDO com sucesso!')
                break
            elif resp == 'n' or resp == 'nao' or resp == 'não' or resp == 'no':
                print('Operação Cancelada!\n')
                break
        except:
            print('Erro ao excluir usuário...')
    return new_lista


def salvar(lista, file):
    with open(file, 'w+', newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(lista)
        print('Arquivo Salvo!')


#Programa Principal

#header = ['Id', 'Usuario', 'Email', 'Senha']
dados = list()

with open('dados.csv', 'r+', newline='') as arquivo:
    writer = csv.writer(arquivo)
    leitor = csv.reader(arquivo)
    for linha in leitor:
        dados.append(linha)
    while True:
        menu()
        op = ut.lerInt('Digite sua opção: ')
        if op < 1 or op > 5:
            print('Opção Inválida...\n')
        elif op == 1:
            new_user = list()
            new_user = (cadastrar(dados))
            dados.append(new_user)
            salvar(dados, 'dados.csv')
        elif op == 2:
            listar(dados)
        elif op == 3:
            #...editar
            inList(dados)
            continue
        elif op == 4:
            #...excluir
            pos = inList(dados)
            if pos != 0:
                dados = excluir(dados, pos)
                salvar(dados, 'dados.csv')
        elif op == 5:
            salvar(dados, 'dados.csv')
            break