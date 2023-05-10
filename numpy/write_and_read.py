print(f'{" Inicio do Programa ":#^30}\n')
numeros = '3\n4\n7\n11\n18\n29\n47\n'
arq = open('arquivos_numeros', 'w')
arq.write(numeros)
arq.close()

print('Leitura')
count = 0
sum = 0
for linha in open('arquivos_numeros'):
    n = int(linha)
    sum += n
    count += 1
    print(f'Elemento {count} = {n}')

print(f'Soma: {sum}. Quantidade: {count}')
