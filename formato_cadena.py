#incluir valores de variable en el texto
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage)

#incluir valores de variable en el texto con el metodo format()
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth" .format(mass_percentage))

#incluir valores de variable en el texto con el uso de f-strings()
mass_percentage = "1/6"
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")

#incluir varios valores de variables en el texto
print("""Both sides of the %s get the same amount of sunlight,
... but only one side is seen from %s because
... the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

#asignar variables repetidas varias veces
mass_percentage = "1/6"
print("You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth" .format("Moom",mass_percentage))

#asignar variables repetidas varias veces usando argumentos de palabras clave
mass_percentage = "1/6"
print("You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth" .format(moon="Moom", mass= mass_percentage))

mass_percentage = round(100/6, 1)
print(mass_percentage)

#con f-strings, no es necesario asignar un valor a una variable 
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")

#metodos de cadena validos
subject = "interesting facts about the moon"
f"{subject.title()}"
print(subject.title())

name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'
print(f"Gravity Facts about {name}\n" f"Planet Name:{planet}" '\n'f"Gravity on {name}:"f"{gravity} m/s2")

template = """Gravity Facts about {nameformat}
----------------------------------------
Planet Name: {planetformat}
Gravity on {nameformat}: {gravityformat} m/s2"""
print(template.format(nameformat= name, planetformat = planet, gravityformat = gravity))
