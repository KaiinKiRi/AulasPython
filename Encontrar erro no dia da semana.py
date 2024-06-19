# Programa progSemana
vetSemana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']
num = int(input('Digite o número do dia (1 a 7) :'))
if num>=1 and num<=7 :
    print('O dia ', num, ' é ', vetSemana[num-1])
else :
    print('Dia inválido')
