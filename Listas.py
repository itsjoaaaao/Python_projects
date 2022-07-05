# Declaração
cores = list()
cores = []
cores = ['branco', 'azul', 'amarelo']
numeros = [1, 2, 3, 4, 5]

#print(len(numeros))
#Acesso
#print(cores[0])
print(numeros[-2])
print('azul' in cores)
#print(cores)
# Alterar / Adicionar
cores[1] = 'rosa'
#print(cores)
cores.append('azul')
#print(cores)
cor = 'vermelho'
cores.insert(-1, cor)
print(cores)
# Remover
#del cores[1]
#cor = cores.pop(1)
#print("removi: ", cor)
if 'roxo' in cores:
    cores.remove('roxo')
    print("Removi o roxo")
else:
    print("Não há roxo na lista")

#for cor_new in cores:
#    print(cor_new)
    #outras instruções

# lista variada
lista1 = [1, 3, 5, 2, 4]
nome_da_lista = ['amarelo', 1, [10.4, 10.5], 'azul']

print(type(nome_da_lista[0]))
print(type(nome_da_lista[1]))
print(type(nome_da_lista[2]))

nova_lista = nome_da_lista[2]
print(nova_lista[0])

list_3 = list( range(0,5,1) )
print("tamanho da lista:", len(list_3))
print(list_3)

i = 0
for n in list_3:
    list_3[i] = n +1
    i = i+1
#print(list3)