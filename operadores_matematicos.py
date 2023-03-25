# a = 98
# b= 100
# # test expresion
# if a > b:
#     print("a es mayor que b")
# elif a < b:
#     print(" a es menor que b")
# else:
#     print ( "a es igual que b")

#anidación de secuencias 
# a = 29
# b = 29
# c = 27
# if a > b:
#     if b > c:
#         print ("a is greater than b and b is greater than c")
#     else: 
#         print ("a is greater than b and greater than c")
# elif a == b:
#     print ("a is equal to b")
# else:
#     print ("a is less than b")

# object_size = 10
# if object_size > 5:
#     print ('we need to keep an eye on this object')
# else:
#     print('object poses no threat')

# a = 23
# b = 24
# if a == 24 or b == 24:
#     print( a + b)
# else:
#     print(False)

# a = 24
# b = 24
# if a == 24 and b == 24:
#     print( a + b)
# else:
#     print(False)

object_size = 10
proximity = 9000

if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')