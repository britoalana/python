#Alana Beatriz da Silva Brito
print("Bem-vindo à calculadora simples!")
print("Operações disponíveis:")
print("+ : Adição")
print("- : Subtração")
print("* : Multiplicação")
print("/ : Divisão")

operacao = input("Escolha a operação (+, -, *, /): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == "+":
  soma = num1 + num2
  print(f"O resultado de {num1} + {num2} é {soma}")

elif operacao == "-":
  sub = num1 - num2
  print(f"O resultado de {num1} - {num2} é {sub}")

elif operacao == "*":
  mult = num1 * num2
  print(f"O resultado de {num1} * {num2} é {mult}")

elif operacao == "/":
  if num1 == 0 or num2 == 0:
     print("Digite um número válido")
  else:
    div = num1 / num2
    print(f"O resultado de {num1} / {num2} é {div:.2f}")  