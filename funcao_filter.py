## Função Filter ela filtra um valor de uma estrutura de dados

lista1=[1,"João",67,"Pedro",78.31]
def busca(x):
    return x =="João"
print(list(filter(busca,lista1)))

##Otimizando a busca utilizando Lambda

print(list(filter(lambda x:x=="Pedro",lista1)))