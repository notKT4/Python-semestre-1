'''
Desarrollar un programa que al momento de ingresar los lados de un triangulo
(a, b y c) en consola, indique si es equilatero, isosceles o escaleno. Tambien se
solicita calcular el area utilizando la formula de Heron:
A**2 = p(p - a)(p - b)(p - c), donde p = (a + b + c)/2

'''

ladoA=float(input("Ingrese la medida del primer lado del triangulo \n"))
ladoB=float(input("Ingrese la medida del segundo lado del triangulo \n"))
ladoC=float(input("Ingrese la medida del tercer lado del triangulo \n"))

sp = (ladoA+ladoC+ladoB)/2
area = float((sp-ladoA)*(sp-ladoB)*(sp-ladoC))
	
if ladoA==ladoC==ladoB:
	print("El triangulo es equilatero")

if ladoA != ladoB != ladoC:
	print("El triangulo es escaleno")

if ladoA == ladoB and ladoB != ladoC and ladoA != ladoC:
	print("El triangulo es isosceles")
		
if ladoB == ladoC and ladoC != ladoA and ladoA != ladoB:
	print("El triangulo es isosceles")
		
if ladoC == ladoA and ladoC != ladoB and ladoA != ladoB:
    print("El triangulo es isosceles")

print(f"El semiperimetro corresponde a {sp}")
print(f"El area corresponde a {area}")