#arquivos

arquivo = open('arquivoteste.txt','w')
line1 = 'eu amo ela demais\n'
line2 = 'hj tem gol do ribamar'
arquivo.write(line1)
arquivo.write(line2)
print(line1)
arquivo.close()
