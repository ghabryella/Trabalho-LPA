# parte 2

# mensagem de boas-vindas e apresentação do menu
print('Bem vindo(a) ao Marmita Express! Desenvolvido por Ghabryella Miranda dos Santos.')
print('--------------------------------------------------------------------------------')
print('-----------------------------Cardápio-------------------------------------------')
print('--------------------------------------------------------------------------------')
print('---------|  Tamanho  |  Bife Acebolado (BA)  |  Filé de Frango (FF)  |----------')
print('---------|     P     |       R$ 16,00        |       R$ 15,00        |----------')
print('---------|     M     |       R$ 18,00        |       R$ 17,00        |----------')
print('---------|     G     |       R$ 22,00        |       R$ 21,00        |----------')
print('--------------------------------------------------------------------------------')

# início do acumulador com valor zero
acumulador = 0.0

# loop da escolha do sabor e tamanho
while True:

    sabor = input('Entre com o sabor desejado (BA/FF): ')
    while sabor not in ['BA', 'FF']:
        print('Sabor inválido. Tente novamente.')
        sabor = input('Entre com o sabor desejado (BA/FF): ')

    tamanho = input('Entre com o tamanho desejado (P/M/G): ')
    while tamanho not in ['P', 'M', 'G']:
        print('Tamanho inválido. Tente novamente.')
        tamanho = input('Entre com o tamanho desejado (P/M/G): ')

# decisão do sabor e preço do produto, e somatoria do acumulador
    if sabor == 'BA' and tamanho == 'P':
        print('Você pediu um Bife Acebolado no tamanho P: R$16.00')
        acumulador = acumulador + 16

    elif sabor == 'BA' and tamanho == 'M':
        print('Você pediu um Bife Acebolado no tamanho M: R$18.00')
        acumulador = acumulador + 18

    elif sabor == 'BA' and tamanho == 'G':
        print('Você pediu um Bife Acebolado no tamanho G: R$22.00')
        acumulador = acumulador + 22

    elif sabor == 'FF' and tamanho == 'P':
        print('Você pediu um Filé de Frango no tamanho P: R$15.00')
        acumulador = acumulador + 15

    elif sabor == 'FF' and tamanho == 'M':
        print('Você pediu um Filé de Frango no tamanho M: R$17.00')
        acumulador = acumulador + 17

    else:
        print('Você pediu um Filé de Frango no tamanho G: R$21.00')
        acumulador = acumulador + 21

# se o usuario desejar mais alguma coisa, o programa continua
    maisItens = input('Deseja mais alguma coisa? (S/N): ')

    if maisItens == 'S':
        continue

    else:
        break

# exibição do valor total a ser pago pelo cliente
print(f'O valor total a ser pago é: R${acumulador:.2f}')

