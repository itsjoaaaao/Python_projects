tinta = 0
arquivo = open("Arquivo_mat_construção.txt", "w")
tamanho = int(input("Digite o tamanho em metros quadrados: "))
if tamanho == 54:
    arquivo.write(print("Você comprou 1 lata de tinta, Preço: 80,00"))
elif tamanho < 54:
    arquivo.write(print("O tamanho precisa ser maior que 54 metros, cada 3 metros = 1L, cada tinta = 18L"))
elif tamanho > 54:
    result = tamanho / 18
    tinta = result * 80
    arquivo.write(print("Você comprou {} latas de tinta, Preço : {}", result, tinta))
arquivo.close()