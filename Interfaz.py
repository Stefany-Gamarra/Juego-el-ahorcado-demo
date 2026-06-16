from Lógica import *


#verifica si funciona correctamente
palabras = cargar_palabras()
palabra  = elegir_palabra(palabras, "es", "animales")
estado   = nuevo_juego(palabra, max_intentos=6)

print("Palabra:", estado["palabra"])
print("Visible:", letras_correctas_visibles(estado))

adivinar_letra(estado, "A")
adivinar_letra(estado, "Z")   
print("Visible:", letras_correctas_visibles(estado))
print("Intentos:", estado["intentos_restantes"])  
