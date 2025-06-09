arquivo= open('arquivo.txt', 'r',encoding='utf-8')
#read the entire file
conteudo = arquivo.read()
# print the content of the file
print(conteudo)
# close the file
arquivo.close