""" total = int(input("Cuanto dinero tienes en tu cartera:\n"))

#las condicionales siempre empezaran con un if, y terminan en else

if total >= 100:
    print("dame todo tu dinero")

elif total >= 50:
    print("rajate con el almuerzo")

elif total < 5 and total > 0 and total > 1:
    print("amigo dame una monedita")

elif total < 0 or total == 0:
    print("estas endeudado")

else:
    #no se necesita nada mas en el else
    print("hola") """


#haz un programa que le pregunte al usuario cuantos invitados hay para el baby shower
## si los invitados son mayor o igual a 50 imprimes el costo del baby shower es de 4000 doalres

#si hay 100 o mas invitados el costo es de 10000 doalres

# si hay 200 invitados el costo es de 20000

#en otro caso el costo sera de 30000

guest = int(input("cuantos invitados hay:\n"))
if guest >= 50 and guest < 100:
    print("4000 dolars")
elif guest > 1 and guest < 50:
    print ("2200")
elif guest >= 100  and guest < 200:
    print ("10000 dolars")
elif guest == 200:
    print ("20000 dolars")
else:
    print ("30000 dolars")