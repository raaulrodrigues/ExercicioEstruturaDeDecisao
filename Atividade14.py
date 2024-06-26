nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print('\nMédia de Aproveitamento  Conceito')

if media > 9 and media <= 10:
    print('Entre 9.0 e 10.0         A')
    print('Aprovado!')
elif media > 7.5 and media < 9.0:
    print('Entre 7.5 e 9.0         B')
    print('Aprovado!')
elif media > 6.0 and media < 7.5:
    print('Entre 6.0 e 7.5         C')
    print('Aprovado!')
elif media > 4.0 and media < 6.0:
    print('Entre 4.0 e 6.0         D')
    print('Reprovado!')
else:
    print('Entre 4.0 e 0.0         E')
    print('Reprovado!')