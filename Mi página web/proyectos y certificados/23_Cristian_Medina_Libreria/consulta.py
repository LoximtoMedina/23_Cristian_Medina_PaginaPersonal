#Importación del módulo de SQLite3
import sqlite3

#Creación de la conexión con la base de datos
con=sqlite3.connect("BDLibreria.bd")

#Creación del objeto cursor
cur=con.cursor()

#Inicio del ciclo para las consultas dinámicas
while True:
    print("""-------------MENÚ DE CONSULTAS DE REGISTROS-------------
        1- Mostrar los libros por categoría
        2- Mostrar los libros por nombre
        3- Mostrar los libros por autor
        4- Mostrar los libros con menos de 3 unidades
        5- Mostrar los libros con estado "Disponible"
        6- Mostrar los libros con estado "Prestado"
        7- Mostrar un libro en específico
        8- Volver al menú principal""")

    #Respuesta del usuario a las opciones presentadas
    op=int(input("""¿Qué consulta desea realizar? (Utilice los números) 
            ¬ """))
    print("")

    #Evaluación de la respuesta del usuario (Se realiza una consulta según el número que haya puesto)
    if op==1:

        #Sentencia que me permite ordenar los libros por categoría (Ascendente)
        cur.execute("SELECT * FROM TDLibros WHERE categoria ORDER BY ASC;")
        tabla=cur.fetchall()
        for fila in tabla:
            print(fila)

        #Comprobando si el usuario desea hacer más consultas o desea volver al menú principal
        comprobacion=int(input("""¿Desea realizar otra consulta?
                1- Sí
                2- No
                ¬ """))

        #Evaluación de la respuesta del usuario ante la confirmación (regresa al menú principal en caso de que sea 2)
        if comprobacion==2:
            print("Regresando al menú principal...")
            import menu.py
            menu.py

    elif op==2:

        #Sentencia que me permite ordenar los libros por nombre (Ascendente)
        cur.execute("SELECT * FROM TDLibros WHERE nombre ORDER BY ASC;")
        tabla=cur.fetchall()
        for fila in tabla:
            print(fila)
        
        #Comprobando si el usuario desea hacer más consultas o desea volver al menú principal
        comprobacion=int(input("""¿Desea realizar otra consulta?
                1- Sí
                2- No
                ¬ """))

        #Evaluación de la respuesta del usuario ante la confirmación (regresa al menú principal en caso de que sea 2)
        if comprobacion==2:
            print("Regresando al menú principal...")
            import menu.py
            menu.py

    elif op==3:

        #Sentencia que me permite ordenar los libros por autor (Ascendente)
        cur.execute("SELECT * FROM TDLibros WHERE autor ORDER BY ASC;")
        tabla=cur.fetchall()
        for fila in tabla:
            print(fila)

        #Comprobando si el usuario desea hacer más consultas o desea volver al menú principal
        comprobacion=int(input("""¿Desea realizar otra consulta?
                1- Sí
                2- No
                ¬ """))

        #Evaluación de la respuesta del usuario ante la confirmación (regresa al menú principal en caso de que sea 2)
        if comprobacion==2:
            print("Regresando al menú principal...")
            import menu.py
            menu.py

    elif op==4:

        #Sentencia que me permite saber que libros poseen 3 o menos unidades
        cur.execute("SELECT * FROM TDLibros WHERE cantidad<4;")
        tabla=cur.fetchall()
        for fila in tabla:
            print(fila)

        #Comprobando si el usuario desea hacer más consultas o desea volver al menú principal
        comprobacion=int(input("""¿Desea realizar otra consulta?
                1- Sí
                2- No
                ¬ """))

        #Evaluación de la respuesta del usuario ante la confirmación (regresa al menú principal en caso de que sea 2)
        if comprobacion==2:
            print("Regresando al menú principal...")
            import menu.py
            menu.py

    elif op==5:

        #Sentencia que me permite saber qué libros están disponibles
        cur.execute("SELECT * FROM TDLibros WHERE estado LIKE '%Disponible%;")
        tabla=cur.fetchall()
        for fila in tabla:
            print(fila)

        #Comprobando si el usuario desea hacer más consultas o desea volver al menú principal
        comprobacion=int(input("""¿Desea realizar otra consulta?
                1- Sí
                2- No
                ¬ """))

        #Evaluación de la respuesta del usuario ante la confirmación (regresa al menú principal en caso de que sea 2)
        if comprobacion==2:
            print("Regresando al menú principal...")
            import menu.py
            menu.py

    elif op==6:

        #Sentencia que me permite saber qué libros están prestados
        cur.execute("SELECT * FROM TDLibros WHERE estado LIKE '%Prestado%';")
        tabla=cur.fetchall()
        for fila in tabla:
            print(fila)

        #Comprobando si el usuario desea hacer más consultas o desea volver al menú principal
        comprobacion=int(input("""¿Desea realizar otra consulta?
                1- Sí
                2- No
                ¬ """))

        #Evaluación de la respuesta del usuario ante la confirmación (regresa al menú principal en caso de que sea 2)
        if comprobacion==2:
            print("Regresando al menú principal...")
            import menu.py
            menu.py

    elif op==7:

        #Sentencia que me permite saber la información de un libro específico
        especifico=int(input("Ingrese el código que desea consultar: "))
        cur.execute(f"SELECT * FROM TDLibros WHERE codigo={especifico};")
        fila=cur.fetchone()
        if fila!=None:
            for registro in fila:
                print(registro)
        else:
            print("Libro Inexistente")

        #Comprobando si el usuario desea hacer más consultas o desea volver al menú principal
        comprobacion=int(input("""¿Desea realizar otra consulta?
                1- Sí
                2- No
                ¬ """))

        #Evaluación de la respuesta del usuario ante la confirmación (regresa al menú principal en caso de que sea 2)
        if comprobacion==2:
            print("Regresando al menú principal...")
            import menu.py
            menu.py

    elif op==8:
        #Comprobando que el usuario realmente desea regresar al menú principal
        comprobacion=int(input("""¿Realmente desea regresar al menú principal?
                1- Sí
                2- No
                ¬ """))

        #Evaluación de la respuesta del usuario ante la confirmación (Sale del programa en caso de que sea 1)
        if comprobacion==1:
            print("Regresando al menú principal...")
            import menu.py
            menu.py
    else:
        print("Instrucción inválida")

        #Comprobando si el usuario desea hacer más consultas o desea volver al menú principal
        comprobacion=int(input("""¿Desea realizar otra consulta?
                1- Sí
                2- No
                ¬ """))

        #Evaluación de la respuesta del usuario ante la confirmación (regresa al menú principal en caso de que sea 2)
        if comprobacion==2:
            print("Regresando al menú principal...")
            import menu.py
            menu.py