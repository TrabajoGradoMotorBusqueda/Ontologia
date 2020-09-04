class programa_tiene_estudiante(ObjectProperty):
        domain = [Programa]
        range  = [Estudiante]
        inverse_property = estudiante_pertenece_programa
  
    #SUBCLASE PROGRAMA
    class Programa(Departamento):
        def relation_programa_tiene_estudiante(self, estudiante):
            self.programa_tiene_estudiante.append(estudiante)

        programa = Programa("Sistemas")
        programa.programa_tiene_estudiante(clase a ser relacionada)
