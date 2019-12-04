

class Alumno:

    def __init__(self):
        pass

    #def __init__(self, _codigo, _nombre, _horario, _especialidad, _correo):
    #    self.codigo = _codigo
    #    self.nombre = _nombre
    #    self.horario = _horario
    #    self.especialidad = _correo

    def setcodigo(self, _codigo):
        self.codigo = _codigo

    def setnombre(self, _nombre):
        self.nombre = _nombre

    def sethorario(self, _horario):
        self.horario = _horario

    def setespecialidad(self, _especialidad):
        self.especialidad = _especialidad

    def setcorreo(self, _correo):
        self.correo = _correo


    def getcodigo(self):
        return self.codigo

    def getnombre(self):
        return self.nombre

    def gethorario(self):
        return self.horario

    def getespecialidad(self):
        return self.especialidad

    def getcorreo(self):
        return self.correo