inverse palabra_describe_pi some Palabra
inverse pi_tiene_palabra some Proyecto_investigacion

pi_tiene_palabra some Palabra
palabra_describe_pi some Proyecto_investigacion

Palabra and palabra_describe_pi some Proyecto_investigacion
Proyecto_investigacion and pi_tiene_palabra some Palabra


Palabra and palabra_describe_pi some pi1
Proyecto_investigacion and pi_tiene_palabra value arte

-- Proyecto tiene palabras
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX po: <http://www.semanticweb.org/OntologiaInvestigacionPrueba#>
SELECT ?Palabra
WHERE { ?Palabra po:palabra_describe_pi po:pi427. } 
LIMIT 100


-- Palabra describe PI

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX po: <http://www.semanticweb.org/OntologiaInvestigacionPrueba#>
SELECT ?Proyecto
	WHERE { ?Proyecto po:pi_tiene_palabra po:buscador.}



--directa
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX po: <http://www.semanticweb.org/OntologiaInvestigacionPrueba#>
select ?id_pi?Titulo?proyecto_investigacion (count(?id_pi)as ?c)
where{
        ?proyecto_investigacion po:pi_tiene_palabra ?palabra.
        ?proyecto_investigacion po:titulo_proyecto_investigacion ?Titulo.
        ?proyecto_investigacion po:id_proyecto_investigacion ?id_pi.
        ?palabra po:descripcion_palabra ?descripcion.
        FILTER (
            REGEX(str(?descripcion), 'descubrimiento','i')||
            REGEX(str(?descripcion), 'conocimiento','i')
        )
    }
group by ?id_pi?Titulo?proyecto_investigacion
order by DESC(?c)

--Inversa
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX po: <http://www.semanticweb.org/OntologiaInvestigacionPrueba#>
select ?id_pi?Titulo?proyecto_investigacion (count(?id_pi)as ?c)
where{
        ?palabras po:descripcion_palabra ?descripcion.
        ?palabras po:palabra_describe_pi ?proyecto_investigacion.
        ?proyecto_investigacion po:titulo_proyecto_investigacion ?Titulo.
        ?proyecto_investigacion po:id_proyecto_investigacion ?id_pi.
        FILTER (
            REGEX(str(?descripcion), 'descubrimiento','i')||
            REGEX(str(?descripcion), 'conocimiento','i')
        )
    }
group by ?id_pi?Titulo?proyecto_investigacion
order by DESC(?c)

