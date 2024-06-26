vogal = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')

letra = input('Digite uma letra: ')

if letra in vogal:
    print('A letra escolhida é vogal.')
else:
    print('A letra digitada é consoante.')