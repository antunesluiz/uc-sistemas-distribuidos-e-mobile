nome = ''
idade = 0
salario = 0
sexo = 'f'
estado_civil = 's'

while 'true':
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    salario = float(input('Digite seu salário: '))
    sexo = input('Digite seu sexo f ou m: ')
    estado_civil = input('Digite seu estado civil s, c, v, d: ')

    if ((len(nome) > 3) and (idade > 0 or idade < 150) and (salario > 0) and (sexo == 'f' or sexo == 'm') and (estado_civil in 'scvd')):
        break
    else:
        print('Digitou tudo errado')

print('digitou certo')
