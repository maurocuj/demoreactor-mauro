planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets[3] = 'Red Planet' #modificar valores de una lista mediante un índice
planets.append('Pluto') #Agregar un elemento al último a la cadena.
planets.pop() #Eliminar el último elemento de una lista.

print("El primer planetas es", planets[0])
print("El segundo planeta es", planets[1])
print("El tercero planeta es", planets[2])
print("El cuarto planeta es", planets[3])
print("El quinto planeta es", planets[4])
print("El sexto planeta es", planets[5])
print("El septimo planeta es", planets[6])
print("El octavo planeta es", planets[7])
#Los índices comienzan en cero y van en aumento. Los índices negativos comienzan al final de la lista y van hacia atrás.
print("El ultimo planeta es", planets[-1])
print("El penultimo planeta es", planets[-2])

#Para obtener la longitud de una lista
numeros_planetas = len(planets)
print("son", numeros_planetas, "planetas los que componen nuestro sistema solar")

#determinar dónde se almacena un valor en una lista
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

#puede averiguar el peso de un autobús de dos pisos en diferentes planetas obteniendo el valor de la lista:
planetas = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
gravedad_planetas = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
peso_autobus = 12650 # en kilogramos, en la tierra

print ("en", planetas[0], f"un autobus de doble piso con un peso de {peso_autobus} kg , pesa",f"{peso_autobus*gravedad_planetas[0]} kg")
print ("en", planetas[1], f"un autobus de doble piso con un peso de {peso_autobus} kg , pesa",f"{peso_autobus*gravedad_planetas[1]} kg")
print ("en", planetas[2], f"un autobus de doble piso con un peso de {peso_autobus} kg , pesa",f"{peso_autobus*gravedad_planetas[2]} kg")
print ("en", planetas[3],f"un autobus de doble piso con un peso de {peso_autobus} kg , pesa",f"{peso_autobus*gravedad_planetas[3]} kg")
print ("en", planetas[4],f"un autobus de doble piso con un peso de {peso_autobus} kg , pesa",f"{peso_autobus*gravedad_planetas[4]} kg")
print ("en", planetas[5],f"un autobus de doble piso con un peso de {peso_autobus} kg , pesa",f"{peso_autobus*gravedad_planetas[5]} kg")
print ("en", planetas[6],f"un autobus de doble piso con un peso de {peso_autobus} kg , pesa",f"{peso_autobus*gravedad_planetas[6]} kg")
print ("en", planetas[7],f"un autobus de doble piso con un peso de {peso_autobus} kg , pesa",f"{peso_autobus*gravedad_planetas[7]} kg")

#funciones integradas para calcular los números más grandes y más pequeños de una lista
print("En la", planetas[2], f"un autobus de dos pisos pesa {peso_autobus}kg")
print(f"Lo más ligero que sería un autobús en el sistema solar es de {peso_autobus * min(gravedad_planetas)} kg")
print(f"Lo más pesado que sería un autobús en el sistema solar es de {peso_autobus * max(gravedad_planetas)}kg")

#Recuperar una parte de una lista mediante una segmentación

planetas = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
#se usa una segmentación, se crea una lista que comienza en el índice inicial y termina antes del índice final (y no lo incluye).
planetas_antes_tierra = planetas[0:2]
#razón es que el índice de Neptuno es 7, porque la indexación comienza en 0. Dado que el índice final era 8, incluye el último valor.
planeta_despues_tierra = planetas[3:8]
#Si no coloca el índice de detención en la segmentación, Python asume que quiere ir al final de la lista:
planeta_despues_tierra = planetas[3:]
print(planetas_antes_tierra, planeta_despues_tierra)


##Combinación de listas
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]
#Únalas mediante + para crear una lista
regular_satellite_moons = amalthea_group + galilean_moons
#Para ordenar una lista, use el método .sort()
regular_satellite_moons.sort()
#Para ordenar una lista en orden inverso, llame a .sort(reverse=True) 
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune"]
user_planet = input("Please enter the name of the planet (with a capital letter to start): ")
planet_index = planets.index(user_planet)
print("Aquí están los planetas que estan antes de", user_planet ,":",planets[0:planet_index])
print("Aquí están los planetas que estan despues de", user_planet ,":",planets[planet_index:])