import math as m

# Funções que realizam as operações
def soma(x,y):
  resultado = x + y
  return resultado

def diferença(x,y):
  resultado = x - y
  return resultado

def multiplicaçao(x, y):
  resultado = x * y
  return resultado

def divisao(x, y):
  resultado = x / y
  return resultado

print("\n===========================\n Bem vindo a CALCULADORA!\n===========================\n")

# Loops de entrada do usuário

while True:
  while True:
    print("-----------------")
    numero1 = input("NÚMERO 1:  ")
    print("-----------------")
    if not numero1.isdigit():
      print("Digite um número!")
      continue
    numero1 = int(numero1)
    break
  while True:
    print("-----------------")
    operaçao = input('Digite a operação (+ - * /): ')
    print()
    print("-----------------") 
    if operaçao not in ["+","-","*","/"]: 
      print("Operação incorreta!")
    else:
      break
  while True:
    print("-----------------")    
    numero2 = input("Número 2: ")
    print()
    print("-----------------")
    if not numero2.isdigit():
      print("Digite um número!")
      continue
    numero2 = int(numero2)
    break
# Chamada das funções
  if operaçao == "+":
    print("O resultado é: ", soma(numero1,numero2))
  elif operaçao == "-":
    print("O resultado é: ", diferença(numero1,numero2))
  elif operaçao == "*":
    print("O resultado é: ", multiplicaçao(numero1,numero2))
  elif operaçao == "/":
    print("O resultado é: ", round(divisao(numero1,numero2),2))
# Verificação para reiniciar o loop
  reiniciar = input("\nDeseja continuar?(s/n): ").lower().strip()
  if reiniciar != "s":
    print("\n┌-----------┐\n|           |\n| Até mais! |\n|           |\n└-----------┘")
    break

