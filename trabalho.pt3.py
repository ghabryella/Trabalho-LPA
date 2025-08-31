# parte 3

# mensagem de boas-vindas
print('Bem vindo(a) a fábrica de camisetas! Desenvolvido por Ghabryella Miranda dos Santos.\n')

# usuario digita qual modelo vai querer
print('Entre com o modelo desejado:\n')

# apresentação das opçoes
print('MCS - Manga Curta Simples:')
print ('MLS - Manga Longa Simples:')
print ('MCE - Manga Curta Com Estampa:')
print ('MLE - Manga Longa Com Estampa:')


def escolha_modelo():
    escolha = input('>> ')
    while escolha not in ['MCS', 'MLS', 'MCE', 'MLE']: #verifica se a resposta é válida
        print('Escolha inválida, entre com o modelo novamente.')
        escolha = input('>> ') #pede a escolha novamente se a resposta for inválida
    return escolha

modelo = escolha_modelo()

# valor unitário dos modelos
if modelo == 'MCS':
    precoUnitario = 1.80

elif modelo == 'MLS':
    precoUnitario = 2.10

elif modelo == 'MCE':
    precoUnitario = 2.90

else:
    precoUnitario = 3.20


def num_camisetas():
    controle = True
    while controle:
        try:
            quantidade = int(input('Entre com o número de camisetas: '))
            while quantidade >20000:
                print('Não aceitamos tantas camisetas de uma vez.\nPor favor, entre com o número de camisetas novamente.')
                quantidade = int(input('Entre com o número de camisetas: '))
            controle = False
        except ValueError:
            controle = True

    return quantidade

quantiaCamisetas = num_camisetas()

if quantiaCamisetas <20:
    desconto = 0

elif quantiaCamisetas >=20 and quantiaCamisetas <200:
    desconto = 5

elif quantiaCamisetas >=200 and quantiaCamisetas <2000:
    desconto = 7

elif quantiaCamisetas >=2000 and quantiaCamisetas <=20000:
    desconto = 12

camisetasSemDesconto = quantiaCamisetas * precoUnitario
camisetasComDesconto = camisetasSemDesconto * (1 - desconto / 100)

quantidadeComDesconto = quantiaCamisetas * (1 - desconto / 100)

print('\nEscolha o tipo de frete:')
print('1 - Frete por transportadora - R$ 100.00')
print('2 - Frete por sedex - R$ 200.00')
print('0 - Retirar o pedido na fábrica - R$ 0.00')

def frete():
    tipoFrete = input('>> ')
    while tipoFrete not in ['1', '2', '0']:
        tipoFrete = input('>> ')

    if tipoFrete == '1':
        return 100.00

    elif tipoFrete == '2':
        return 200.00

    else:
        return 0.00

valorDoFrete = frete()


total = camisetasComDesconto + valorDoFrete

print(f'\nTotal: R${total:.2f} (Modelo: {precoUnitario:.2f} * Quantidade(com desconto): {quantidadeComDesconto:.0f} + Frete: R${valorDoFrete:.2f})')





