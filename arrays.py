""" #el indice de la lista empieza en 0
#esta lista tiene 0,1,2,3,4 como indices
number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]

print(number_list[8])

number_list.append(14)
print(number_list) 

#aca se imprime hasta cuando se agrego 14 ala lista

##agregues los numeros del 15 al 18
number_list.append(15)
number_list.append(16)
number_list.append(17)
number_list.append(18)
print(number_list)

#aca no hay nada para visualizar el valor actual de la lista modificada """


""" number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#pop elimina el ultimo elemento del array
number_list.pop()
number_list.pop()
number_list.pop()
number_list.pop()
print(number_list)
 """

number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#extend agrega mas elemento que dclare dentro de corchete ala lista
number_list.extend([14,15,16,17])
print(number_list)

number_list.extend([18,19,29,21])
print(number_list)
#este es un comentario
