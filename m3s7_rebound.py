from os import system
from time import sleep
numero=int()
continuar = True
orden = ("primer",
         "segundo",
         "tercero",
         "cuarto",
         "quinto",
         "sexto",
         "septimo",
         "octavo",
         "noveno",
         "decimo")

while continuar:
    listaNros = []
    for contador in range(10):
        system("cls")
        numero=int(input(f"Ingrese el {orden[contador]} numero: "))
        listaNros.append(numero)
    system("cls")
    print("Los Numeros ingresados fueron los siguientes:")
    for n in listaNros:
        if n==0:
            print(f"{n}, este numero era CERO")
        elif n%2==0:
            print(f"{n}, este numero era PAR")
        else:
            print(f"{n}, este numero era IMPAR")
        sleep(1)
    opcion=input("Deseas probar de nuevo?: (s/n)").lower()
    if opcion !="s":
        continuar=False
