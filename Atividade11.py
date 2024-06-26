salario = int(input("Digite o seu salário: "))

if salario <= 280:
    taxa = salario * 0.20
    percentual = 20

elif salario > 280 and salario < 700:
    taxa = salario * 0.15
    percentual = 15

elif salario > 700 and salario < 1500:
    taxa = salario * 0.10
    percentual = 10

else:
    taxa = salario * 0.05
    percentual = 5

salarioAtualizado = (salario + taxa)

print("O seu salário antes:", salario)
print('O aumento no seu salario será de:', percentual, '%')
print('O valor aumentado é de:', taxa)
print('Seu novo salário com aumento é de:', salarioAtualizado)
