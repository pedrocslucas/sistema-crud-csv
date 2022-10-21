import csv
import uteis as ut
import functionsSistem as fs

#Programa Principal

#header = ['Id', 'Usuario', 'Email', 'Senha']
dados = list()
file = 'dados.csv'

with open('dados.csv', 'r+', newline='') as arquivo:
    writer = csv.writer(arquivo)
    leitor = csv.reader(arquivo)
    #Carregar dados!
    for linha in leitor:
        if not len(linha) == 0:
            dados.append(linha)
    while True:
        fs.menu()
        op = ut.lerInt('Digite sua opção: ')
        if op < 1 or op > 5:
            print('Opção Inválida...\n')
        elif op == 1:
            #...cadastrar
            new_user = list()
            new_user = (fs.cadastrar(dados))
            dados.append(new_user)
            fs.salvar(dados, file)
        elif op == 2:
            #...listar dados
            fs.listar(dados)
        elif op == 3:
            #...editar
            pos = fs.inList(dados)
            if pos != 0:
                dados = fs.editar(dados, pos)
                fs.salvar(dados, file)
        elif op == 4:
            #...excluir
            pos = fs.inList(dados)
            if pos != 0:
                dados = fs.excluir(dados, pos)
                fs.salvar(dados, file)
        elif op == 5:
            fs.salvar(dados, file)
            break