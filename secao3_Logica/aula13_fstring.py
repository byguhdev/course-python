# imc
nome = 'Bla bla'
peso = 89
altura = 1.77867453
imc = peso / (altura ** 2)

"f-strings"
linha_1 = f'{nome}, tem, {altura:.2f}, de altura'
linha_2 = f'e pesa, {peso}, quilos e seu imc e: , {imc:.2f}'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)