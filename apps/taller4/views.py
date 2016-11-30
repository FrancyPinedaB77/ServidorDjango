from django.shortcuts import render
#import ner
#from nltk.tag import StanfordNERTagger
#from nltk.tokenize import word_tokenize
import sys
import SPARQLWrapper
from SPARQLWrapper import SPARQLWrapper, JSON
from django.core.paginator import Paginator
from pymongo import MongoClient
import json

from conexionmongo import Connection

from bson.json_util import dumps
# Create your views here.
def taller4_parte1(request): #ESTA VISTA ME MUETRA LAS PREGUNTAS CON SU INFORMACION 
    conn = Connection()
    if request.GET.get('page') != None:
        PAGE = int(request.GET.get('page'))
    else:
        PAGE = 1
    #Conexion a MongoDB
    #cliente = MongoClient()#Inicializar objeto
    #cliente = MongoClient('127.0.0.1', 27017)#Indicar parametros del servidor
    #bd = cliente.taller4 #Seleccionar Schema
    coleccion =conn.bd.body_pregunta  #Seleccionar Coleccion  
    coleccion2=conn.bd.body_respuestas
    coleccion_con_movies=conn.bd.peliculas_en_preguntas

    #coleccion_con_tuitrespuesta=conn.bd.tuit_respuesta
    coleccion_con_tuitpregunta=conn.bd.tuit_preguntas

    count=coleccion.count()
    numero_preguntas_pagina=1
    consulta1= coleccion.find().skip(numero_preguntas_pagina * (PAGE-1)).limit(numero_preguntas_pagina)
    pregunta_for_front=coleccion.find().skip(numero_preguntas_pagina * (PAGE-1)).limit(numero_preguntas_pagina)
    consulta2= coleccion2.find().skip(numero_preguntas_pagina * (PAGE-1)).limit(numero_preguntas_pagina)
    consulta_movies=coleccion_con_movies.find().skip(numero_preguntas_pagina * (PAGE-1)).limit(numero_preguntas_pagina)

    consulta_tuitpregunta=coleccion_con_tuitpregunta.find().skip(numero_preguntas_pagina * (PAGE-1)).limit(numero_preguntas_pagina)
    
    #jsondata = {}
    n=1
    salida={}
    datos=[]
    for los_id_pregunta in pregunta_for_front:
        id_pregunta=int(los_id_pregunta.get("items")[0]["question_id"])  
        datos.append(id_pregunta)
    print datos


    datta=  coleccion2.find({"items.0.question_id": { '$in': datos} })
    movies= coleccion_con_movies.find({"items.0.question_id": { '$in': datos} })
    tuits= coleccion_con_tuitpregunta.find({"items.0.question_id": { '$in': datos} })

    print movies
    infoPage={'countPage': count, 'num_pages': count/numero_preguntas_pagina + 1, 'page':PAGE,'previous_page_number':PAGE-1, 'next_page_number':PAGE+1}
    return render(request, "taller4_parte1.html",{"consulta1":consulta1, "datta":datta,"movies":movies,"tuits":tuits ,"infoPage":infoPage})



def relationship (request):
    conn = Connection()
    if request.GET.get('page') != None:
        PAGE = int(request.GET.get('page'))
    else:
        PAGE = 1
    coleccion = conn.bd.body_pregunta  #Seleccionar Coleccion  
    count=coleccion.count()
    numero_preguntas_pagina=1
    consulta1= coleccion.find().skip(numero_preguntas_pagina * (PAGE-1)).limit(numero_preguntas_pagina)
    consulta2= coleccion.find().skip(numero_preguntas_pagina * (PAGE-1)).limit(numero_preguntas_pagina)
         
    infoPage={'countPage': count, 'num_pages': count/numero_preguntas_pagina + 1, 'page':PAGE,'previous_page_number':PAGE-1, 'next_page_number':PAGE+1}
    return render(request, "relation.html",{"consulta1":consulta1,"consulta2":consulta2,"infoPage":infoPage})

def taller4_parte2(request):
    numero2=78
    return render(request, "taller4_parte2.html",{"numero2":numero2})

def taller4_parte3(request):
    numero3=79
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?lat
    WHERE { <http://dbpedia.org/resource/Colombia> geo:lat ?lat }
""")
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        a=2
        #print (result["lat"]["value"]).decode(string)
    lat=(result["lat"]["value"]) 
    print lat   
    #Trae los valores de longitud 
    sparql.setQuery("""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?long
        WHERE { <http://dbpedia.org/resource/Colombia> geo:long ?long }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        a=2
        #print (result["long"]["value"])
    longit=(result["long"]["value"]) 
    print longit

    return render(request, "taller4_parte3.html",{"longit":longit,"lat":lat})


def taller4_parte4(request):
    b="funciona"

    return render(request, "taller4_parte4.html",{"b":b})