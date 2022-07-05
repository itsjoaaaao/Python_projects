print('-----Calculadora-----')
nome = str(input('Qual é o seu nome? '))
print('Seja Bem vindo {}!'.format(nome))
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
op = str(input('Digite a operação: '))
if op == '+':
    soma = x + y
    print('o resultado de {} + {} é: {}'.format(x, y, soma))
if op == '-':
    sub = x - y
    print('o resultado de {} - {} é: {}'.format(x, y, sub))
if op == '*':
    mult = x * y
    print('o resultado de {} * {} é: {}'.format(x, y, mult))
if op == '/':
    div = x / y
    print('o resultado de {} / {} é: {}'.format(x, y, div))
#print(dfff)
