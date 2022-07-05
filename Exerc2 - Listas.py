#usuario inserindo dados na lista
num = []
for c in range(0, 5):
    x = int(input("Digite um numero: "))
    num.append(x)
max(num)
min(num)
print("O maior número é: {}".format(max(num)))
print("O menor número é: {}".format(min(num)))