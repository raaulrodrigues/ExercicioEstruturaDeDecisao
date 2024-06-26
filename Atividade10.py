turno = input('Digite qual é seu turno: \n[M] para matutino \n[V] para vespertino \n[N] para noturno')


if turno == 'M' or turno == 'm':
    print('Bom dia.')
elif turno == 'V' or turno == 'v':
    print('Boa tarde.')
elif turno == 'N' or turno == 'n':
    print('Boa noite.')
else:
    print('Nenhuma opção válida.')