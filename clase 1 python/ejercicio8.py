nombre = str(input("¿Cuál es tu nombre?"))
edad = int(input("¿Cuál es tu edad?"))
nota1 = float(input("Ingresa tu primera nota"))
nota2 = float(input("Ingresa tu segunda nota"))
nota3 = float(input("Ingresa tu tercera nota"))
promedio = (nota1 + nota2 + nota3)/ 3
print("Tu promedio es ", promedio)
if promedio >= 71:
    print("aprobado")
else:
    print("reprobado")