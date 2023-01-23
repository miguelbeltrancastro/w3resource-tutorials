#https://www.w3resource.com/python-exercises/math/
import math

# #Math exercise 1 convert degree to radian
# print("Ejercicio 1: grados a radianes")
# grados = input("Grados: ")
# radianes = float(grados) * math.pi/180
# print("Radianes: ", radianes)

# #Math exercise 2 convert radian to degree
# print("Ejercicio 2: radianes a grados")
# radianes = input("Radianes: ")
# grados = float(radianes) * 180/math.pi
# print("Grados: ", grados)

#Math exercise 3 calculate the area of a trapezoid
# print("Ejercicio 3: área de un trapezoide")
# altura = int(input("Altura: "))
# baseA = int(input("Base A: "))
# baseB = int(input("Base B: "))
# area = (baseA*altura)/2 + (baseB*altura)/2
# print("Area", area)

#Math exercise 4 calculate the area of a parallelogram
# print("Ejercicio 4: área de un paralelogramo")
# baseA = int(input("Base A: "))
# baseB = int(input("Base B: "))
# altura = math.sqrt(baseB*baseB-(baseA/2)*(baseA/2))
# area = (baseA*altura/2 + baseB*altura/2)
# print("Area", area)

#Math exercise 5 calculate surface volume and area of a cylinder
# print("Ejercicio 5: volumen y area de un cilindro")
# altura = int(input("Altura: "))
# radio = int(input("Radio: "))
# volumen = altura * math.pi * radio * radio
# area = (math.pi * radio * radio) * 2 + (2 * math.pi * radio * altura)
# print("Area", area)
# print("Volumen",volumen)

#Math exercise 6 calculate surface volume and area of a sphere
print("Ejercicio 6: volumen y area de una esfera")
radio = float(input("Radio: "))
volumen = 4/3 * math.pi * radio**3
area = 4 * math.pi * radio ** 2
print("Area", area)
print("Volumen",volumen)