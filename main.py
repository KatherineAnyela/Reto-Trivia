import random

puntaje=random.randint(0,10)
print("\nHola ʕ•́ᴥ•̀ʔっ \nbienvenido a mi trivia sonbre lo fundamental\n ")
print("Pondremos a pruebas tus conocimientos basicos")
print("\n Iniciaras con,",puntaje,"puntos")
name=input("\n Ingresa tu nombre: ")

print("\nHola",name,"＼(^o^)／ responde a las siguientes preguntas escribiendo la letra de la alternativa correcta y presiona enter para enviar tu respuesta: ")
print(" ")
##############################################################################################
print("\n-------- PREGUNTA 1--------")
print("\n¿Cuál fue el primer refresco que se llevó al espacio?")
print("\na) Pepsi")
print("b) Fanta")
print("c) Coca Cola")
print("d) Snapple\n")
r1=input("Escribe tu respuesta:")

while r1 not in ("a","b","c","d","k"):
  r1=input("\nDebes responder a,b,c,d. Ingresa nuevamente tu respuesta: ")
if r1=="a":
  puntaje-=1
  print("\n˘︹˘ Incorrecto",name, "Fue la Coca Cola ")
elif r1=="b":
  puntaje-=1
  print("\n˘︹˘ Incorrecto",name, "Fue la Coca Cola ")
elif r1=="d":
  puntaje-=1
  print("\n˘︹˘ Incorrecto",name, "Fue la Coca Cola ")
elif r1=="k":
  puntaje+=20
  print("\n\nEste es un mensaje secreto",name, "\nLos astranautas a bordo del transbordador espacial Challenger \nprobaron la Coca-Cola en una lata del espacio el \n12 de julio de 1985.")
else: 
  puntaje+=10
  print("\nMuy bien",name,"sigue asi")

print("Por ahora llevas",puntaje,"puntos")
################################################################################################

print("\n-------- PREGUNTA 2--------")
print("\n¿Quién escribió un diario famoso mientras se escondía de los nazis en Amsterdam?")
print("\na) Anne Frank")
print("b) Bridget Jones")
print("c) Marie Curie")
print("d) Helen Keller\n")
r1=input("Cual es la respuesta:")

while r1 not in ("a","b","c","d","k"):
  r1=input("\nDebes ingresar nuevamente tu respuesta: ")
if r1=="b":
  puntaje-=1
  print("\n˘︹˘ Incorrecto",name, "La que escribio el diario fue Anne Frank")
elif r1=="c":
  puntaje-=1
  print("\n˘︹˘ Incorrecto",name, "La que escribio el diario fue Anne Frank")
elif r1=="d":
  puntaje-=1
  print("\n˘︹˘ Incorrecto",name, "La que escribio el diario fue Anne Frank")
elif r1=="k":
  puntaje+=20
  print("\n\nEste es un mensaje secreto",name, "\nAnne Frank llamó al diario “Kitty”.")
else: 
  puntaje+=10
  print("\nMuy bien",name,"!!!")
print("Por ahora llevas",puntaje,"puntos")
#################################################

print("\n-------- PREGUNTA 3 --------")
print("\n ¿Qué significa el término “piano”?")
print("\na) A un ritmo rápido")
print("b) Para tocar suavemente")
print("c) Moderadamente lento")
print("d) A un ritmo rápido\n")
r1=input("Cual es la respuesta:")

while r1 not in ("a","b","c","d","k"):
  r1=input("\nDebes ingresar nuevamente tu respuesta: ")
if r1=="a":
  puntaje-=1
  print("\˘︹˘ Incorrecto",name, "Significa para ser tocado suavemente")
elif r1=="c":
  puntaje-=1
  print("\n˘︹˘ Incorrecto",name, "Significa para ser tocado suavemente")
elif r1=="d":
  puntaje-=1
  print("\n˘︹˘ Incorrecto",name, "Significa para ser tocado suavemente")
elif r1=="k":
  puntaje=+20
  print("\n\nEste es un mensaje secreto",name, "\nEl piano se define como el nivel de sonido cuando la música se toca suavemente.")
else: 
  puntaje+=10
  print("\nMuy bien",name,"!!!")

print("\n --------------------------------- \nGracias",name, "por jugar conmigo, \n\nTu puntaje final es:", puntaje)