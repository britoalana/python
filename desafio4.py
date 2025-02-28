notas = [7.5, 6.0, 9.0, 8.5, 10.0]
nomes = ["João", "Maria", "Pedro", "Ana", "Lucas"]

print("Notas dos alunos:")

media = sum(notas) / len(notas) 
print(f"Média das notas: {media :.2f}")

maiornota = max(notas)
print(f"Tirou a melhor nota {maiornota}")