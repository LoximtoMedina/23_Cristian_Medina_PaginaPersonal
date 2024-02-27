#Importación del módulo de SQLite3 y el resto de programas del programa
import sqlite3

#Creación de la conexión con la base de datos
con=sqlite3.connect("BDLibreria.bd")

#Creación del objeto cursor
cur=con.cursor()

#Creación de la tabla
try:
    con.execute("""CREATE TABLE TDLibros(
        codigo int pk ai,
        nombre text,
        autor text,
        categoria text,
        cantidad int,
        estado text);""")
    print("La tabla ha sido creada correctamente")
except sqlite3.OperationalError:
    print("-------------¡Bienvenido Usuario!-------------")
    print("")

#Inicio del ciclo para el programa dinámico
while True:

    #Lista de opciones que posee el programa
    print("""-------------MENÚ PRINCIPAL-------------
        1- Insertar Registros
        2- Modificar Registros
        3- Eliminar Registros
        4- Realizar Consultas
        5- Presentación
        6- Salir del programa  """)

    #Respuesta del usuario a las opciones presentadas
    op=int(input("""¿Qué desea realizar? (Utilice los números) 
            ¬ """))
    print(" ")

    #Evaluación de la respuesta del usuario (Se abre un programa según el número que haya puesto)
    if op==1:
        import ingreso.py
        ingreso.py
    elif op==2:
        import Modificar.py
        modificar.py
    elif op==3:
        import eliminar.py
        eliminar.py
    elif op==4:
        import consulta.py
        consulta.py
    elif op==5:
        import presentacion.py
        presentacion.py
    elif op==6:
        #Comprobando que el usuario realmente desea salir del programa
        comprobacion=int(input("""¿Realmente desea salir del programa?
                1- Sí
                1- No
                ¬ """))

        #Evaluación de la respuesta del usuario ante la confirmación (Sale del programa en caso de que sea 1)
        if comprobacion==1:
            print("Bye Bye!")
            con.close()
            break