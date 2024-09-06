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
        print(conversor_temperatura(100, "CtoF"))   
    elif unidade == "FtoC":
        print(conversor_temperatura(32, "FtoC"))   
    elif unidade == "CtoK":
        print(conversor_temperatura(0, "CtoK"))     
    elif unidade == "KtoC":
        print(conversor_temperatura(273.15, "KtoC"))
    elif unidade == "FtoK":
        print(conversor_temperatura(32, "FtoK"))   
    elif unidade == "KtoF":
        print(conversor_temperatura(273.15, "KtoF"))
    else:
        return "Unidade inválida. As unidades válidas são: CtoF, FtoC, CtoK, KtoC, FtoK, KtoF."

def menu():
    print("\nEscolha o tipo de conversão:")
    print("1. Celsius para Fahrenheit (CtoF)")
    print("2. Fahrenheit para Celsius (FtoC)")
    print("3. Celsius para Kelvin (CtoK)")
    print("4. Kelvin para Celsius (KtoC)")
    print("5. Fahrenheit para Kelvin (FtoK)")
    print("6. Kelvin para Fahrenheit (KtoF)")
    print("s. Sair")

def escolha_unidade(opcao):
    if opcao == "1":
        return "CtoF"
    elif opcao == "2":
        return "FtoC"
    elif opcao == "3":
        return "CtoK"
    elif opcao == "4":
        return "KtoC"
    elif opcao == "5":
        return "FtoK"
    elif opcao == "6":
        return "KtoF"
    else:
        return None

def main():
    temperaturas = []

    while True:
        menu()
        opcao = input("Digite a opção desejada: ")

        if opcao.lower() == 's':
            break

        unidade = escolha_unidade(opcao)
        if unidade is None:
            print("Opção inválida, tente novamente.")
            continue

        try:
            temperatura = float(input("Digite a temperatura a ser convertida: "))
            resultado = conversor_temperatura(temperatura, unidade)

            if isinstance(resultado, str):
                print(resultado) 
            else:
                temperaturas.append(resultado)
                print(f"Temperatura convertida: {resultado}")
        except ValueError:
            print("Entrada inválida. Digite um número para a temperatura.")
        except Exception as e:
            print(f"Erro: {e}")

    if temperaturas:
        maior = max(temperaturas)
        menor = min(temperaturas)
        media = sum(temperaturas) / len(temperaturas)

        print("\nLista de temperaturas convertidas:", temperaturas)
        print(f"Maior temperatura convertida: {maior}")
        print(f"Menor temperatura convertida: {menor}")
        print(f"Média das temperaturas convertidas: {media:.2f}")

if __name__ == "__main__":
    main()