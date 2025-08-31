# parte 1

# mensagem de boas-vindas
print('Bem vindo(a) ao app de vendas! Desenvolvido por Ghabryella Miranda dos Santos.\n')

# entrada de dados
valorDoPedido = float(input('Entre com o valor do pedido: R$'))
quantidadeDeParcelas = int(input('Entre com a quantidade de parcelas: '))

# cálculo da taxa de juros de acordo com a quantidade de parcelas
if quantidadeDeParcelas < 4:
    juros = 0 / 100

elif quantidadeDeParcelas >= 4 and quantidadeDeParcelas < 6:
    juros = 4 / 100

elif quantidadeDeParcelas >= 6 and quantidadeDeParcelas < 9:
    juros = 8 / 100

elif quantidadeDeParcelas >= 9 and quantidadeDeParcelas < 13:
    juros = 16 / 100

else:
    juros = 32 / 100


# cálculo do valor da parcela
valorDaParcela = valorDoPedido * (1 + juros) / quantidadeDeParcelas

# cálculo do valor total parcelado
valorTotalParcelado = valorDaParcela * quantidadeDeParcelas

# exibição dos resultados
print(f'O valor das parcelas é de: R${valorDaParcela:.2f}')
print(f'Valor total parcelado é de: R${valorTotalParcelado:.2f}')
