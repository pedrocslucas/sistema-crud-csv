import csv
import uteis as ut

#------------------ Menu da Aplicação
def menu():
    print("""1 - Cadastrar
2 - Listar
3 - Editar
4 - Deletar
5 - Sair e Salvar""")


def listaVazia(lista):
    if len(lista) == 1:
        return True
    else:
        return False


#------------------ Retorna um Id Válido para um usuário
def retornarId(lista):
    if not listaVazia(lista):
        id = lista[-1][0] + 1 #somando 1 com o id da última conta
    return id


#------------------ Encontrar Posição do Usuário na lista
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
    if not listaVazia(lista):
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
                id = retornarId(lista)
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
        if listaVazia(lista):
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
def editar(lista, pos):
    user = []
    new_lista = list()
    for i in range(0, len(lista)):
        if i == pos:
            user = lista[i]
    while True:
        try:
            print("O que deseja alterar?\n1 - nome de usuário\n2 - email\n3 - senha")
            item = ut.lerInt('Digite sua opção: ')
            if item == 1: # Editando Nome - [1]
                while True:
                    nome = str(input('Digite o novo nome de usuário: ')).strip()
                    if nome == user[1]:
                        print('O nome não pode ser igual ao anterior!')
                    elif sameUser(nome, lista):
                        print('NOME de usuário alterado com Sucesso!')
                        user[1] = nome
                        break
                break
            elif item == 2: # Editando Email - [2]
                while True:
                    email = str(input('Digite o novo email do usuário: ')).strip()
                    if email == user[2]:
                        print('O email não pode ser igual ao anterior!')
                    else:
                        print('EMAIL do usuário alterado com Sucesso!')
                        user[2] = email
                        break
                break
            elif item == 3: # Editando Senha - [3]
                while True:
                    senha = str(input('Digite a nova senha: ')).strip()
                    if senha == user[3]:
                        print('A nova senha não pode ser igual a anterior!')
                    else:
                        confSenha = str(input('Confirme a senha: ')).strip()
                        if confSenha != senha:
                            print('As senhas devem ser iguais!')
                        else:
                            print('SENHA do usuário alterada com Sucesso!')
                            user[3] = senha
                            break
                break
            else:
                print('Opção Inválida...\n')
        except:
            print('Erro ao editar usuário...\n')
            break
    #Deletando Usuário Editado
    lista.pop(pos)
    new_lista = lista
    new_lista.insert(pos, user) #Adicionando Usuário Editado!
    return new_lista


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
            print('Erro ao excluir usuário...\n')
    return new_lista


#---------------------- Salvar Arquivo
def salvar(lista, file):
    with open(file, 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(lista)
        print('Arquivo Salvo!')
        