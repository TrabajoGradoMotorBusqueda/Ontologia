from owlready2 import *

# agregar la carpeta que contiene la ontologia,
# para busqueda local, sino en internet
onto_path.append("../Data")

# carga de ontologia por IRI o por ruta directa al archivo owl

ontologia = get_ontology(
    "http://www.semanticweb.org/OntologiaInvestigacionTest").load()

with ontologia:
    #GRUPO DE INVESTIGACION
    class Grupo_investigacion(Thing):

        def get_id_grupo_investigacion(self):
            return self.id_grupo_investigacion

        def set_id_grupo_investigacion(self,id_grupo_investigacion):
            self.id_grupo_investigacion = [id_grupo_investigacion]

        def get_nombre_grupo_investigacion(self):
            return self.nombre_grupo_investigacion
        
        def set_nombre_grupo_investigacion(self,nombre_grupo_investigacion):
            self.nombre_grupo_investigacion = [nombre_grupo_investigacion]

        def get_clasificacion_grupo_investigacion(self):
            return self.clasificacion_grupo_investigacion
        
        def set_clasificacion_grupo_investigacion(self,valor):
            self.clasificacion_grupo_investigacion = [valor]
        
        def get_area_grupo_investigacion(self):
            return self.area_grupo_investigacion
        
        def set_area_grupo_investigacion(self,valor):
            self.area_grupo_investigacion = [valor]
        
        def get_correo_grupo_investigacion(self):
            return self.correo_grupo_investigacion
        
        def set_correo_grupo_investigacion(self,valor):
            self.correo_grupo_investigacion = [valor]


    #SUBCLASE LINEA DE INVESTIGACION
    class Linea_investigacion(Grupo_investigacion):
        def get_id_linea_invetigacion(self):
            return self.id_linea_invetigacion[0]
        
        def set_id_linea_invetigacion(self, id_linea_invetigacion):
            self.id_linea_invetigacion.clear()
            self.id_linea_invetigacion.append(id_linea_invetigacion)
        
        def get_nombre_linea_investigacion(self):
            return self.nombre_linea_investigacion[0]
        
        def set_nombre_linea_investigacion(self, nombre_linea_investigacion):
            self.nombre_linea_investigacion.clear()
            self.nombre_linea_investigacion.append(nombre_linea_investigacion)
        
        
    #CLASE INVESTIGACION 
    class Investigador(Thing):
        
        def get_id_investigador(self):
            return self.id_investigador

        def set_id_investigador(self,valor):
            self.id_investigador = [valor]



        def get_nombres_investigador(self):
            return self.nombres_investigador

        def set_nombres_investigador(self,valor):
            self.nombres_investigador = [valor]



        def get_apellidos_investigador(self):
            return self.apellidos_investigador

        def set_apellidos_investigador(self,valor):
            self.apellidos_investigador = [valor]
        


        def get_codigo_investigador(self):
            return self.codigo_investigador

        def set_codigo_investigador(self,valor):
            self.codigo_investigador = [valor]
        


        def get_cedula_investigador(self):
            return self.cedula_investigador

        def set_cedula_investigador(self,valor):
            self.cedula_investigador = [valor]
        


        def get_correo_investigador(self):
            return self.correo_investigador

        def set_correo_investigador(self,valor):
            self.correo_investigador = [valor]
    

    #SUBCLASE DOCENTE INVESTIGADOR
    class Docente(Investigador):
        def get_id_docente(self):
            return self.id_docente[0]
        
        def set_id_docente(self, id_docente):
            self.id_docente.clear()
            self.id_docente.append(id_docente)
        

    #SUBCLASE ESTUDIANTE INVESTIGADOR
    class Estudiante(Investigador)
        def get_id_estudiante(self):
            return self.id_estudiante[0]
        
        def set_id_estudiante(self, id_estudiante):
            self.id_estudiante.clear()
            self.id_estudiante.append(id_estudiante)
        
        
    #SUBCLASE DOCENTE INVESTIGADOR
    class Investigador_externo(Investigador):
        def get_id_investigador_externo(self):
            return self.id_investigador_externo[0]
        
        def set_id_investigador_externo(self, id_investigador_externo):
            self.id_investigador_externo.clear()
            self.id_investigador_externo.append(id_investigador_externo)
        
        
    #CLASE PALABRA
    class Palabra(Thing):
        
        def get_id_palabra(self):
            return self.id_palabra[0]

        def set_id_palabra(self,valor):
            self.id_palabra = valor



        def get_descripcion_palabra(self):
            return self.descripcion_palabra[0]

        def set_descripcion_palabra(self,valor):
            self.descripcion_palabra = valor



        def get_lema_palabra(self):
            return self.lema_palabra

        def set_lema_palabra(self,valor):
            self.lema_palabra = valor 



        def get_tipo_palabra(self):
            return self.tipo_palabra[0]

        def set_tipo_palabra(self,valor):
            self.tipo_palabra = valor 



        def get_concepto_palabra(self):
            return self.concepto_palabra[0]

        def set_concepto_palabra(self,valor):
            self.concepto_palabra = valor


        def get_significado_palabra(self):
            return self.significado_palabra[0]

        def set_significado_palabra(self,valor):
            self.significado_palabra = valor         

    #CLASE PROYECTO DE INVESTIGACION
    class Proyecto_investigacion(Thing):

        def set_id(self, id_investigacion):
            self.id_proyecto_investigacion.clear()
            self.id_proyecto_investigacion.append(id_investigacion)

        def set_titulo(self, titulo):
            self.titulo_proyecto_investigacion.clear()
            self.titulo_proyecto_investigacion.append(titulo)

        def set_resumen(self, resumen):
            self.resumen_proyecto_investigacion.clear()
            self.resumen_proyecto_investigacion.append(resumen)

        def set_estado_proyecto_investigacion(self, estado):
            self.estado_proyecto_investigacion.clear()
            self.estado_proyecto_investigacion.append(estado)

        def set_tipo_proyecto_investigacion(self, tipo):
            self.tipo_proyecto_investigacion.clear()
            self.tipo_proyecto_investigacion.append(tipo)


    #CLASE UNIVERSIDAD
    class Universidad(Thing):
        
        def set_id_universidad(self, id_universidad):
            self.id_universidad.clear()
            self.id_universidad.append(id_universidad)

        def get_id_universidad(self):
            return self.id_universidad[0]
        
        def set_nombre_universidad(self, nombre_universidad):
            self.nombre_universidad.clear()
            self.nombre_universidad.append(nombre_universidad)

        def get_nombre_universidad(self):
            return self.nombre_universidad[0]
                        

    #SUBCLASE FACULTAD
    class Facultad(Universidad):
        def set_id_facultad(self, id_facultad):
            self.id_facultad.clear()
            self.id_facultad.append(id_facultad)

        def get_id_facultad(self):
            return self.id_facultad[0]
        
        def set_nombre_facultad(self, nombre_facultad):
            self.nombre_facultad.clear()
            self.nombre_facultad.append(nombre_facultad)

        def get_nombre_facultad(self):
            return self.nombre_facultad[0]
        

    #SUBCLASE DEPARTAMENTO
    class Departamento(Facultad):
        def set_id_departamento(self, id_departamento):
            self.id_departamento.clear()
            self.id_departamento.append(id_departamento)
        
        def get_id_departamento(self):
            return self.id_departamento[0]
        
        def set_nombre_departamento(self, nombre_departamento):
            self.nombre_departamento.clear()
            self.nombre_departamento.append(nombre_departamento)
        
        def get_nombre_departamento(self):
            return self.nombre_departamento[0]

  
    #SUBCLASE PROGRAMA
    class Programa(Departamento):

        def set_id_programa(self, id_programa):
            self.id_programa.clear()
            self.id_programa.append(id_programa)
        
        def get_id_programa(self):
            return self.id_programa[0]

        def set_nombre_programa(self, nombre_programa):
            self.nombre_programa.clear()
            self.nombre_programa.append(nombre_programa)
        
        def get_nombre_programa(self):
            return self.nombre_programa[0]


    #CLASE VIIS
    class VIIS(Thing):
        def set_id_VIIS(self, id_VIIS):
            self.id_VIIS.clear()
            self.id_VIIS.append(id_VIIS)
        
        def get_id_VIIS(self):
            return self.id_VIIS[0]

        def set_nombre_VIIS(self, nombre_VIIS):
            self.nombre_VIIS.clear()
            self.nombre_VIIS.append(nombre_VIIS)
        
        def get_nombre_VIIS(self):
            return self.nombre_VIIS[0]

    #SUBCLASE CONVOCATORIA
    class Convocatoria(VISS):

        def set_id_convocatoria(self, id_convocatoria):
            self.id_convocatoria.clear()
            self.id_convocatoria.append(id_convocatoria)
        
        def get_id_convocatoria(self):
            return self.id_convocatoria[0]

        def set_nombre_convocatoria(self, nombre_convocatoria):
            self.nombre_convocatoria.clear()
            self.nombre_convocatoria.append(nombre_convocatoria)
        
        def get_nombre_convocatoria(self):
            return self.nombre_convocatoria[0]

        def set_tipo_convocatoria(self, tipo_convocatoria):
            self.tipo_convocatoria.clear()
            self.tipo_convocatoria.append(tipo_convocatoria)
        
        def get_tipo_convocatoria(self):
            return self.tipo_convocatoria[0]

        def set_anio_convocatoria(self, anio_convocatoria):
            self.anio_convocatoria.clear()
            self.anio_convocatoria.append(anio_convocatoria)
        
        def get_anio_convocatoria(self):
            return self.anio_convocatoria[0]