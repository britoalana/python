num = int(input("Digite um número inteiro positivo: "))

if num < 0:
    print("Por favor, digite um número positivo.")

else:
 for i in range (num, -1, -2):
    print(i)