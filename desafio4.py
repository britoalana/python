notas = [7.5, 6.0, 9.0, 8.5, 10.0]
nomes = ["João", "Maria", "Pedro", "Ana", "Lucas"]

print("\nNotas dos alunos:\n")
for nome, nota in zip (nomes, notas):
    print(f'{nome}: {nota}')

media = sum(notas) / len(notas) 
print(f"\nMédia das notas: {media :.2f}")

maior_nota = max(notas)
melhor = [nomes[i] for i, nota in enumerate(notas) if nota == maior_nota]
print(f"\n{' '.join(melhor)} tirou a melhor nota {maior_nota}\n")
