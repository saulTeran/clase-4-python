while True:
    print("ingrese su nombre")
    nombre=input()
    print("ingrese su edad")
    edad=int(input())
    print("ingrese su estado civil? (s)soltero (c)casado (p)pareja")
    estadoCivil=input().upper()
    if not estadoCivil == "S" or estadoCivil == "C" or estadoCivil == "P":
        print("tipo de letra invalido") 
    else:
        mayorEdad=(edad>=18)
    soltero=(estadoCivil=="S")
    casado=(estadoCivil=="C")
    pareja=(estadoCivil=="P")
    if mayorEdad:
        print(f"{nombre} es mayor de edad")
    else:
        print(f"{nombre} es menor de edad")
    #manera de hacerlo con not
    if not mayorEdad:
        print(f"{nombre} es menor de edad")
    else:
        print(f"{nombre} es mayor de edad")
    #estado civil con not
    if not soltero:
        print(f"{nombre} no esta solter@")
    else:
        print(f"{nombre} esta solter@")
    if not casado:
        print(f"{nombre} no esta casad@")
    else:
        print(f"{nombre} si esta casad@")
    if not pareja:
        print(f"{nombre} no tiene pareja")
    else:
        print(f"{nombre} tiene pareja")
    print("presione espacio para detener las ventas")
    resp=input()
    if resp==" ":
        break