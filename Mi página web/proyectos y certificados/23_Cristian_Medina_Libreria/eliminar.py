#Importación del módulo de SQLite3.
import sqlite3

#Creación de la conexión con la base de datos.
con=sqlite3.connect("BDLibreria.bd")

#Creación del objeto cursor.
cur=con.cursor()

#Inicio del ciclo para la eliminación de registros de forma dinámica.
while True:
    print("""-------------MENÚ DE ELIMINACIÓN DE REGISTROS-------------
        1- Eliminar un registro
        2- Volver al menú principal""")
    
    #Respuesta del usuario a las opciones presentadas.
    op=int(input("""¿Qué desea realizar? (Utilice los números) 
            ¬ """))
    print("")

    #Evaluación de la respuesta del usuario (Se realiza una acción según el número que haya puesto).
    if op==1:

        #Sentencia que permite al usuario borrar el registro que desea.
        registro=int(input("Ingrese el código del registro que desea eliminar: "))
        cur.execute(f"SELECT * FROM TDLibros WHERE codigo={registro};")
        fila=cur.fetchone()
        if fila!=None:
            cur.execute(f"DELETE * FROM TDLibros WHERE codigo={registro};")
            con.commit()
            cur.execute(f"SELECT * FROM TDLibros;")
            tabla=cur.fetchall()
            for filas in tabla:
                print(filas)
        else:
            print("Registro Inexistente")
            print("")

        #Comprobando si el usuario desea eliminar más registros o desea volver al menú principal
        comprobacion=int(input("""¿Desea eliminar otro registro?
                1- Sí
                2- No
                ¬ """))

        #Evaluación de la respuesta del usuario ante la confirmación (regresa al menú principal en caso de que sea 2)
        if comprobacion==2:
            print("Regresando al menú principal...")
            import Menú.py
            Menú.py

    elif op==2:

        #Comprobando que el usuario realmente desea regresar al menú principal.
        comprobacion=int(input("""¿Realmente desea regresar al menú principal?
                1- Sí
                2- No
                ¬ """))

        #Evaluación de la respuesta del usuario ante la confirmación (Sale del programa en caso de que sea 1).
        if comprobacion==1:
            print("Regresando al menú principal...")
            import Menú.py
            Menú.py