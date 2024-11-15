print("Programa para calculo IVA")

precio_sin_IVA=float(input("introduce un precio"))
IVA =float(input("introduce el IVA"))

IVA=precio_sin_IVA*IVA/100
precio_con_IVA=precio_sin_IVA + IVA

print("El precio sin IVA es " ,precio_sin_IVA)
print("El IVA es " , IVA)
print("El precio con IVA es " , precio_con_IVA)


#Código para comprobar el test

#Para probar que el código funciona, se ejecuta en otro terminal abajo, se pone como primer valor precio sin Iva : 100. El IVA : 20. 
#El resultado sería en este caso: el Precio sin Iva : 100, IVA : , pRECIO CON iva :120.
#se comprueba que los valores son correctos.

#Descripción
#Con este programa se puede calcular un precio con IVA, dado cualquier precio y cualquier IVA.
#Al trabajar en equipo se pueden recibir otos puntos de vista y otras formas de harce las cosas de forma diferente a como estamos acostumbrados.

#COMO, QUIERO, PARA QUE
#Desde el punto de vista de un esquimal, se quiere saber la temperatura perfecta para pescar en el hielo.
