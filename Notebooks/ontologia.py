from owlready2 import *

# agregar la carpeta que contiene la ontologia,
# para busqueda local, sino en internet
onto_path.append("../Data")

# carga de ontologia por IRI o por ruta directa al archivo owl

ontologia = get_ontology("http://www.semanticweb.org/OntologiaInvestigacionTest").load()

with ontologia:

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
        
        def set_estado_proyecto_investigacion(self,estado):
            self.estado_proyecto_investigacion.clear()
            self.estado_proyecto_investigacion.append(estado)

        def set_tipo_proyecto_investigacion(self,tipo):
            self.tipo_proyecto_investigacion.clear()
            self.tipo_proyecto_investigacion.append(tipo)

