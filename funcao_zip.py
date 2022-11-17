## Zip manipula e mescla estruturas de dados e seus valores, porem o resultado sempre sera da o valor da menor estrutura de dados

dicverduras={1:"cebola",2:"Alface",3:"Repolho",4:"Beterraba"}
dicfrutas={1:"Maça",2:"Laranja",3:"Pera"}
mescla=list(zip(dicverduras,dicfrutas))
print(mescla)

mesclavalores=list(zip(dicverduras.values(),dicfrutas.values()))
print(mesclavalores )

## Interar os valores
for p in mesclavalores:
    print(p)