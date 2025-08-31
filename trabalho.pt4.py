# parte 4

global id_global
id_global = 5411445 # o primeiro funcionário começa com esse id e vai aumentando a cada novo funcionário cadastrado

global lista_funcionarios
lista_funcionarios= [] # lista criada para armazenar os funcionários cadastrados


def remover_funcionario(): # função criada para remover os funcionários pelo id
    global lista_funcionarios

    continua = True
    while continua:
        funcionarioASerRemovido = int(input('Digite o id do funcionário a ser removido: '))
        for funcionario in lista_funcionarios:
            if funcionario['id'] == funcionarioASerRemovido: # compara o id passado pelo usuário com o id do funcionario atual
                lista_funcionarios.remove(funcionario) # remove o funcionário da lista
                continua = False
                print('Funcionário removido com sucesso!')
        if continua == True:
            print('Id inválido.')

def cadastrar_funcionario(id): # função criada para cadastrar um novo funcionário
    global id_global
    global lista_funcionarios

    # entrada de dados do funcionário a ser cadastrado
    print('-------------------------------------------MENU CADASTRAR FUNCIONÁRIO-------------------------------------------' )
    print(f'Id do Funcionário: {id}')
    nome = input('Por favor entre com o nome do funcionário: ')
    setor = input('Por favor entre com o setor do funcionário: ')
    salario = float(input('Por favor entre com o salário do funcionário: '))

    funcionario = {'nome': nome, 'setor': setor, 'salario': salario, 'id': id} # dicionário com os dados do funcionário
    lista_funcionarios.append(funcionario) # adiciona o novo funcionário na lista
    id_global = id_global + 1 # adiciona +1 para o próximo id


def consultar_funcionarios(): # função criada para consultar os funcionários já cadastrados

    controle = True
    while controle:
        print(menuInterno) # exibe o menu interno para o usuario
        escolhaDoMenuInterno = int(input('>>'))

        if escolhaDoMenuInterno == 1: # mostra todos os funcionários
            for item in lista_funcionarios:
                exibir_funcionario(item)

        elif escolhaDoMenuInterno == 2: # mostra somente o funcionário do id digitado pelo usuário
            controleId = True
            while controleId:
                idDoFuncionario = int(input('Digite o id do funcionário: '))
                print('')
                for funcionario in lista_funcionarios:
                    if funcionario['id'] == idDoFuncionario:
                        exibir_funcionario(funcionario)
                        controleId = False
                if controleId == True:
                    print('Id inválido')

        elif escolhaDoMenuInterno == 3: # mostra todos os funcionários de determinado setor digitado pelo usuário
            setorFuncionario = input('Digite o setor do(s) funcionário(s): ')
            print('')
            for funcionario in lista_funcionarios:
                if funcionario['setor'] == setorFuncionario:
                    exibir_funcionario(funcionario)

        elif escolhaDoMenuInterno == 4: # retorna para o menu principal
            print('Sair')
            controle = False

        else:
            print('Opção inválida.') # caso o usuário digite uma opção diferente de 1,2,3 ou 4


def exibir_funcionario(funcionario): # função para mostrar os dados do funcionário
    print(f'Id: {funcionario['id']}')
    print(f'Nome: {funcionario['nome']}')
    print(f'Setor: {funcionario['setor']}')
    print(f'Salário: {funcionario['salario']}\n')

# texto do menu interno que é exibido quando o usuário escolhe a opção "2) consultar funcionário"
menuInterno = '''-------------------------------------------MENU CONSULTAR FUNCIONÁRIO---------------------------------------------------
Escolha a opção desejada:
1. Consultar todos os funcionários  
2. Consultar funcionário por id 
3. Consultar funcionário por setor 
4. Retornar ao menu principal
------------------------------------------------------------------------------------------------------------------------'''

# print com mensagem de boas-vindas
print('Seja bem vindo(a) ao sistema de gerenciamento de funcionários! Desenvolvido por Ghabryella Miranda dos Santos.')
print('----------------------------------------------------------------------------------------------------------------')

#loop
controle = True
while controle:
    print('----------------------------------------------MENU PRINCIPAL----------------------------------------------------')
    print('Escolha a opção desejada:')
    print('1) Cadastrar Funcionário')
    print('2) Consultar Funcionário')
    print('3) Remover Funcionário')
    print('4) Sair')
    print('----------------------------------------------------------------------------------------------------------------')
    escolha = input('>>')

    if escolha == '1': # cadastra um novo funcionário
        cadastrar_funcionario(id_global)

    elif escolha == '2': # abre o menu interno de consultar funcionário
        print('Consultar Funcionário')
        consultar_funcionarios()

    elif escolha == '3': # remove um funcionário
        print('Remover Funcionário')
        remover_funcionario()

    elif escolha == '4': # encerra o programa
        controle = False
        print('Encerrar programa.')

    else:
        print('Opção inválida.') # se digitar algo diferente de 1,2,3 ou 4
