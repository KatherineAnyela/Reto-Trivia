BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

import time 
import random

#puntaje=random.randint(0,10)

iniciar_trivia= True
intentos=0

print(CYAN+"\nHola ʕ•́ᴥ•̀ʔっ \nbienvenido a mi trivia sobre diversos temas\n "+RESET)

#numero_carga
for num_c in range (5,0,-1):
  print(num_c)
  
time.sleep(1)
print (CYAN+"Pondremos a prueba tu conocimiento sobre diversos temas. Debes responder las siguientes preguntas escribiendo la letra de la alternativa y presiona 'Enter' para enviar tu respuesta."+RESET)

time.sleep(1)
print(CYAN+"\nTen en cuenta que al equivocarte se te restara puntaje!"+RESET)
#print(CYAN+"\nIniciaras con:"+RESET,RED+" ",puntaje,"puntos"+RESET)

time.sleep(2)
name = input(CYAN+"Ingresa tu nombre y presiona 'enter': "+RESET)

while iniciar_trivia==True:
  puntaje=random.randint(0,10)
  print(CYAN+"\nIniciaras con:"+RESET,RED+" ",puntaje,"puntos"+RESET)
  intentos+=1
  #puntaje=0

  print("\nIntento número: ", intentos)
  input("Presiona Enter para continuar")

  

  print(CYAN+"\nHola",name,"＼(^o^)／ responde a las siguientes preguntas escribiendo la letra de la alternativa correcta y presiona enter para enviar tu respuesta: "+RESET)
  time.sleep(2)

  print(" ")
  ##############################################################################################
  print("\n-------- PREGUNTA 1--------")
  print(GREEN+"\n¿Cuál fue el primer refresco que se llevó al espacio?"+RESET)
  print(BLUE+"\na) Pepsi"+RESET)
  print(BLUE+"b) Fanta"+RESET)
  print(BLUE+"c) Coca Cola"+RESET)
  print(BLUE+"d) Snapple\n"+RESET)
  r1=input(GREEN+"Escribe tu respuesta:"+RESET)
  
  while r1 not in ("a","b","c","d","k"):
    r1=input("\nDebes responder a,b,c,d. Ingresa nuevamente tu respuesta: ")
  if r1=="a":
    puntaje-=5
    print("\n˘︹˘ Incorrecto",name, ".Tu puntaje actual es:",puntaje,".")
  elif r1=="b":
    puntaje-=5
    print("\n˘︹˘ Incorrecto",name, ".Tu puntaje actual es:",puntaje,".")
  elif r1=="d":
    puntaje-=5
    print("\n˘︹˘ Incorrecto",name, ".Tu puntaje actual es:",puntaje,".")
  elif r1=="k":
    puntaje+=30
    print("\n\nEste es un mensaje secreto",name, "\nLos astranautas a bordo del transbordador espacial Challenger \nprobaron la Coca-Cola en una lata del espacio el \n12 de julio de 1985.")
    print(BLUE+"\nTu puntaje actual es:",puntaje,"."+RESET)
  else: 
    puntaje+=25
    print("\nMuy bien",name,".Tu puntaje actual es:",puntaje,".")
  
  
  
  time.sleep(2)

################################################################################################

  print("\n-------- PREGUNTA 2--------")
  print(GREEN+"\n¿Quién escribió un diario famoso mientras se escondía de los nazis en Amsterdam?"+RESET)
  print(BLUE+"\na) Anne Frank"+RESET)
  print(BLUE+"b) Bridget Jones"+RESET)
  print(BLUE+"c) Marie Curie"+RESET)
  print(BLUE+"d) Helen Keller\n"+RESET)
  r2=input(GREEN+"Cual es la respuesta:"+RESET)
  
  while r2 not in ("a","b","c","d","k"):
    r2=input("\nDebes ingresar nuevamente tu respuesta: ")
  if r2=="b":
    puntaje-=5
    print("\n˘︹˘ Incorrecto",name, ".Tu puntaje actual es:",puntaje,".")
  elif r2=="c":
    puntaje-=5
    print("\n˘︹˘ Incorrecto",name, ".Tu puntaje actual es:",puntaje,".")
  elif r2=="d":
    puntaje-=5
    print("\n˘︹˘ Incorrecto",name, ".Tu puntaje actual es:",puntaje,".")
  elif r2=="k":
    puntaje*=2
    print("\n\nEste es un mensaje secreto",name, "\nAnne Frank llamó al diario “Kitty”")
    print(BLUE+"\nTu puntaje actual es:",puntaje,"."+RESET)
  else: 
    puntaje+=25
    print("\nMuy bien",name,"!!!"".Tu puntaje actual es:",puntaje,".")
  
  time.sleep(2)  

  #################################################

  print("\n-------- PREGUNTA 3 --------")
  print(GREEN+"\n ¿Qué significa el término “piano”?"+RESET)
  print(BLUE+"\na) A un ritmo rápido"+RESET)
  print(BLUE+"b) Para tocar suavemente"+RESET)
  print(BLUE+"c) Moderadamente lento"+RESET)
  print(BLUE+"d) A un ritmo rápido\n"+RESET)
  r1=input(GREEN+"Cual es la respuesta:"+RESET)
  
  while r1 not in ("a","b","c","d","k"):
    r1=input("\nDebes ingresar nuevamente tu respuesta: ")
  if r1=="a":
    puntaje-=5
    print("\˘︹˘ Incorrecto",name, ".Tu puntaje actual es:",puntaje,".")
  elif r1=="c":
    puntaje-=5
    print("\n˘︹˘ Incorrecto",name, ".Tu puntaje actual es:",puntaje,".")
  elif r1=="d":
    puntaje-=5
    print("\n˘︹˘ Incorrecto",name, ".Tu puntaje actual es:",puntaje,".")
  elif r1=="k":
    puntaje*=2
    print("\n\nEste es un mensaje secreto",name, "\nEl piano se define como el nivel de sonido cuando la música se toca suavemente.")
    print(BLUE+"\nTu puntaje actual es:",puntaje,"."+RESET)
  else: 
    puntaje+=25
    print("\nMuy bien",name,"!!!"".Tu puntaje actual es:",puntaje,".")
  
  time.sleep(2)  

  #################################################
  
  print("\n-------- PREGUNTA 4 --------")
  print(GREEN+"\n En Los tres cerditos, ¿de qué está hecha la casa más fuerte?"+RESET)
  print(BLUE+"\na) Palos"+RESET)
  print(BLUE+"b) Ladrillos"+RESET)
  print(BLUE+"c) Paja"+RESET)
  print(BLUE+"d) Bambu\n"+RESET)
  r1=input(GREEN+"Cual es la respuesta:"+RESET)
      
  while r1 not in ("a","b","c","d","k"):
    r1=input("\nDebes ingresar nuevamente tu respuesta: ")
  if r1=="a":
    puntaje-=5
    print("\˘︹˘ Incorrecto",name, ".Tu puntaje actual es:",puntaje,".")
  elif r1=="c":
    puntaje-=5
    print("\n˘︹˘ Incorrecto",name, ".Tu puntaje actual es:",puntaje,".")
  elif r1=="d":
    puntaje-=5
    print("\n˘︹˘ Incorrecto",name, ".Tu puntaje actual es:",puntaje,".")
  elif r1=="k":
    puntaje*=2
    print("\n\nEste es un mensaje secreto",name, "\nEn la historia original, el lobo intentó entrar en la casa de ladrillos a través de la chimenea, pero cayó al agua caliente y murió..")
    print(BLUE+"Tu puntaje actual es:",puntaje,"."+RESET)
  else: 
    puntaje+=25
    print("\nMuy bien",name,"!!!"".Tu puntaje actual es:",puntaje,".")
      
  time.sleep(2)  


  print(RED+"\nGracias", name, "por jugar mi trivia, alcanzaste", puntaje, "puntos"+RESET)
  print("\n---------------------------------")
  print("\n¿Quieres jugar la trivia nuevamente?")
  repetir_trivia=input("\nIngresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  
  if repetir_trivia!="si":
    print("\n---------------------------------")
    print("\nEspero", name, "que te hayas divertido, Cuidate!! hasta pronto.")
    iniciar_trivia= False 

  