# aula em 20 de jun 2024 as 11:08
'''print(int('1'), type(int('1')))
print(type(float('1')+1))
print(bool(' '))
print(str(11)+ 'b')
'''

# exercicios
nome = 'luis'
sobrenome = 'Orlando'
idade = 45
ano_nascimento = 2024 - idade
maior_de_idade = idade >= 18
altura_metros = 1.75


print ('Nome: ', nome)
print ('Sobrenome: ', sobrenome)
print ('Idade: ', idade)
print ('Ano do nascimento: ', ano_nascimento)
print (' É maior de idade? ', maior_de_idade)
print ('Altura em metros: ', altura_metros)

adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)

concatenacao = 'Luiz' + ' ' + 'Otávio'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_luiz = 3 * 'Luiz'
print(a_dez_vezes)
print(tres_vezes_luiz)