from django.shortcuts import render
import ner
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import sys
import SPARQLWrapper
from SPARQLWrapper import SPARQLWrapper, JSON



# Create your views here.
def taller4_parte1(request):
    numero2=78
    return render(request, "taller4_parte1.html",{"numero2":numero2})

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
    st = StanfordNERTagger('/home/xubuntu/Taller4/nueva/classifiers/english.all.3class.distsim.crf.ser.gz','/home/xubuntu/Taller4/nueva/stanford-ner.jar', encoding='utf-8')
    text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'
    tokenized_text = word_tokenize(text)
    classified_text = st.tag(tokenized_text)
    print(classified_text)

    return render(request, "taller4_parte4.html",{"classified_text":classified_text,"b":b})