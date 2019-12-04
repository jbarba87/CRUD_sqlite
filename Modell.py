
import sqlite3
import Alumno

path = 'alumnos_db'

class Modell:

    def ingresar_alumno_db(alumno):
        try:
            conn = sqlite3.connect(path)
        except:
            print("Error al conectar con la DB")
        c = conn.cursor()

        codigo = alumno.getcodigo()
        nombre = alumno.getnombre()
        horario = alumno.gethorario()
        esp = alumno.getespecialidad()
        correo = alumno.getcorreo()

        sql_command = "insert into IEE239 (codigo, nombre, horario, especialidad, correo) values ('{}', '{}', '{}', '{}', '{}')".format (codigo, nombre, horario, esp, correo)

        c.execute(sql_command)
        conn.commit()
        conn.close()


    def actualizar_alumno_db(alumno):
        try:
            conn = sqlite3.connect(path)
        except:
            print("Error al conectar con la DB")
        c = conn.cursor()

        codigo = alumno.getcodigo()
        nombre = alumno.getnombre()
        horario = alumno.gethorario()
        esp = alumno.getespecialidad()
        correo = alumno.getcorreo()

        sql_command = "update IEE239 set nombre='{}', horario='{}', especialidad='{}', correo='{}' where codigo = '{}'".format (nombre, horario, esp, correo, codigo)
        c.execute(sql_command)
        conn.commit()
        conn.close()


    def borrar_alumno_db(alumno):
        try:
            conn = sqlite3.connect(path)
        except:
            print("Error al conectar con la DB")
        c = conn.cursor()

        codigo = alumno.getcodigo()

        sql_command = "delete from IEE239 where codigo = '{}'".format(codigo)
        c.execute(sql_command)
        conn.commit()
        conn.close()



    def listar_alumnos_db():
        
        try:
            conn = sqlite3.connect(path)
        except:
            print("Error al conectar con la DB")

        c = conn.cursor()

        c.execute("select * from IEE239;")
        record = c.fetchall()        
        
        conn.close()

        return record