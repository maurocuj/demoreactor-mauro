fact = "En luna no hay atmosfera"
two_facts = fact + " ,No hay sonido fuertes en la luna"
print(two_facts)

print('The "near side" is the part of the Moon that faces the Earth')

print("we only see about 60% of the Moon's surface")

print("""we only see about 60% of the Moon's surface, this is know as the "near side".""")

#multilinea
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound"
print(multiline)

print("Temperatura and facts about the moon".title())
heading = "temperatures and facts about the moon"
heading.title()

#separa la cadena en cada espacio, en una lista de todas las palabras o número separados por un espacio.
temperatures = """Daylight: 260 F 
Nighttime: -280 F"""
print(temperatures .split())

#Dividir la cadena final de cada linea, y crear líneas únicas
temperatures = """Daylight: 260 F 
Nighttime: -280 F"""
print(temperatures .split('\n'))

#Encontrar una palabra u caracter o un grupo de caracteres determinados.
print("Moon" in "This text will describe facts and challenges with space travel")
print("Moon" in "This text will describe facts about the Moon")
temperatures = "Saturno tiene una temperatura diurna de -170 grados centígrados, ... mientras que Marte tiene -28 Celsius"
print(temperatures.find("luna"))
temperatures = "Saturno tiene una temperatura diurna de -170 grados centígrados, ... mientras que Marte tiene -28 Celsius"
print(temperatures.find("Marte"))

#contar el total de repeticiones de una palabra u caracter o un grupo de caracteres determinada en una cadena
temperatures = "Saturno tiene una temperatura diurna de -170 grados centígrados, ... mientras que Marte tiene -28 Celsius"
print(temperatures.count("luna"))
temperatures = "Saturno tiene una temperatura diurna de -170 grados centígrados, ... mientras que Marte tiene -28 Celsius"
print(temperatures.count("-"))

#Destinguir MAYUSCULAS DE minusculas
print ("The Moon And The Earth".lower())
#Destinguir minusculas de MAYUSCULAS
print ("The Moon And The Earth".upper())

#Extraer información con una expresión irregular con un texto "regular".
temperatures = "La temperatura promedio en marte es: -60 C"
parts = temperatures.split(':')
print(parts[0])
print(parts[-1])

#Extraer información con una expresión irregular con un texto "irregular".
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

mars_temperature = "The highest temperature on Mars is about -30 C"
for item in mars_temperature.split():
    if item.startswith('-'):
        print(item)

mars_temperature = "The highest temperature on Mars is about -30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print("Esta temperatura es positiva")
    elif item.endswith('C'):
            print('y esta en grados celcius')
    elif item.endswith('F'):
        print("y esta en grados fahrenheit")
    elif item.startswith('-'):
        print("Esta temperatura es negativa")    
    elif item.endswith('C'):
            print('y esta en grados celcius')
    elif item.endswith('F'):
        print(" y esta en grados fahrenheit")

def is_number(letra):
    try:
        complex(letra)
        return True
    except ValueError:
        return False
mars_temperature = "The highest temperature on Mars is about -20.30 C"
for item in mars_temperature.split():
    if is_number(item):
        print("la temperatura es", item)

#Buscar y reemplazar repeticiones de un caracter o grupo de caracteres:
text = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."
replace = text.replace("Celsius" , "C")
print(replace)

#normalizar el texto para realizar una busqueda sin distinguir mayusculas de minusculas
text = "Temperatures on the Moon can vary wildly"
temperatures = "temperatures" in text
print(temperatures)
text = "Temperatures on the Moon can vary wildly"
temperatures= "temperatures" in text.lower()
print(temperatures)

#Volver a gruparlos
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
join = '\n'.join(moon_facts)
print(join)

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
sentence = text.split('. ')
print(sentence)

for sentence in sentence:
    if "temperature" in sentence:
        print(sentence)