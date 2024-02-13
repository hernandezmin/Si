
for _ in range(10):
    numerodecarne=input("ingrese el número de carné del alumno")
    if len(numerodecarne)==8:
        nombreyapellido=input("Ingrese el nombre y el apellido del alumno")
        print("Los alumnos y sus carnés son:" , numerodecarne, nombreyapellido)
    else:
        print("Carne invalido, alumno no ingresado")
    