lado1 = int(input('Digite o valor do primeiro lado: '))
lado2 = int(input('Digite o valor do segundo lado: '))
lado3 = int(input('Digite o valor do terceiro lado: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('\nPode ser um triângulo')

    if lado1 == lado2 == lado3:
        print('É um triângulo Equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('É um triângulo Isósceles')
    else:
        print('É um triângulo Escaleno')
else:
    print('Não pode ser um triângulo.')
