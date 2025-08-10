#  1. Escreva um programa que mostre todos os numeros pares no intervalo de 1 a 40 de forma decrescente, utilizando o comando while.

n = 0

while n < 40:
  if n % 2 == 0:
    print(n, end= " ")
  n += 1

# 2. Escreva um programa que mostre na tela os numeros multiplos de 3 no intervalo de 2 a 100.

for n in range(2,101):
  if n % 3 == 0:
    print(n, end=' ')
  n += 1

#  3. Escreva um programa que mostre na tela os numeros primos no intervalo de 0 a 100.

for n in range(2,101):
  primo = True
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      primo = False
      break
  if primo:
    print(n, end=' ')

#  4. Leia uma sequencia de numeros, sendo que o final da sequencia sempre termina com 0. A saıda do programa e o maior numero da sequencia.

maior_numero = float('-inf')
numero = -1

while numero != 0:
    numero = int(input("Digite um número (ou 0 para encerrar): "))
    if numero != 0 and numero > maior_numero:
        maior_numero = numero

print("O maior número da sequência é:", maior_numero)

#  5. Faça um algoritmo que calcula n!

n = int(input("Digite um número inteiro positivo para calcular o fatorial: "))

if n < 0:
    print("Número invalido")
elif n == 0:
    print("O fatorial de 0 é 1.")
else:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i

    print("O fatorial de", n, "é", fatorial)

# 6. Calcula Cn,p = n!
              # p!·(n−p)!

n = int(input('Digite o número n: '))
p = int(input('Digite o número p: '))

if n < 0 or  p < 0 or p > n:
  print('Número invalido')
elif n >= 0 and p >= 0:
  fatorial = 1
  for i in range(1, n + 1):
    fatorial *= i
  fatorial2 = 1
  for i in range(1, p + 1):
    fatorial2 *= i
  fatorial_n_p = 1
  for i in range(1, (n - p) + 1):
    fatorial_n_p *= i

c = fatorial/(fatorial2 * fatorial_n_p)
print('C(', n, ',', p, ')=', c)

#  7. Dado o valor de x (float) e n (inteiro positivo), calcula s = 1 + x²/2 + x^n/n + ...

x = float(input("Digite o valor de x: "))
n = int(input("Digite o valor de n: "))

s = 1
potencia = x

for i in range(1, n + 1):
    s += potencia / i
    potencia *= x

print("O valor de s é:", s)

#  8. Dado o valor de n e de m, faca um algoritmo que calcula o valor de S:

n = int(input("Digite o valor de n: "))
m = int(input("Digite o valor de m: "))

S = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        numerador = (i ** 2) * (j ** 2)
        denominador = 2 * i + 2 * j
        S += numerador / denominador

print("O valor de S é:", S)

 # 9. Imprima a matriz identidade na tela.

matriz = []

for linha in range (3):
  linha_interna = []
  for coluna in range(3):
    if linha == coluna:
      linha_interna.append(1)
    else:
      linha_interna.append(0)
  matriz.append(linha_interna)
  for coluna in range(len(matriz[0])):
    print(matriz[linha][coluna], end=' ')
  print()

 # 10. Crie um menu de linha de comando (fica em loop ate o usuario digitar 0) com as seguintes opcoes:
 # 1. Escreve o nome do programa e do desenvolvedor;
 # 2. Imprime os numeros primos de 1 ate um numero fornecido pelo usuario;
 # 3. Le 10 numeros digitados pelo usuario e mostra o menor e o maior;
 # 4. Imprime todos os multiplos de 3 e de 5 ate um numero fornecido pelo usuario

while True:
    print("\nMenu:")
    print("1. Programa e Desenvolvedor")
    print("2. Números Primos")
    print("3. Menor e Maior de 10 Números")
    print("4. Múltiplos de 3 e 5")
    print("0. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        break
    elif opcao == 1:
        print("Nome do Programa: Menu do Brunão")
        print("Desenvolvedor: Bruno Ianoski")
    elif opcao == 2:
        limite = int(input("Digite um número limite: "))
        print("Números primos até", limite, ":")
        for num in range(2, limite + 1):
            primo = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    primo = False
                    break
            if primo:
                print(num, end=" ")
        print()
    elif opcao == 3:
        numeros = []
        for i in range(10):
            num = int(input(f"Digite o {i+1}º número: "))
            numeros.append(num)
        menor = min(numeros)
        maior = max(numeros)
        print("Menor número:", menor)
        print("Maior número:", maior)
    elif opcao == 4:
        limite = int(input("Digite um número limite: "))
        print("Múltiplos de 3 e 5 até", limite, ":")
        for num in range(1, limite + 1):
            if num % 3 == 0 and num % 5 == 0:
                print(num, end=" ")
        print()
    else:
        print("Opção inválida. Tente novamente.")