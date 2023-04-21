# criando as variaveis
num1 = float(input("primeiro número: "))
num2 = float(input("segundo número: "))
simbolos = (input("+ - * / ^: "))

# Dar a resposta de acordo com o simbolo matemático
if simbolos == "+":
    print(num1+num2)
elif simbolos == "-":
    print(num1-num2)
elif simbolos == "*":
    print(num1*num2)
elif simbolos == "/":
    if num2 == 0:
        print("não é possível dividir por zero")
    else:
        print(num1 / num2)
elif simbolos == "^":
    print(num1^num2)
input()
