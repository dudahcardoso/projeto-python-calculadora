def somar(a, b):
    return a + b  # Retorna a soma de a e b

def subtrair(a, b):
    return a - b  # Retorna a subtração de a por b

def multiplicar(a, b):
    return a * b  # Retorna a multiplicação de a por b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"  # Evita divisão por zero
    return a / b  # Retorna a divisão de a por b

def main():
    print("Calculadora Simples")  # Exibe o título
    print("Operações disponíveis: +, -, *, /")  # Mostra as operações
    a = float(input("Digite o primeiro número: "))  # Lê o primeiro número
    op = input("Digite a operação (+, -, *, /): ")  # Lê a operação
    b = float(input("Digite o segundo número: "))  # Lê o segundo número

    # Verifica qual operação foi escolhida e executa
    if op == "+":
        resultado = somar(a, b)
    elif op == "-":
        resultado = subtrair(a, b)
    elif op == "*":
        resultado = multiplicar(a, b)
    elif op == "/":
        resultado = dividir(a, b)
    else:
        resultado = "Operação inválida"  # Caso a operação não seja reconhecida

    print("Resultado:", resultado)  # Exibe o resultado

if __name__ == "__main__":
    main()  # Executa a função principal se o arquivo for executado diretamente