'''
Questão 2: Escreva uma função chamada determinar_fase_da_vida que recebe um número inteiro representando a idade de uma pessoa e 
retorna uma string que classifica a pessoa em uma das seguintes fases da vida:

1- "Infância" se a idade for menor que 3 anos.
2- "Pré-adolescência" se a idade for entre 3 e 12 anos.
3- "Adolescência" se a idade for entre 13 e 19 anos.
4- "Juventude" se a idade for entre 20 e 35 anos.
5- "Meia-idade" se a idade for entre 36 e 55 anos.
6- "Terceira idade" se a idade for 56 anos ou mais.

# Teste a função
print(determinar_fase_da_vida(2))   # Saída esperada: Infância
print(determinar_fase_da_vida(10))  # Saída esperada: Pré-adolescência
print(determinar_fase_da_vida(16))  # Saída esperada: Adolescência
print(determinar_fase_da_vida(25))  # Saída esperada: Juventude
print(determinar_fase_da_vida(40))  # Saída esperada: Meia-idade
print(determinar_fase_da_vida(60))  # Saída esperada: Terceira idade

'''
idade = int(input('Digite a idade: '))


def determinar_fase_da_vida(idade):
    if idade < 3:
        print("Infância")
    elif 3 <= idade <= 12:
        print("Pré-adolescência")
    elif 13 <= idade <= 19:
        print("Adolescência")
    elif 20 <= idade <= 35:
        print("Juventude")
    elif 36 <= idade <= 55:
        print("Meia-idade")
    else:
        print("Terceira idade")