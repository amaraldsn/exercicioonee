name = input('Informe o seu nome: ')
nota1 = float(input('Informe o resultado da sua primeira prova: '))
nota2 = float(input('Informe o resultado da sua segunda prova: '))
nota3 = float(input('Informe o resultado da sua terceira prova: '))
media = (nota1+nota2+nota3)/3
print(f'Olá, {name}, a sua média é: {media:.2f}')
