#https://www.w3resource.com/python-exercises/math/
import math
import matplotlib.pyplot as plt
import numpy as np

# #Math exercise 1 convert degree to radian
# print("Ejercicio 1: grados a radianes")
# grados = input("Grados: ")
# radianes = float(grados) * math.pi/180
# print("Radianes: ", radianes)
def degree_to_radian(grados):
    return (float(grados) * math.pi/180)


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
# print("Ejercicio 6: volumen y area de una esfera")
# radio = float(input("Radio: "))
# volumen = 4/3 * math.pi * radio**3
# area = 4 * math.pi * radio ** 2
# print("Area", area)
# print("Volumen",volumen)

# xpoints = 0
# yvolumen = 0
# yarea = 0

# for x in range(50):
#     xpoints = np.append(xpoints,x)
#     volumen = 4/3 * math.pi * x**3
#     area = 4 * math.pi * x ** 2
#     yvolumen = np.append(yvolumen,volumen)
#     yarea = np.append(yarea,area)

# plt.plot(xpoints, yvolumen)
# plt.plot(xpoints, yarea)
# plt.show()

#Math exercise 7 calculate arc length of an angle
# print("Ejercicio 7: longitud del arco de un ángulo")
# diametro = int(input("Diametro: "))
# angulo = int(input("Ángulo: "))
# longitud = degree_to_radian(angulo) * diametro/2
# print("Longitud: ", longitud)

#Math exercise 8 calculate the area of the sector
print("Ejercicio 8: area de un sector")
radio = int(input("Radio: "))
angulo = int(input("Ángulo: "))
area =  radio ** 2 * degree_to_radian(angulo) /2
print("Area: ", area)