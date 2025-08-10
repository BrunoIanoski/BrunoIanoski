# Desenvolva um programa que solicite o nome e a pontuação de 10 participantes de um evento esportivo e, ao final, apresente o nome do vencedor.

n = 10
nome = [""]*n
pontuacao = [0]*n
for i in range(0,n):
  nome[i] = input('Digite o nome do participante: ')
  pontuacao[i] = int(input('Digite a pontuação: '))
  nome.append(nome)
  pontuacao.append(pontuacao)
vencedor = 0
maior_pontuacao = pontuacao[0]
for i in range(0,n):
  if pontuacao[i] > maior_pontuacao:
    maior_pontuacao = pontuacao[i]
    vencedor = i
print(f"O vencedor é {nome[vencedor]} com {pontuacao[vencedor]} pontos!")

# Crie um programa que leia um vetor de inteiros, gere um novo vetor com os elementos na 
# ordem inversa (ou seja, o último elemento passa a ser o primeiro, o penúltimo o segundo, e assim por diante) e exiba o vetor invertido.

q = int(input('Informe a quantidade de números que deseja insirir: '))
inteiros = []
for i in range (q):
  num = int(input('Insira os números que deseja: '))
  inteiros.append(num)
  inteiros_invertido = inteiros[::-1]
print(inteiros_invertido)

# Elabore um programa que leia um vetor v1 de números em ponto flutuante e construa um 
# segundo vetor v2 da seguinte maneira: para índices pares, atribua o valor correspondente 
# de v1 multiplicado por 2; para índices ímpares, atribua o valor de v1 dividido por 2. Ao final, o programa deverá mostrar ambos os vetores.

vetor1 = []
vetor2 = []
for i in range (5):
  v1 = float(input('Insira os números que deseja: '))
  vetor1.append(v1)
  if v1 % 2 == 0:
    multi = v1*2
    vetor2.append(multi)
  if v1 % 2 != 0:
    div = v1/2
    vetor2.append(div)
print(vetor2)
print(vetor1)


# Desenvolva um programa que leia um vetor de inteiros fornecido pelo usuário, ordene-o em ordem crescente e exiba o resultado na tela

crescente = []
for i in range(5):
  num = int(input('Insira os números inteiros: '))
  crescente.append(num)
  crescente.sort()
print(crescente)


# Implemente um programa que, dado um vetor de inteiros, reorganize-o de forma que os elementos nas posicões pares sejam ordenados de maneira crescente, enquanto os
# elementos nas posições ímpares fiquem em ordem decrescente.

crescente = []
decrescente = []
for i in range(6):
  num = int(input('Insira os números inteiros: '))
  if num % 2 == 0:
    crescente.append(num)
    crescente.sort()
  if num % 2 != 0:
    decrescente.append(num)
    decrescente.sort(reverse=True)
lista = crescente + decrescente
print(lista)

# Crie um programa que leia um vetor de inteiros e um número inteiro; o programa deverá localizar e imprimir o índice em que o número se encontra no vetor.

vetor1 = []
vetor2 = []
for i in range(5):
  num = int(input('Insira os números inteiro: '))
  vetor1.append(num)
for i in range(1):
  num2 = int(input('Insira o número que deseja localizar: '))
  vetor2.append(num2)
  if num2 in vetor1:
    indice = vetor1.index(num2)
    print(f"O número está localizado no índice: {indice}")
  else:
    print('O número não foi localizado no vetor.')

# Desenvolva um programa que leia um vetor de strings contendo nomes de pessoas, solicite que o usuário digite um nome e informe se esse nome está presente no vetor

nomes = []
for i in range(4):
  nome = str(input('Insira os nomes das pessoas: '))
  nomes.append(nome)
for i in range(1):
  local = str(input('Insira o nome que deseja localizar: '))
  if local in nomes:
    print('O nome pertence ao vetor!')
  else:
    print('O nome não pertence ao vetor.')

# Implemente um programa que leia um vetor de strings com nomes de pessoas e exiba-os em ordem alfabética. Neste exercício, você não deve ordenar o vetor de strings
# diretamente, mas sim utilizar um vetor de inteiros que referencia as posições do vetor original para produzir a saída ordenada

nomes = []
posicao = []
for i in range(0,5):
  nome = str(input('Insira os nomes das pessoas: '))
  nomes.append([nome,i])
  nomes.sort()
  posicao.append(i)
# posicao_ordenada = sorted(posicao, key=lambda x: nomes[x])

print("Lista de posições ordenadas:", nomes)
