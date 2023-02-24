from punto_polar2 import Punto_Polar, Numero_Complejo

p1 = Punto_Polar(2.50, 45)
p2 = Punto_Polar(3, 125)
n1 = Numero_Complejo(1, 1)
n2 = Numero_Complejo(6, 3)
n3 = Numero_Complejo(81, 0)
print("=========================\n"
      "OPERACIONES DE POLARES\n"
      "=========================")
print(p1)
print(p1 * p2)
print(-p2)
print(p1 / p2)
print(p1 ** 2)
print(p1.polar_complejo())
print("=========================\n"
      "OPERACIONES DE NÚMEROS COMPLEJOS\n"
      "=========================")
print(n1)
print(n1.conj())
print(-n2)
print(n1 + n2)
print(n1 + 3)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 ** 4)
n3.rad(4)
print(n1.complejo_polar())
