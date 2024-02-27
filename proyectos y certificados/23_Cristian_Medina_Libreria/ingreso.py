#Importación del módulo de SQLite3.
import sqlite3

#Creación de la conexión con la base de datos.
con=sqlite3.connect("BDLibreria.bd")

#Creación del objeto cursor.
cur=con.cursor()

#Inicio del ciclo para ingresar registros de forma dinámica.
while True:
    print("""-------------MENÚ DE INGRESO DE REGISTROS-------------
        1- Ingresar un registro
        2- Volver al menú principal""")
    
    #Respuesta del usuario a las opciones presentadas.
    op=int(input("""¿Qué desea realizar? (Utilice los números) 
            ¬ """))
    print("")

    #Evaluación de la respuesta del usuario (Se realiza una acción según el número que haya puesto).
    if op==1:

        #Sentencia que permite al usuario ingresar un registro
        cod=int(input("Ingrese el código del libro: "))
        nom=str(input("Ingrese el nombre del libro: "))
        aut=str(input("Ingrese el autor del libro: "))
        cat=str(input("Ingrese la categoría del libro: "))
        can=int(input("Ingrese la cantidad de unidades que hay de ese libro: "))
        est=str(input("""Ingrese el estado del libro | 1-Disponible 2-Prestado
                ¬ """))
        if est==1:
            est="Disponible"
        else:
            est="Prestado"
        cur.execute(f"INSERT INTO TDLibros (codigo,nombre,autor,categoria,cantidad,estado) VALUES ({cod},'{nom}','{aut}','{cat}',{can},'{est}');")
        con.commit()
        cur.execute(f"SELECT * FROM TDLibros;")
        tabla=cur.fetchall()
        for filas in tabla:
            print(filas)

        #Comprobando si el usuario desea ingresar más registros o desea volver al menú principal
        comprobacion=int(input("""¿Desea ingresar otro registro?
                1- Sí
                2- No
                ¬ """))

        #Evaluación de la respuesta del usuario ante la confirmación (regresa al menú principal en caso de que sea 2)
        if comprobacion==2:
            print("Regresando al menú principal...")
            import menu.py
            menu.py

    elif op==2:

        #Comprobando que el usuario realmente desea regresar al menú principal.
        comprobacion=int(input("""¿Realmente desea regresar al menú principal?
                1- Sí
                2- No
                ¬ """))

        #Evaluación de la respuesta del usuario ante la confirmación (Sale del programa en caso de que sea 1).
        if comprobacion==1:
            print("Regresando al menú principal...")
            import menu.py
            menu.py