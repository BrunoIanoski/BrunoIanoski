# Bibliotecas
import random
from palavras import palavra_facil, palavra_media, palavra_dificil
from palavras import forca

print('\n===========================\nBem vindo ao JOGO DA FORCA!\n===========================')

while True:
  while True:
    escolha = input('---------------------------\n1 - Fácil \n2 - Médio \n3 - Difícil\n---------------------------\nInsira a dificuldade que deseja jogar: ')
    print('\n========================================\n')
    if not escolha.isdigit():
      print('\nDificuldade Inválida! Digite apenas números.')
      continue
    escolha = int(escolha)  
    if escolha not in [1,2,3]:
      print('\nDificuldade Inválida! Tente novamente.')
    else:
      break
  if escolha == 1:
    palavra = random.choice(palavra_facil)
  elif escolha == 2:
    palavra = random.choice(palavra_media)
  elif escolha == 3:
    palavra = random.choice(palavra_dificil) 

  palavra_aleatoria = palavra
  letras_usuario = []
  chances = 4
  ganhou = False

  while True:
    for letra in palavra:
      if letra.lower() in letras_usuario:
        print(letra.upper(), end=" ")
      else:
        print("_", end=" ")
    print("\n\nLetras já escolhidas:", " ".join(sorted(letras_usuario)).upper())
    print()
    print(forca[4 - chances])
    print(f"\nVocê tem {chances} chances restantes.\n-----------------------------")
    print()
    while True:
      tentativa = input('---------------------------------\nEscolha uma letra para adivinhar: ').strip().lower()
      print()
      if len(tentativa) != 1 or not tentativa.isalpha():
        print('\nEntrada inválida! Digite apenas UMA letra.\n⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
        print()
      elif tentativa in letras_usuario:
        print('\nEscolha outra letra...\n⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
        print()
      else:
        letras_usuario.append(tentativa.lower())
        break
    if tentativa.lower() not in palavra.lower():
      chances -= 1
    ganhou = True
    for letra in palavra:
      if letra.lower() not in letras_usuario:
        ganhou = False
    if chances == 0 or ganhou:
      break
  if ganhou:
    print(f"\n\n_____________________\n=====================\n\n    VOCÊ VENCEU!😎\n\nA palavra era {palavra.upper()}.\n\n_____________________\n=====================")
    print()
  else:
    print(forca[4])
    print(f'\n\n_____________________\n=====================\n\n    VOCÊ PERDEU!💀\n\nA palavra era {palavra.upper()}.\n\n_____________________\n=====================')
    print()
  reiniciar = input('\nDeseja jogar novamente? (s/n): ').strip().lower()
  if reiniciar != 's':
    print('-------------\n|Fim de jogo|\n-------------')
    break
