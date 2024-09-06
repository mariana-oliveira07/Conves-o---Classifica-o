'''
Questão 3: Implementar um Conversor de Temperaturas com Loop
Escreva uma função chamada conversor_temperatura que recebe dois argumentos: um número (temperatura) e uma string representando a unidade de conversão (unidade). 
A função deve retornar o resultado da conversão da temperatura para a unidade especificada. As unidades suportadas são:

    "CtoF" para converter de Celsius para Fahrenheit
    "FtoC" para converter de Fahrenheit para Celsius
    "CtoK" para converter de Celsius para Kelvin
    "KtoC" para converter de Kelvin para Celsius
    "FtoK" para converter de Fahrenheit para Kelvin
    "KtoF" para converter de Kelvin para Fahrenheit

A função deve lidar com entradas inválidas e retornar uma mensagem apropriada nesses casos.

Segue um trecho mostrando como deve ser implementada a função:
    def conversor_temperatura(temperatura, unidade):
        if unidade == "CtoF":
            return (temperatura * 9/5) + 32


Na entrada dos números deve ser feito o tratamento de exceções, para que seja tratado os casos que não sejam digitados números.

O programa deve ficar em loop, solicitando ao usuário os valores e a unidade de conversão até que o usuário digite s para sair.

As temperaturas convertidas devem ser armazenadas em uma lista e depois de encerrar, mostrar a lista, a maior temperatura, a menor temperatura e a média das temperaturas convertidas.

# Exemplo de uso:
# Input: 100 "CtoF"
# Output: 212.0

# Input: 32 "FtoC"
# Output: 0.0

# Teste a função
print(conversor_temperatura(100, "CtoF"))   # Saída esperada: 212.0
print(conversor_temperatura(32, "FtoC"))    # Saída esperada: 0.0
print(conversor_temperatura(0, "CtoK"))     # Saída esperada: 273.15
print(conversor_temperatura(273.15, "KtoC"))# Saída esperada: 0.0
print(conversor_temperatura(32, "FtoK"))    # Saída esperada: 273.15
print(conversor_temperatura(273.15, "KtoF"))# Saída esperada: 32.0

'''

def conversor_temperatura(temperatura, unidade):
    if unidade == "CtoF":
        return (temperatura * 9/5) + 32
    elif unidade == "FtoC":
        return (temperatura - 32) * 5/9
    elif unidade == "CtoK":
        return temperatura + 273.15
    elif unidade == "KtoC":
        return temperatura - 273.15
    elif unidade == "FtoK":
        return (temperatura - 32) * 5/9 + 273.15
    elif unidade == "KtoF":
        return (temperatura - 273.15) * 9/5 + 32
    else:
        return "Unidade inválida."

temperaturas_convertidas = []

while True:
    sair = input("Digite 's' para sair ou Enter para continuar: ").strip().upper()
    if sair == 'S':
        break
    
    temperatura = float(input("Digite a temperatura: "))
    
    print("Escolha a unidade de conversão:")
    print("1. Celsius para Fahrenheit (CtoF)")
    print("2. Fahrenheit para Celsius (FtoC)")
    print("3. Celsius para Kelvin (CtoK)")
    print("4. Kelvin para Celsius (KtoC)")
    print("5. Fahrenheit para Kelvin (FtoK)")
    print("6. Kelvin para Fahrenheit (KtoF)")
    
    escolha = input("Digite o número da opção desejada: ").strip()
    
    unidades = {
        "1": "CtoF",
        "2": "FtoC",
        "3": "CtoK",
        "4": "KtoC",
        "5": "FtoK",
        "6": "KtoF"
    }
    
    unidade = unidades.get(escolha, "Unidade inválida.")
    
    resultado = conversor_temperatura(temperatura, unidade)
    
    if resultado == "Unidade inválida.":
        print(resultado)
    else:
        print(f"A temperatura convertida é: {resultado}")
        temperaturas_convertidas.append(resultado)

if temperaturas_convertidas:
    maior = max(temperaturas_convertidas)
    menor = min(temperaturas_convertidas)
    media = sum(temperaturas_convertidas) / len(temperaturas_convertidas)
    
    print("\nTemperaturas convertidas:", temperaturas_convertidas)
    print(f"Maior temperatura: {maior}")
    print(f"Menor temperatura: {menor}")
    print(f"Média das temperaturas: {media}")
else:
    print("Nenhuma temperatura foi convertida.")