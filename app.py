import random

salas= []
sala_de_cine= []

peliculas= ["Interestelar", "El Padrino", "Titanic", "Marvel: Avengers", "La Liga de la Justicia", "El Señor de los Anillos"]



filas_x= 8
columnas_y=10

"""

print(f"{'-'*25} CREACIÓN DE SALA DE CINE {'-'*25}")



while filas_x<=0 or columnas_y<=0:

    filas_x= int(input("Ingrese la cantidad de filas horizontales: \n"))
    columnas_y= int(input("Ingrese la cantidad de columnas verticales: \n"))

if filas_x<=0 or columnas_y<=0:
    print("Ingrese valores válidos para las filas y columnas.\n")

"""

cantidad_sillas= filas_x * columnas_y



print(f"La cantidad de sillas en la sala es: {cantidad_sillas}\n")

        

def crear_sala(filas_x, columnas_y):


    for fil in range(filas_x):
        fila= []
        for col in range(columnas_y):
            fila.append("-")
        sala_de_cine.append(fila)
    return sala_de_cine

crear_sala(filas_x, columnas_y)

i=0
for i, pelicula in enumerate(peliculas):


    conjunto_salas= {
        "id": i+1,
        "pelicula": pelicula,
        "sala": sala_de_cine
    }
    salas.append(conjunto_salas)
    i+=1

print(salas)

def mostrar_sala(sala_de_cine):
    print("------- [PANTALLA] -------\n")

    for i, fila in enumerate(sala_de_cine):
        print(f"Fila {i+1}")
        for j, silla in enumerate(fila):
            print(f"{silla} ", end=" ")
        print()




opc= 1

while opc==1:

    print(f"""{'-'*25} SALA DE CINE {'-'*25}
    1. Comprar tiquetes
    2. Ver Salas de Cine
    3. Salir

    """)


    opcion= int(input("Ingrese una opción: "))


    match opcion:

        case 1:
            
            seguir= 1

            while seguir==1:
            
                print("BIENVENIDO A CINEDAN. A CONTINUACIÓN, SE MUESTRAN LAS SALAS DISPONIBLES")


                for sala in range(len(salas)):

                    print(f"""{'-'*25} SALA {sala+1} {'-'*25}""")
                    print(f"Película: {peliculas[sala]}\n")

                elegir_sala= int(input("Ingrese N° de sala de interés: "))
                elegir_sala-=1

                if elegir_sala > 0 or elegir_sala <= len(peliculas):
        
                    print(f"""{'-'*25} SALA {salas[elegir_sala]["id"]} {'-'*25}""")
                    print(f"Película: {peliculas[elegir_sala]}\n")

                mostrar_sala(sala_de_cine)
                

                

                cantidad_boletos= int(input("\n Ingrese la cantidad de boletos que desea comprar: \n"))


                if cantidad_boletos > 0:

                    fila_escogida= int(input("Ingrese el número de fila que desea escoger: \n")) - 1

                    ocupada= False

                    for i in range(cantidad_boletos):

                        columnas_escogidas= int(input(f"Ingrese el número de columna para el boleto {i+1}: \n")) - 1
                            
                        if 0<=fila_escogida<len(sala_de_cine) and 0 <= columnas_escogidas < len(sala_de_cine[0]):
                                
                                if sala_de_cine[fila_escogida][columnas_escogidas] == "-":
                                        sala_de_cine[fila_escogida][columnas_escogidas] = "X"
                                        print(f"Asiento elegido: ({fila_escogida+1},{columnas_escogidas+1})\n")

                                else:
                                        print("La silla ya está ocupada.")
                                        ocupada= True

                                if ocupada:
                                    break
                                        
                                    


                        else:
                                print("Número de fila o columna inválido.")


                    print("\n NUEVO ESTADO DE LA SALA DE CINE\n")
                    mostrar_sala(sala_de_cine)


                    seguir= input("¿Desea continuar? (1: Sí, Cualquier otra tecla: No)")
                    seguir= int(seguir)

                else:
                    print("Cantidad de boletos insuficientes")
                


        case 2:
            print("MOSTRANDO SALA DE CINE...\n")
            mostrar_sala(sala_de_cine)

        case 3:
            print("Saliendo...")
            break
         
        case _:
               print("Opción inválida. Por favor, ingrese una opción válida.")







