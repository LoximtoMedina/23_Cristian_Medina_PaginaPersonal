#Importación del módulo de SQLite3
import sqlite3

#Creación de la conexión con la base de datos
con=sqlite3.connect("BDLibreria.bd")

#Creación del objeto cursor
cur=con.cursor()

#Inicio del ciclo para la modificación de registros de forma dinámica
while True:
    print("""-------------MENÚ DE MODIFICACIÓN DE REGISTROS-------------
        1- Modificar un registro
        2- Volver al menú principal""")
    
    #Respuesta del usuario a las opciones presentadas
    op=int(input("""¿Qué desea realizar? (Utilice los números) 
            ¬ """))
    
    #Evaluación de la respuesta del usuario (Se realiza una acción según el número que haya puesto)
    if op==1:

        #Sentencia que me permite modificar el registro que desea el usuario
        registro=int(input("Ingrese el código del registro que desea modificar: "))
        cur.execute(f"SELECT * FROM TDLibros WHERE codigo={registro};")
        fila=cur.fetchone()
        if fila!=None:

            #Petición al usuario para ingressar los datos del registro a modificar
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
            
            cur.execute(f"UPDATE TDLibros SET nombre='{nom}', autor='{aut}', categoria='{cat}', cantidad={can}, estado='{est}' WHERE codigo={registro};")
            con.commit()
            cur.execute(f"SELECT * FROM TDLibros WHERE codigo={registro};")
            tabla=cur.fetchone()
            for filas in tabla:
                print(filas)
        else:
            print("Registro Inexistente")
            print("")
        
        #Comprobando si el usuario desea modificar más registros o desea volver al menú principal
        comprobacion=int(input("""¿Desea modificar otro registro?
                1- Sí
                2- No
                ¬ """))

        #Evaluación de la respuesta del usuario ante la confirmación (regresa al menú principal en caso de que sea 2)
        if comprobacion==2:
            print("Regresando al menú principal...")
            import menu.py
            menu.py

    elif op==2:

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