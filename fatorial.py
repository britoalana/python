numero = int(input("Digite um número: "))

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado
    

if numero < 0:
 print("Digite um número inteiro não negativo")

else:
   print(f"O fatorial de {numero} é {fatorial(numero)}")
   