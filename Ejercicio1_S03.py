import random
import logging
import sys
logging.basicConfig(format='%(asctime)s %(message)s')

logger_1 = logging.getLogger("Mi_logger")
log_handler = logging.StreamHandler(sys.stdout)
log_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - $(message)s - %(funcName)s - line %(lineno)d"))

log_handler.setLevel(logging.DEBUG)
logger_1.addHandler(log_handler)
logger_1.setLevel(logging.DEBUG)

logger_1.info("INICIO DEL PROGRAMA")

numero_random = (random.randint(10, 60))
print("Número aleatorio que se genera" ,numero_random)

lista = []

while True:
    try:
     print("Adivine el número generado")
     intentos = int(input("Introduzca número intentos permitidos: "))

     if intentos > 0:
         break

    except ValueError:
     #print("El valor introducido no es correcto")
     logging.error("El valor introducido no es correcto")

while True:
    try:
       numero_entrada = int(input("Introduzca número: "))
       lista.append(numero_entrada)
    except ValueError:
        #print("El valor introducido no es correcto.")
        logging.error("El valor introducido no es correcto")

    try:
     if numero_entrada > numero_random:
        intentos = intentos - 1
        print("Intento erróneo. El número a adivinar es menor," ,intentos, "intentos disponibles")
     elif numero_entrada < numero_random:
        intentos = intentos - 1
        print("Intento erróneo. El número a adivinar es mayor" ,intentos, "intentos disponibles")
     elif numero_entrada == numero_random:
        print("Has acertado el número!! es:" ,numero_random, "Los intentos fueron los siguientes:", lista[:])
        break

     if intentos <= 0:
        print("Ya no tienes más intentos los intentos fueros " ,lista[:])
        break

    except NameError:
        logging.warning("El valor introducido no es correcto")

logger_1.info("FIN DEL PROGRAMA")

