print(f'{" Inicio do Programa ":#^30}\n')

gravacao = 'Gravação e Leitura de texto'
arq = open('./ex_tst_01', 'w')             # com 'w' abrimos o arquivo em modo de escrita, sobrescrevendo tudo o que existir
arq.write(gravacao)
arq.close()

# Leitura do arquivo

arq = open('./ex_tst_01', 'r')
line = arq.readline()
arq.close()
print(f'String lida: {line}')

print(f'\n{" Fim do Programa ":#^30}')
