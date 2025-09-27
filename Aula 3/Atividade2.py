nomeAtleta = input("Digite o nome do atleta: ")
notas = []

# Cria um loop que vai se repetir 7 vezes.
for i in range(7):
# variável i começa em 0 e vai até 6 
#Mostra na tela a Nota 1 até Nota 7
    nota = float(input(f"Nota {i+1}: "))
#diciona número no final da lista notas.
    
    notas.append(nota)



# Eliminando melhor e pior nota
melhor_nota = max(notas)
pior_nota = min(notas)

notas.remove(melhor_nota)
notas.remove(pior_nota)

# Calculando média 
media = sum(notas) / len(notas)
print("atleta:",nomeAtleta)
print("Notas:", notas)
print("Melhor nota eliminada:", melhor_nota)
print("Pior nota eliminada:", pior_nota)
print("Média das notas:", media)

    