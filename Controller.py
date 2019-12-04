import Modell


class Controller:
    @staticmethod
    def ingresar_alumno(al):
        #print("Ingresar No implementado")
        Modell.Modell.ingresar_alumno_db(al)

    @staticmethod
    def actualizar_alumno(al):
        #print("Actualizar No implementado")
        Modell.Modell.actualizar_alumno_db(al)

    @staticmethod
    def borrar_alumno(al):
        #print("Borrar No implementado")
        Modell.Modell.borrar_alumno_db(al)

    @staticmethod
    def listar_alumnos():
        #print("Borrar No implementado")
        return Modell.Modell.listar_alumnos_db()