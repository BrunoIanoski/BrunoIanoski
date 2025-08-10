#Lista de Exercícios I da disciplina de Algoritmos e Estruturas de Dados I

# Exercício 1
print('Programação é incrível!')

# Exercício 2
var1 = int(input('Insira o primeiro número: '))
var2 = int(input('Insira o segundo número: '))

soma = var1 + var2

print('A soma é: ', soma)

# Exercício 3
# a)
import math as m

x = float(input('Insira o primeiro número: '))
y = float(input('Insira o segundo número: '))
z = float(input('Insira o terceiro número: '))

a = m.cos(m.radians(x))
b = m.cos(m.radians(y))
c = m.cos(m.radians(z))

print('O cosseno de X Y e Z é: %1.3f %1.3f %1.3f' % (a, b, c))

# b)
multi = x * y * z

print('A multiplicação de X Y e Z é: ', multi)

# c)
div = (x+y)/z

print('O resultado de X+Y/2 é: ', div)

# d)
mediaP = (x*2 + y*3 + z*5)/10

print('A média ponderada entre X Y e Z é: ', mediaP)

# e)
poten = (x**y)**z

print('O resultado da potenciação é: ', poten)

# f)
log = (m.log2(x)+m.log10(y)) * z

print('O resultado do logaritmo é: ', round(log,2))

# g)
oper = (x*0.4)+(y*0.5)+(z*0.1)

print('O resultado da operação é: ', round(oper,2))

# h)
poten2 = (x**2) + (y**5) + (z**7)

print('O resultado da potenciação é: ', poten2)

# i)
oper2 = (x/3) + (y**2) - 5 * z

print('O resultado da operação é: ', round(oper2,2))

# j)
cossin = m.cos(m.radians(x)) + y**2 * m.sin(m.radians(z))

print('O resultado da operação é: ', round(cossin,2))

# k)
raiz = m.sqrt(x) + y * z

print('O resultado da operação é: ', round(raiz,2))

# l)
tancos = (m.tan(m.radians(x))+y**4)/(m.cos(m.radians(z))+1)

print('O resultado da operação é: ', round(tancos,2))

# Exercício 4
h = float(input('Insira a altura inicial em M: '))
g = 9.81

i = m.sqrt((2*h)/g)

print('O tempo que o objeto demora para cair em segundos é: ', round(i,2))

# Exercício 5
valor1 = int(input('Insira o primeiro valor: '))
valor2 = int(input('Insira o segundo valor: '))

quociente = valor1/valor2
resto = valor1%valor2

print(f'O quociente é: {round(quociente,5)} e o resto é {resto}')
