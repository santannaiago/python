print("olá, eu sou a sua calculadora de prompt de comando (:")
modo = input("Digite soma, subtração, multiplicação, divisão, exponenciação ou módulo: ")

def soma(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    return x / y

def exponenciacao(x,y):
    return x ** y

def modulo(x,y):
    return x // y

if modo == "soma":
    print("~SOMA~")
    x = float(input("digite o primeiro número:"))
    y = float(input("Digite o segundo número:"))
    result = soma(x,y)
    print(f"{x} + {y} = {result}")
elif modo == "subtração":
    print("~SUBTRAÇÃO~")
    x = float(input("digite o primeiro número:"))
    y = float(input("Digite o segundo número:"))
    result = subtracao(x,y)
    print(f"{x} - {y} = {result}")
elif modo == "multiplicação":
    print("~MULTIPLICAÇÃO~")
    x = float(input("digite o primeiro número:"))
    y = float(input("Digite o segundo número:"))
    result = multiplicacao(x,y)
    print(f"{x} * {y} = {result}")
elif modo == "divisão":
    print("~DIVISÃO~")
    x = float(input("digite o primeiro número:"))
    y = float(input("Digite o segundo número:"))
    result = divisao(x,y)
    print(f"{x} / {y} = {result}")
elif modo == "exponenciação":
    print("~EXPONENCIAÇÃO~")
    x = float(input("digite o primeiro número:"))
    y = float(input("Digite o segundo número:"))
    result = exponenciacao(x,y)
    print(f"{x} ** {y} = {result}")
elif modo == "módulo":
    print("~MÓDULO~")
    x = float(input("digite o primeiro número:"))
    y = float(input("Digite o segundo número:"))
    result = modulo(x,y)
    print(f"{x} // {y} = {result}")
else:
    print("Por favor, digite um valor válido")