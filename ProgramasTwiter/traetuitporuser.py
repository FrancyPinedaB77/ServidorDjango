from twitter import *
import json
from pymongo import MongoClient
from bson import Binary, Code
#Conexion a MongoDB
cliente = MongoClient()#Inicializar objeto
cliente = MongoClient('127.0.0.1', 27017)#Indicar parametros del servidor
bd = cliente.grupo14 #Seleccionar Schema
tweets = bd.pertemas  #Seleccionar Coleccion

#.........................autentificacion...........................
consumer_key= "1vZk3OJcUaiXf1Qe63sRjyCEa"
consumer_secret="hlpnMlZ0ET00KsIluWsDZdHpXrefs6k5DG1sl2jZ5LVl44rnaq"
access_token= "341615632-Hr8Uzc0i9v6e416rRoq5QqlAYLpZrJS9PCqpZbYH"
access_secret="tKz9cnH5E8NDTzWG4MtWrBWGox1wPua71RUDgSFxG1vrl"

twitter = Twitter(auth = OAuth(access_token, access_secret, consumer_key, consumer_secret))


names=["@JuanManSantos","@AlvaroUribeVel","@petrogustavo","@mluciaramirez","@AABenedetti","@ERobledo","@IvanCepedaCast","@piedadcordoba","@AntanasMockus","@jcvelezuribe","@DanielSamperO","@saludhernandezm","@CristoBustos","@sergio_fajardo","@Timochenko_FARC","@IvanMarquezFARC","@German_Vargas","@ELTIEMPO","@ClaudiaLopez","@RevistaSemana","@VickyDavilaH"]
for recor in names:
	results = twitter.statuses.user_timeline(screen_name =recor, count=100)
	for r in results:
		tweets.insert_one(r)








