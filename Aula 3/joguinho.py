import os
# JOGO DA PALAVRA
palavra_secreta = "cachorro"
dica = "Um animal peludo"
tentativas = 5

# Recebendo nomes dos jogadores
jogador1 = input("Jogador 1, digite seu nome: ")
jogador2 = input("Jogador 2, digite seu nome: ")
vencedor = jogador1

print("Bem-vindos ao jogo de adivinhação!")
print("A dica da palavra é:", dica)

# Loop de tentativas f"Tentativa {i+1}/{tentativas} - {jogador2},
for i in range(tentativas):
    resposta = input("adivinhe a palavra: ")

    if resposta == palavra_secreta:
        print("Você acertou!!")
        break
    else:
        print("Tente novamente")
        
if resposta != palavra_secreta:
    print("Acabaram as tentativas!")
    print("A palavra era:", palavra_secreta)
    vencedor = jogador1
    print(f'O vencedor foi: {vencedor}')