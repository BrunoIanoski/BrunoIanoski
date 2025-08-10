# 1. Escreva um programa que verifique se um numero digitado pelo usuário é menor, igual ou maior que zero.

numero = int(input('Insira um número inteiro: '))
if numero > 0:
  print('O número é maior que zero.')
elif numero == 0:
  print('O número é igual a zero')
else:
  print('O número é menor que zero')

# 2. Faça um algoritmo que recebe como entrada dois numeros reais a, b. A saída deve ser estes numeros em ordem crescente.

n1 = int(input('Insira o número A: '))
n2 = int(input('Insira o número B: '))

if n1 < n2:
  print(n1,n2)
elif n1 > n2:
  print(n2,n1)
else:
  print(n1,n2)

# 3. Faça um algoritmo que recebe como entrada tres números reais a, b, c. Na saída deve informar se a soma de a + b e maior que c.

n1 = int(input('Insira o número A: '))
n2 = int(input('Insira o número B: '))
n3 = int(input('Insira o número C: '))

if n1 + n2 > n3:
  print('A soma de A + B é maior que C.')
elif n1 + n2 == n3:
  print('A soma é igual a C.')
else:
  print('A soma não é maior.')

# 4. Faça um algoritmo que recebe como entrada tres notas de prova de uma disciplina a, b, c.Na saída deve informar a media e se o aluno esta aprovado ou reprovado (aprovado média
# maior que 70). Se o aluno foi reprovado ou esta de exeme o algoritmo deve informar tambem a menor dentre as três notas.

n1 = int(input('Insira a nota A: '))
n2 = int(input('Insira a nota B: '))
n3 = int(input('Insira a nota C: '))

media = (n1+n2+n3)/3

if media >= 70:
  print('O aluno está aprovado!')
elif media > 40 and media < 70:
  print('O aluno está de exame.')
else:
  print('O aluno está reprovado')

if media < 70:
  if n1 < n2 and n1 < n3:
    print(f'A menor nota é: {n1}')
  elif n2 < n1 and n2 < n3:
    print(f'A menor nota é: {n2}')
  else:
    print(f'A menor nota é: {n3}')

print(f'A média do aluno é: {round(media,2)}')

# 5. Faça um algoritmo que retorna se um determinado numero é Impar ou Par e Positivo ou Negativo. Se ele for Impar o algoritmo tambem deve verificar se o número é divisivel por 3.

n = int(input('Insira um número inteiro: '))

if n % 2 == 0:
  print('O número é Par.')
elif n % 2 != 0:
  print('O número é Impar.')

if n >= 0:
  print('O número é Positivo')
else:
  print('O número é Negativo')

if n % 2 != 0:
  if n % 3 == 0:
    print('O número é divisivel por 3.')

# 6. Dados tres valores x, y e z, verificar se eles podem ser lados de um triangulo. Se eles forem lados de um triangulo, verificar se é um triangulo equilatero, isosceles ou escalenos.
# Informar tambem se os tres valores nao formam um triangulo.
# Probriedades de um triangulo:
# • O comprimento de um lado de um triangulo é sempre menor que a soma dos outros dois lados;
# • Triangulo Equilatero: os tres lados iguais;
# • Triangulo Isosceles: tem dois lados iguais;
# • Triangulo Escaleno: tem tres lados diferentes.

x = int(input('Insira o lado A: '))
y = int(input('Insira o lado B: '))
z = int(input('Insira o lado C: '))

if x < y + z and y < x + z and z < x + y:
  print('Os valores podem ser lados de um triângulo.')
  if x == y == z:
    print('O triângulo é equilatero.')
  elif x == y or x == z or y == z:
    print('O triângulo é isosceles.')
  else:
    print('O triângulo é escaleno')
else:
  print('Os valores não podem ser lados de um triângulo')

# 7. Escreva um algoritmo que le um numero e informe se ele e divisıvel por 10, por 7, por 5, ou por 2 ou se nao e divisıvel por nenhum deles.

n = int(input('Insira um número inteiro: '))

divisivel = False

if n % 10 == 0:
  print('O número é divisível por 10')
  divisivel = True
if n % 7 == 0:
  print('O número é divisível por 7')
  divisivel = True
if n % 5 == 0:
  print('O número é divisível por 5')
  divisivel = True
if n % 2 == 0:
  print('O número é divisível por 2')
  divisivel = True
if not divisivel:
  print('Não é divisível por nenhum dos números.')

# 8. Faça um algoritmo que verifica a qual intervalo a seguir um número informado pelo usuário pertence:
# • [100, 500];
# • [200, 400];
# • [400, 600];
# • [501, 1000];
# • não pertence a nenhum intervalo dos anteriores.

n = int(input('Insira um número inteiro: '))

if n >= 100 and n <= 1000:
    if n >= 100 and n <= 500:
      print('O número pertence ao intervalo 100 a 500.')
    if n >= 200 and n <= 400:
      print('O número pertence ao intervalo 200 a 400.')
    if n > 400 and n <= 600:
      print('O número pertence ao intervalo 400 a 600.')
    if n >= 501 and n <= 1000:
      print('O número pertence ao intervalo 501 a 1000.')
else:
  print('O número não pertence a nenhum intervalo.')

# 9. Elabore um algoritmo que le 5 valores inteiros e apresente na tela o maior e o menor dentre eles.

numeros = []

for numero in range(5):
  n =  int(input('Insira um valor inteiro: '))
  numeros.append(n)
numeros.sort(reverse=True)
print(numeros[0])
numeros.sort()
print(numeros[0])

# Ou

numeros2 = []

for i in range(5):
  n2 =  int(input('Insira um valor inteiro: '))
  numeros2.append(n2)

maior = numeros2[0]
menor = numeros2[0]

for i in range(1, len(numeros2)):
  if numeros2[i] > maior:
    maior = numeros2[i]
  if numeros2[i] < menor:
    menor = numeros2[i]

print(f'O maior é {maior} e o menor é {menor}')

# 10. Elabore um algoritmo que le 5 valores inteiros e apresente na tela estes valores em ordem crescente.

numeros = []

for i in range(5):
  n = int(input('Insira um valor inteiro: '))
  numeros.append(n)

for i in range(len(numeros)):
  for j in range(i + 1, len(numeros)):
    if numeros[i] > numeros[j]:
      temp = numeros[i]
      numeros[i] = numeros[j]
      numeros[j] = temp

print("Números em ordem crescente:", numeros)

# 11. Elabore um algoritmo que le 5 valores inteiros e apresente na tela estes valores em ordem crescente e em ordem decrescente.

numeros = []

for i in range(5):
  n = int(input('Insira um valor inteiro: '))
  numeros.append(n)

for i in range(len(numeros)):
  for j in range(i + 1, len(numeros)):
    if numeros[i] > numeros[j]:
      temp = numeros[i]
      numeros[i] = numeros[j]
      numeros[j] = temp

numeros2 = []

for i in range(5):
  n = int(input('Insira um valor inteiro: '))
  numeros2.append(n)

for i in range(len(numeros2)):
  for j in range(i + 1, len(numeros2)):
    if numeros2[i] < numeros2[j]:
      temp = numeros2[i]
      numeros2[i] = numeros2[j]
      numeros2[j] = temp

print("Números em ordem crescente:", numeros)

print("Números em ordem decrescente:", numeros2)

# 12. Escrever um algoritmo que le um valor em reais (dinheiro) e calcula qual o menor numero possıvel de notas de 100, 50, 20, 10, 5, 2 e 1 em que o valor lido pode ser
# decomposto. A saıdas deve ser a quantidade de cada nota que sera necessaria.

valor = int(input("Digite um valor em reais: "))

notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
notas_1 = 0

if valor >= 100:
    notas_100 = valor // 100
    valor %= 100

if valor >= 50:
    notas_50 = valor // 50
    valor %= 50

if valor >= 20:
    notas_20 = valor // 20
    valor %= 20

if valor >= 10:
    notas_10 = valor // 10
    valor %= 10

if valor >= 5:
    notas_5 = valor // 5
    valor %= 5

if valor >= 2:
    notas_2 = valor // 2
    valor %= 2

if valor >= 1:
    notas_1 = valor

print("Notas:")
if notas_100 > 0:
    print(f"{notas_100} nota(s) de R$ 100")
if notas_50 > 0:
    print(f"{notas_50} nota(s) de R$ 50")
if notas_20 > 0:
    print(f"{notas_20} nota(s) de R$ 20")
if notas_10 > 0:
    print(f"{notas_10} nota(s) de R$ 10")
if notas_5 > 0:
    print(f"{notas_5} nota(s) de R$ 5")
if notas_2 > 0:
    print(f"{notas_2} nota(s) de R$ 2")
if notas_1 > 0:
    print(f"{notas_1} nota(s) de R$ 1")

# 13. Ler uma nota numerica (numero real) codificada entre 0 e 10. Em seguida converta essa nota para a correspondente em conceito, segundo os itens abaixo.
# • A = acima ou igual a 9.0
# • B = inferior a 9.0 e superior ou igual a 7.0
# • C = inferior a 7.0 e superior ou igual a 5.0
# • D = inferior a 5.0 e superior ou igual a 2.5
# • E = Inferior a 2.5

n = float(input('Insira um número real até 10: '))

if n >= 0 and n <=10:
  if n >= 9:
    print('A nota é A')
  elif n < 9 and n >= 7:
    print('A nota é B')
  elif n < 7 and n >= 5:
    print('A nota é C')
  elif n < 5 and n>= 2.5:
    print('A nota é D')
  elif n < 2.5:
    print('A nota é E')
else:
  print('Número invalido')

# 14. Construir um programa que faz a leitura de tres numeros inteiros, representando uma data (dd, mm, aaaa). E, utilizando o comando de selecao, para a escolha do mes,
# imprime a data, onde o mes e escrito por extenso. Exemplo: leitura da data: 31 3 2011; impressao: 31 de marco de 2011

mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril' , 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

data = []

for i in range(3):
  datas = int(input('Insira a data (dia)(mes)(ano): '))
  data.append(datas)

if data[1] == 1:
  print(f'{data[0]} de {mes[0]} de {data[2]}')
elif data[1] == 2:
  print(f'{data[0]} de {mes[1]} de {data[2]}')
elif data[1] == 3:
  print(f'{data[0]} de {mes[2]} de {data[2]}')
elif data[1] == 4:
  print(f'{data[0]} de {mes[3]} de {data[2]}')
elif data[1] == 5:
  print(f'{data[0]} de {mes[4]} de {data[2]}')
elif data[1] == 6:
  print(f'{data[0]} de {mes[5]} de {data[2]}')
elif data[1] == 7:
  print(f'{data[0]} de {mes[6]} de {data[2]}')
elif data[1] == 8:
  print(f'{data[0]} de {mes[7]} de {data[2]}')
elif data[1] == 9:
  print(f'{data[0]} de {mes[8]} de {data[2]}')
elif data[1] == 10:
  print(f'{data[0]} de {mes[9]} de {data[2]}')
elif data[1] == 11:
  print(f'{data[0]} de {mes[10]} de {data[2]}')
elif data[1] == 12:
  print(f'{data[0]} de {mes[11]} de {data[2]}')
else:
  print('Data invalida')



# 15. Construir um programa que faz a leitura de um numero de apenas um dıgito: de 0 a 9. Utilizando o comando if, imprima o numero por extenso. Exemplo: leitura do numero 5, imprimir CINCO.

numero = ['ZERO','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE','OITO','NOVE']

n = int(input('Insira um número de 0 a 9: '))

if n >= 0 and n <=9:
  if n == 0:
    print(numero[0])
  elif n == 1:
    print(numero[1])
  elif n == 2:
    print(numero[2])
  elif n == 3:
    print(numero[3])
  elif n == 4:
    print(numero[4])
  elif n == 5:
    print(numero[5])
  elif n == 6:
    print(numero[6])
  elif n == 7:
    print(numero[7])
  elif n == 8:
    print(numero[8])
  elif n == 9:
    print(numero[9])
else:
  print('Número invalido')

# 16. Construir um programa que faz a leitura de um numero de apenas DOIS dıgitos: de 0 a 99. Utilizando o comando if, imprima o numero por extenso. Exemplo: leitura do numero 52, imprimir CINQUENTA E DOIS.

unidades = ["", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE"]
dezenas = ["", "DEZ", "VINTE", "TRINTA", "QUARENTA", "CINQUENTA", "SESSENTA", "SETENTA", "OITENTA", "NOVENTA"]
especiais = ["DEZ", "ONZE", "DOZE", "TREZE", "QUATORZE", "QUINZE", "DEZESSEIS", "DEZESSETE", "DEZOITO", "DEZENOVE"]

num = int(input("Digite um número entre 0 e 99: "))

if 0 <= num <= 99:
    if num < 10:
        print(unidades[num])
    elif 10 <= num <= 19:
        print(especiais[num - 10])
    else:
        dezena = num // 10
        unidade = num % 10
        extenso = dezenas[dezena]
        if unidade != 0:
            extenso += " E " + unidades[unidade]
        print(extenso)
else:
    print("Número inválido!")

