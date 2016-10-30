
import oauth, tweepy, sys, locale, threading 
import json
from time import localtime, strftime, sleep
from tweepy.auth import OAuthHandler
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from pymongo import MongoClient

#Conexion a MongoDB

cliente = MongoClient()#Inicializar objeto
cliente = MongoClient('127.0.0.1', 27017)#Indicar parametros del servidor
bd = cliente.grupo14 #Seleccionar Schema
tweets = bd.pertemas  #Seleccionar Coleccion
#.........................autentificacion...........................
consumer_key= "r0uT43uaNpYEBbvEyq5NGQkIo"
consumer_secret="KivRqULDd3jQjarIPCXtAvcOmLVjgYKqQrTtTKhxKDROWIiAAS"
access_token= "3876483507-fNfTsMYV8OEadRRG9K46jwWtoOYQyxJk7r0dNWT"
access_secret="FgZnK9RAWsA79jYZVf0aEBQ0ArLfHYV4Wx6kWsQ2TLFvz"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth) 

oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)

#...................parametro de busqueda  .........................

#elusuario="@RevistaSemana"

#...................EL PROGRAMA......................................followers
#for user in tweepy.Cursor(api.followers, screen_name=elusuario).items():
#    print user.screen_name

#DEFINIENDO TRAER TWEETS DE UNA MUESTRA 
twitter_stream = TwitterStream(auth=oauth)
#twitter = Twitter(auth=oauth)

#PARAMETROS DE BUSQUEDA
iterator = twitter_stream.statuses.filter(track="#ReformaTributariaColombia", language="es")

tweet_count = 200
for tweet in iterator:
    #print tweet
    tweet_count -= 1
    eltuit = json.dumps(tweet, indent=4, sort_keys = True,ensure_ascii=False).encode('utf8')
    tweets.insert_one(json.loads(eltuit))
    #print eltuit
    if tweet_count == 0:
        break	

       
#parametros=["#ProcesoDePaz","#ReformaTributariaColombia","plebiscito","#Plebiscito","#guajira","pensional en Colombia","marchas por la paz","ELN","paz en colombia","acuerdos","#AcuerdoYA","@JuanManSantos","@AlvaroUribeVel","@petrogustavo","@mluciaramirez","@AABenedetti","@ERobledo","@IvanCepedaCast","@piedadcordoba","@AntanasMockus","@jcvelezuribe","@DanielSamperO","@saludhernandezm","@CristoBustos","@sergio_fajardo","@Timochenko_FARC","@IvanMarquezFARC","@German_Vargas","@ClaudiaLopez","@VickyDavilaH"]     


#los que ya estan: #ProcesoDePaz






