"""
     Programa: eva01.py
     Alumno:Perla
     Matricula:1723110335
     Fecha:29/01/2024
     """
class Profesores():#define la clase profesores 
    id = None#define el atributo id
    nombre = ""#define el atributo nombre 
    materias =[] #define el atributo materias 

    def __init__ (self, id, nombre):#define el constructor
            self.id = id#asigna el valor del pàrametro id
            self.nombre = nombre#asigna el valor de nombre
            print("Constructor objeto"+"Profesor")#imprime el mensaje 

    def califica(self):#define el constructor
            print(f"El profesor {self.nombre} califica evaluaciones de la materia {self.materias[0]}")#imprime el valor

    def pasaAsistencia(self):
            print(f"El profesor {self.nombre} pasa asistencia")

profesor1 = Profesores("111", "Profesor 1")
profesor1.materias.append("Materia 1")
profesor1.materias.append("Materia 2")
profesor1.califica()
profesor1.pasaAsistencia()

