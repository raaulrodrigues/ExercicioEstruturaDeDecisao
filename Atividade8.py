produto1 = float(input('Digite o valor do primeiro produto: '))
produto2 = float(input('Digite o valor do segundo produto: '))
produto3 = float(input('Digite o valor do terceiro produto: '))


if produto1 < produto2 and produto1 < produto3:
    print('\nCompre o primeiro produto, é o mais barato')
elif produto2 < produto1 and produto2 < produto3:
    print('\nCompre o segundo produto, é o mais barato')
elif produto3 < produto1 and produto3 < produto2:
    print('\nCompre o terceiro produto, é o mais barato')
else:
    print('\nO preço dos três produtos é o mesmo.')