#Importamos las palabras
import json
#Importamos la librería random (integrada en python)
import random

#No está completo

#Cargar las palabras
def cargar_palabras (ruta = "palabras.json"):
    with open (ruta, encoding = "utf-8") as f:
        return json.load(f)
    


#Seleccionar una palabra
def elegir_palabra (palabras, idioma, categoria):
    
    #Seleccionar una palabra aleatoria
    if categoria == "aleatorio":
        todas = []
        for lista in palabras [idioma].values ():
            todas.extend (lista)
        return random.choice (todas).upper()
    
    #Seleccionar una palabra de un categoría específica
    return random.choice (palabras[idioma][categoria]).upper()



#Estado del juego
def nuevo_juego (palabra, max_intentos):
    
    #Devuelve un diccionario que representa el estado 
    return {
        "palabra":          palabra,           
        "letras_correctas": set(),             
        "letras_incorrectas": set(),           
        "intentos_restantes": max_intentos,    
        "max_intentos":     max_intentos,
        "terminado":        False,
        "gano":             False,
    }



#Funcion parea adivinar letra por letra
#Aún en contrucción por falta de pruebas
def adivinar_letra (estado, letra):
    
    #Recibe el estado y una letra
    letra = letra.upper()
    #Si ya fue usado devuelve el esatado
    if letra in estado ["letras_correctas"] or \
       letra in estado ["letras_incorrectas"] or \
       estado ["terminado"]:
        return estado
    
    #Si la letra está en palabra lo añade a palabras_corrctas, sino a palabras incorrectas y resta un intento
    if letra in estado ["palabra"]:
        estado ["letras_correctas"].add(letra)
    else:
        estado ["letras_incorrectas"].add(letra)
        estado ["intentos_restantes"] -= 1
        verificar_fin (estado)
        
    return estado



#Función para adivinar la palabra completa
#Falta comprobar que funcione
def adivinar_palabra(estado, intento):
    if estado["terminado"]:
        return estado
    
    #Si adivina correctamente revela todas las letras sino pierde automáticamente
    if intento.upper() == estado["palabra"]:
        estado ["letras_correctas"] = set(estado["palabra"])
        estado ["terminado"] = True
        estado ["gano"] = True
    else:
        estado ["terminado"] -= True
        estado ["gano"] = False        
        
    return estado


#Revisa si gano con todas las letras o perdió por no tener intentos
def verificar_fin (estado):
    letras_unicas = set (estado["palabra"])
    
    if letras_unicas <= estado ["letras_correctas"]:
        estado ["terminado"] = True
        estado ["gano"] = True
    elif estado ["intentos_restantes"] <= 0:
        estado ["terminado"] = True
        estado ["gano"] = False



#Hace que las letras correctas sean visibles en vez del guión bajo
def letras_correctas_visibles (estado):
    return [
        letra if letra in estado ["letras_correctas"] else "_"
        for letra in estado ["palabra"]
    ]