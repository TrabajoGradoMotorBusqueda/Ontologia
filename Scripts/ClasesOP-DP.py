#############################################CREACION DE CLASES#################################################

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
        
        def set_clasificacion_grupo_investigacion(self,clasificacion_grupo_investigacion):
            self.clasificacion_grupo_investigacion = [clasificacion_grupo_investigacion]
        
        def get_area_grupo_investigacion(self):
            return self.area_grupo_investigacion
        
        def set_area_grupo_investigacion(self,area_grupo_investigacion):
            self.area_grupo_investigacion = [area_grupo_investigacion]
        
        def get_correo_grupo_investigacion(self):
            return self.correo_grupo_investigacion
        
        def set_correo_grupo_investigacion(self,correo_grupo_investigacion):
            self.correo_grupo_investigacion = [correo_grupo_investigacion]


    #SUBCLASE LINEA DE INVESTIGACION
    class Linea_investigacion(Grupo_investigacion):
        
        def get_id_linea_investigacion(self):
            return self.id_linea_investigacion
        
        def set_id_linea_investigacion(self, id_linea_investigacion):
            self.id_linea_investigacion = [id_linea_investigacion]
        
        def get_nombre_linea_investigacion(self):
            return self.nombre_linea_investigacion
        
        def set_nombre_linea_investigacion(self, nombre_linea_investigacion):           
            self.nombre_linea_investigacion = [nombre_linea_investigacion]
        
        
    #CLASE INVESTIGACION 
    class Investigador(Thing):
        
        def get_id_investigador(self):
            return self.id_investigador

        def set_id_investigador(self,id_investigador):
            self.id_investigador = [id_investigador]



        def get_nombres_investigador(self):
            return self.nombres_investigador

        def set_nombres_investigador(self,nombres_investigador):
            self.nombres_investigador = [nombres_investigador]



        def get_apellidos_investigador(self):
            return self.apellidos_investigador

        def set_apellidos_investigador(self,apellidos_investigador):
            self.apellidos_investigador = [apellidos_investigador]
        


        def get_codigo_investigador(self):
            return self.codigo_investigador

        def set_codigo_investigador(self,codigo_investigador):
            self.codigo_investigador = [codigo_investigador]
        


        def get_cedula_investigador(self):
            return self.cedula_investigador

        def set_cedula_investigador(self,cedula_investigador):
            self.cedula_investigador = [cedula_investigador]
        


        def get_correo_investigador(self):
            return self.correo_investigador

        def set_correo_investigador(self,correo_investigador):
            self.correo_investigador = [correo_investigador]
    

    #SUBCLASE DOCENTE INVESTIGADOR
    class Docente(Investigador):

        def get_id_docente(self):
            return self.id_docente
        
        def set_id_docente(self, id_docente):            
            self.id_docente = [id_docente]
        

    #SUBCLASE ESTUDIANTE INVESTIGADOR
    class Estudiante(Investigador)

        def get_id_estudiante(self):
            return self.id_estudiante
        
        def set_id_estudiante(self, id_estudiante):            
            self.id_estudiante = [id_estudiante]
        
        
    #SUBCLASE DOCENTE INVESTIGADOR
    class Investigador_externo(Investigador):
        
        def get_id_investigador_externo(self):
            return self.id_investigador_externo
        
        def set_id_investigador_externo(self, id_investigador_externo):
            self.id_investigador_externo = [id_investigador_externo]
        
        
    #CLASE PALABRA
    class Palabra(Thing):
        
        def get_id_palabra(self):
            return self.id_palabra

        def set_id_palabra(self,id_palabra):
            self.id_palabra = [id_palabra]



        def get_descripcion_palabra(self):
            return self.descripcion_palabra

        def set_descripcion_palabra(self,descripcion_palabra):
            self.descripcion_palabra = [descripcion_palabra]



        def get_lema_palabra(self):
            return self.lema_palabra

        def set_lema_palabra(self,lema_palabra):
            self.lema_palabra = [lema_palabra]



        def get_tipo_palabra(self):
            return self.tipo_palabra

        def set_tipo_palabra(self,tipo_palabra):
            self.tipo_palabra = [tipo_palabra]



        def get_concepto_palabra(self):
            return self.concepto_palabra

        def set_concepto_palabra(self,concepto_palabra):
            self.concepto_palabra = [concepto_palabra]


    #CLASE PROYECTO DE INVESTIGACION
    class Proyecto_investigacion(Thing):

        def set_id_proyecto_investigacion(self, id_proyecto_investigacion):
            self.id_proyecto_investigacion = [id_proyecto_investigacion]

        def set_titulo_proyecto_investigacion(self, titulo_proyecto_investigacion):
            self.titulo_proyecto_investigacion = [titulo_proyecto_investigacion]

        def set_resumen_proyecto_investigacion(self, resumen_proyecto_investigacion):
            self.resumen_proyecto_investigacion = [resumen_proyecto_investigacion]

        def set_estado_proyecto_investigacion(self, estado_proyecto_investigacion):
            self.estado_proyecto_investigacion = [estado_proyecto_investigacion]

        def set_tipo_proyecto_investigacion(self, tipo_proyecto_investigacion):
            self.tipo_proyecto_investigacion = [tipo_proyecto_investigacion]



        def get_id_proyecto_investigacion(self):
            return self.id_proyecto_investigacion

        def get_titulo_proyecto_investigacion(self):
            return self.titulo_proyecto_investigacion

        def get_resumen_proyecto_investigacion(self):
            return self.resumen_proyecto_investigacion

        def get_estado_proyecto_investigacion(self):
            return self.estado_proyecto_investigacion

        def get_tipo_proyecto_investigacion(self):
            return self.tipo_proyecto_investigacion


##FALTAN PALABRAS CLAVE OJO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##FALTAN PALABRAS CLAVE OJO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##FALTAN PALABRAS CLAVE OJO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##FALTAN PALABRAS CLAVE OJO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##FALTAN PALABRAS CLAVE OJO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


    #CLASE UNIVERSIDAD
    class Universidad(Thing):
        
        def set_id_universidad(self, id_universidad):        
            self.id_universidad = [id_universidad]

        def get_id_universidad(self):
            return self.id_universidad
        
        def set_nombre_universidad(self, nombre_universidad):            
            self.nombre_universidad = [nombre_universidad]

        def get_nombre_universidad(self):
            return self.nombre_universidad
                        

    #SUBCLASE FACULTAD
    class Facultad(Universidad):

        def set_id_facultad(self, id_facultad):
            self.id_facultad = [id_facultad]

        def get_id_facultad(self):
            return self.id_facultad
        
        def set_nombre_facultad(self, nombre_facultad):
            self.nombre_facultad = [nombre_facultad]

        def get_nombre_facultad(self):
            return self.nombre_facultad
        

    #SUBCLASE DEPARTAMENTO
    class Departamento(Facultad):
        def set_id_departamento(self, id_departamento):
            self.id_departamento = [id_departamento]
        
        def get_id_departamento(self):
            return self.id_departamento
        
        def set_nombre_departamento(self, nombre_departamento):
            self.nombre_departamento = [nombre_departamento]
        
        def get_nombre_departamento(self):
            return self.nombre_departamento

  
    #SUBCLASE PROGRAMA
    class Programa(Departamento):

        def set_id_programa(self, id_programa):
            self.id_programa = [id_programa]
        
        def get_id_programa(self):
            return self.id_programa

        def set_nombre_programa(self, nombre_programa):
            self.nombre_programa = [nombre_programa]
        
        def get_nombre_programa(self):
            return self.nombre_programa


    #CLASE VIIS
    class VIIS(Thing):
        def set_id_VIIS(self, id_VIIS):
            self.id_VIIS = [id_VIIS]
        
        def get_id_VIIS(self):
            return self.id_VIIS

        def set_nombre_VIIS(self, nombre_VIIS):
            self.nombre_VIIS = [nombre_VIIS]
        
        def get_nombre_VIIS(self):
            return self.nombre_VIIS

    #SUBCLASE CONVOCATORIA
    class Convocatoria(VISS):

        def set_id_convocatoria(self, id_convocatoria):
            self.id_convocatoria = [id_convocatoria]
        
        def get_id_convocatoria(self):
            return self.id_convocatoria

        def set_nombre_convocatoria(self, nombre_convocatoria):
            self.nombre_convocatoria = [nombre_convocatoria]
        
        def get_nombre_convocatoria(self):
            return self.nombre_convocatoria

        def set_tipo_convocatoria(self, tipo_convocatoria):
            self.tipo_convocatoria = [tipo_convocatoria]
        
        def get_tipo_convocatoria(self):
            return self.tipo_convocatoria

        def set_anio_convocatoria(self, anio_convocatoria):
            self.anio_convocatoria = [anio_convocatoria]
        
        def get_anio_convocatoria(self):
            return self.anio_convocatoria




#############################################CREACION DE DATA PROPERTIES#################################################


    with onto:
        class id_estudiante(DataProperty):
            range = [str]




#############################################CREACION DE OBJECT PROPERTIES#################################################

