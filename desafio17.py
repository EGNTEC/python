import math

c1 = float(input('Informe o comprimento: '))
c2 = float(input('Informe a Altura: '))

Hip = math.sqrt(math.pow(c1, 2)+math.pow(c2, 2))

print('O valor da hipotenusa é {}'.format(Hip))