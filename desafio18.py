import math

n1 = int(input('Informe um ângulo: '))

s = math.trunc(math.sin(n1))
c = math.trunc(math.cos(n1))
t = math.trunc(math.tan(n1))

print('O ângulo {} tem como cosseno {}, Seno {} e Tangente {}'.format(n1, s, c, t))