print('Essa aplicação converte uma temperatura Fahrenheit em Celsius')
temp = input('Digite a temperatura em Fahrenheit: ')

conv = float(temp)

c = 5.0 * (conv - 32.0) / 9.0

print('A temperatura em Fahrenheit lida foi: ',conv)
print('A temperatura Fahrenheit, convertida em Celsius e: ',c)