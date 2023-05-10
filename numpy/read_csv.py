print('Gastança')
total = 0
for item in open('lista_de_compras.csv'):
    item = item.strip()
    dados_item = item.split(',')
    dados_item[1], dados_item[2] = int(dados_item[1]), float(dados_item[2])
    total_produto = dados_item[1] * dados_item[2]
    total += total_produto
    print(f' {dados_item[0]:>12}: {dados_item[1]:3} x {dados_item[2]:6.2f} = R$ {total_produto:6.2f}')

print('-' * 40)
print(f'Total da lista de compras: {total:>12}')
