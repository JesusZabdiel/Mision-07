#Jesús Zabdiel Sánchez Chávez
#Mision 07. Ciclos While


def dividir(divisor, dividendo):
    cociente = 0
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente += 1
    print ("El cociente es: ", cociente)
    print("El residuo es: " , dividendo)


def encontrarMayor():
    print ("Teclea una serie de números para encontrar el mayor.")
    numero = int(input("Teclea un número [-1 para salir]"))
    numeroMayor = -1
    while numero != -1:
        if numero >= numeroMayor:
            numeroMayor = numero
            numero = int(input("Teclea un número [-1 para salir]"))

        elif numero < numeroMayor:
            numero = int(input("Teclea un número [-1 para salir]"))

    if numeroMayor != -1:
        print ("El mayor es: ",numeroMayor)

    else:
        print ("No hay mayor")


def menu():

    print("Mision 07. Ciclos While")
    print("Autor: Jesús Zabdiel Sánchez Chávez")
    print("Matrícula: A01374964")
    print ("1. Caluclar divisoines")
    print("2. Encontrar el mayor")
    print ("3. Salir")
    opcion = int(input("Seleccione la opción que desea hacer: "))
    return opcion


def main():
    opcion = menu()
    while opcion != 3:
        if opcion == 1:
            dividendo = int(input(("Inserte el dividendo: ")))
            divisor = int(input("inserte el divisor: "))
            dividir(divisor, dividendo)
            opcion = menu()
        elif opcion == 2:
            encontrarMayor()
            opcion= menu()
        else:
            opcion = int(input("Error, teclea 1, 2 o 3: "))


    print("Termina programa")


main()