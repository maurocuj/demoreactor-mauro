# answer = 30 / 12
# print(answer)

#Obetener segundos a minutos con una division de multiplo inferior (//) y usando el operador resto (%)
# seconds = 1042
# display_minuts= seconds // 60
# display_seconds = seconds % 60
# print(f"{seconds} segundos", f"es igual a {display_minuts} minutos", f"con {display_seconds} segundos")

# result_1 = 1032 + 26 * 2 + 2 - 1 / 2
# result_2 = 1032 + (26 * 2) + (2-1 / 2)
# print(result_1 , result_2)

# first_planet = 149597870
# second_planet = 778547200

# distance_km = second_planet - first_planet 
# print("La distancia en km entre los dos planetas es" , distance_km)

# distance_mi = distance_km / 1.609344
# print("La distancia en milla entre los dos planetas es" , distance_mi)


# demo_int = int('215')
# print(demo_int)
# demo_float = float('215.3')
# print(demo_float)

#
# print(39 - 16, 16 - 39)

#usar abs para convertir el valor negativo en su valor absoluto 
# print(abs(39 - 16) , abs(16 - 39))

##usar round parqa rendondear hacia arriba o abajo al entero más cercano.
# print(round(14.5))

# # Puede optar por redondear siempre hacia arriba al número entero más cercano si usa ceil, o hacia abajo si usa floor.
# from math import ceil, floor
# round_up = ceil(12.5)
# print(round_up)
# round_down = floor(12.5)
# print(round_down)


first_planet_input = input('Enter the distance from the sun for the first planet in KM: ')
second_planet_input = input('Enter the distance from the sun for the second planet in KM: ')

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)
distance_km = second_planet - first_planet
print(abs(distance_km))