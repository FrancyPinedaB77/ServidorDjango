from django.shortcuts import render
import ner
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

# Create your views here.
def taller4_parte1(request):
    b="funciona"
    st = StanfordNERTagger('/home/xubuntu/Taller4/nueva/classifiers/english.all.3class.distsim.crf.ser.gz','/home/xubuntu/Taller4/nueva/stanford-ner.jar', encoding='utf-8')
    text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'
    tokenized_text = word_tokenize(text)
    classified_text = st.tag(tokenized_text)
    print(classified_text)
    return render(request, "taller4_parte1.html",{"classified_text":classified_text,"b":b})


def taller4_parte2(request):
    numero2=78
    return render(request, "taller4_parte2.html",{"numero2":numero2})

def taller4_parte3(request):
    numero3=79
    return render(request, "taller4_parte3.html",{"numero3":numero3})
