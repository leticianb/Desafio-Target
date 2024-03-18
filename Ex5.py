def inverte(palavra):
    invertida = palavra[::-1]
    return invertida

palavra = input('Digite uma palavra: ')
invertida = inverte(palavra)
print(invertida)