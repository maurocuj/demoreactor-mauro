##Creación de un diccionario
#Python usa llaves ({ }) y dos puntos (:)

planet = {
    'name': 'Earth',
    'moons': 1
}

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

planet_moons = {
'mercury': 0,
'venus': 0,
'earth': 1,
'mars': 2,
'jupiter': 79,
'saturn': 82,
'uranus': 27,
'neptune': 14,
'pluto': 5,
'haumea': 2,
'makemake': 1,
'eris': 1
}
# #Los objetos de diccionario tienen un método get que puede usar para acceder a un valor mediante su clave
# #Si una clave no está disponible, get devuelve None 
# print(planet.get('name'),planet.get('moons'),planet.get('wibble'))

# #puede pasar la clave entre corchetes ([ ]), un acceso directo
# #si una clave no esta disponible, [ ] genera un error KeyError.
# print(planet['name'],planet['moons']) ##planet['wibble'])

#Modificación de valores de diccionario
#modificar valores dentro de un objeto de diccionario, con el método update. 
# planet.update({
#     'name': 'Jupiter',
#     'moons': 79
# })

#Al igual que se usa el acceso directo de corchetes ([ ]) para leer valores, se puede utilizar para modificar valores
planet['name'] = 'Jupiter'
planet['moons'] = 79

#Siempre que quiera crear una clave, asígnela como haría con una existente.
planet['orbital period'] = 4333
#Para quitar una clave, use pop. pop devuelve el valor y quita la clave del diccionario. 
planet.pop('orbital period')

#almacenar cualquier tipo de valor, incluidos otros diccionarios
planet['diameter (km)'] = {
    'polar' : 133709,
    'equatorial' : 142984
}
print(planet)

#Para recuperar valores en un diccionario anidado, debe encadenar corchetes o llamadas a get.
print(f'{planet["name"]} tiene: {planet["moons"]} luna(s)')
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

#El método keys() devuelve un objeto de lista que contiene todas las claves. Puede usar este método para iterar por todos los elementos del diccionario.
for key in rainfall.keys():
    print (f'{key}: {rainfall[key]}cm')

# Si quiere agregar a un valor en lugar de sobrescribirlo, puede comprobar si la clave existe mediante in.
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1
print(rainfall['december'])

#devuelve la lista de todos los valores de un diccionario sin sus claves correspondientes
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value
print(f'Hubo {total_rainfall}cm en el último trimestre')

moons = planet_moons.values()
total_planet = len(planet_moons.keys())

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

average = total_moons / total_planet
print(f'cada planeta tiene un promedio de {average} moons')

