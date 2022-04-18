#6.	Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M...


def hora(h, m):
    b = h / 12
    if b <= 1:
        hh = str(h)
        print('Sua hora: '+ hh + ':', end='')
    elif b > 1 and b < 2:
        hhh = str(h - 12)
        print('Sua hora: '+ hhh + ':', end='')
    else:
        print('Formato de hora invalido')
    if b <= 1 and m <= 60:
        print(m, 'a.m')
    elif b > 1 and m <= 60:
        print(m, 'p.m')
    else:
        print('Formato de minutos invalidos')


h = int(input('Informe a hora:'))
m = int(input('Informe os minutos: '))
hora(h, m)