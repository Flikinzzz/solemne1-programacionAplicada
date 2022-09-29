


# ---> Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario.
def ejercicio1 ():

    num = int(input("Ingrese un numero entero \n"))

    for i in range (1,11):
        print(f"{num}*{i}={num*i}")


# ---> A partir de las siguientes 5 listas:
#      nombres = ["Felipe","Javier","Camila","Natalia"]
#      apellidos = ["Gonzalez","Flores","Sepulveda","Fuentez"]
#      nota_1= [6.5,5.1,1.0,4.5]
#      nota_2= [6.2,5.1,2.0,5.5]
#      asistencia = [80,90,50,45]
#
#Las listas tienen una relación 1:1, es decir que el primer elemento de la primera lista se relaciona con el primer
# elemento del resto de las listas. Realice un programa que solicite un nombre. Si el nombre se encuentra en la lista
# nombres, el programa deberá imprimir por pantalla todos sus datos, además de un mensaje de aprobado o reprobado
# dependiendo del promedio entre la nota 1, 2. Considere para aprobar una calificación mayor o igual a 4.5. Si el nombre
# ingresado no se encuentra en la lista, deberá imprimir un mensaje por pantalla que diga “el nombre no se encuentra en
# la lista”. Utilice un ciclo para recorrer los elementos de la lista.
def ejercicio2 ():
    # ---> Datos entregados en el enunciado
    nombres = ["Felipe", "Javier", "Camila", "Natalia"]
    apellidos = ["Gonzalez","Flores","Sepulveda","Fuentez"]
    nota_1= [6.5,5.1,1.0,4.5]
    nota_2= [6.2,5.1,2.0,5.5]
    asistencia = [80,90,50,45]

    # ---> Ingresar nombre que se busca
    nombre = input("Ingrese un nombre: ")

    for i in range(len(nombres)):
        # ---> para evitar problemas de identificacion
        nombres[i] = nombres[i].lower()
        if nombre == nombres[i]:
            print(
                f"Nombre:{nombre}\nApellido:{apellidos[i]}\nNota 1:{nota_1[i]}\nNota 2:{nota_2[i]}\nAsistencia:{asistencia[i]}")
            promedio = (nota_1[i] + nota_2[i]) / 2
            if promedio < 4.5:
                print("Reprobado")
                break
            else:
                print("Aprobado")
                break
        #else:
            #print(f"Ese nombre no existe en la parte {i} de la lista")

        if nombre != nombres[i]:
            print(f"{nombre} no existe en la lista {i}")



ejercicio2()

