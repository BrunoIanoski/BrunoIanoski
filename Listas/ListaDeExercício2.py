import math as m

a = float(input('Insira o primeiro valor em graus: '))
b = float(input('Insira o segundo valor em graus: '))
c = float(input('Insira o terceiro valor em graus: '))

radianos = m.radians(a)
radianos1 = m.radians(b)
radianos2 = m.radians(c)

x = m.sin(radianos)
y = m.sin(radianos1)
z = m.sin(radianos2)

print('O seno de A,B e C é: %1.1f %1.1f %1.1f' % (x,y,z))

a = float(input('Insira o primeiro valor: '))
b = float(input('Insira o segundo valor: '))
c = float(input('Insira o terceiro valor: '))

soma = a+b+c

print('A soma de A,B e C é: ', soma)

soma2 = ((a+b)/2)

print('A soma de (A+B)/2 é: ', soma2)

media = ((a+b+c)/3)

print('A média de A,B e C é: ', media)

a = float(input('Insira o primeiro valor: '))
b = float(input('Insira o segundo valor: '))
c = float(input('Insira o terceiro valor: '))

poten = ((a**b)**c)

print('A o resultado de A elevado a B, elevado a C é: ', poten)

log = m.log10(a)*(c+(m.log2(b)))

print('O resultado é: %1.5f'% log)