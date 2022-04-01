# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

x = float(input('Valor = '))


def valor(v):
  n = int(v)
  m = v * 10
  s = n * 10
  if m == s:
    return (f'O número {v} é inteiro')
  else:
    return (f'O número {v} é decimal') 
r = valor(x)
print(r)