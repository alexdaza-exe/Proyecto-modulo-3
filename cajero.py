#Simula un cajero: pide un monto, valida que sea múltiplo de 100, y muestra cuántos billetes de cada denominación se entregan.
#Entrada
from colorama import Fore, Back, Style, init
init(autoreset=True)


print("Bienvenido al cajero ATM BANCALI ")
correcta = "0000"
n = 0
cajero = 3890
while True:
    contra = input(" Ingrese su contraseña: ")
    if contra == correcta:
        print(Fore.GREEN + " Acceso concedido ")
        if n > 0:
            print(Fore.GREEN + f" El acceso se logro despues de: {n} intento(s) ")
            n = 0

        while True:
            op = int(input("Seleccione la opcion a realizar \n 1: Ingresar \n 2: Retirar \n 3: Salir "))

            if op == 1:
                print("---------------------------------------------")
                print("INGRESO")
                entrada= int(input("Cuanto dinero quiere ingresar: "))
                if entrada % 100 == 0:
                    cajero+=entrada
                    print(Fore.GREEN + f"El cajero Ingresa {entrada}")
                    print(f"Al cajero le resta {cajero}")
                    print("---------------------------------------------")

            elif op == 2:
                print("---------------------------------------------")
                print("RETIRO")

                salida = int(input("Cuanto dinero quiere retirar: "))

                if salida <= 0:
                    print(Fore.ORANGE + "El monto debe ser mayor que cero.")

                elif salida % 100 != 0:
                    print(Fore.ORANGE + "El cajero solo entrega multiplos de 100.")

                elif salida > cajero:
                    print(Fore.RED + "Fondos insuficientes en el cajero.")

                else:
                    restante = salida

                    billetes_1000 = restante // 1000
                    restante = restante % 1000

                    billetes_500 = restante // 500
                    restante = restante % 500

                    billetes_200 = restante // 200
                    restante = restante % 200

                    billetes_100 = restante // 100
                    restante = restante % 100

                    cajero = cajero - salida

                    print(Fore.GREEN + "Retiro exitoso.")
                    print(f"Billetes de $1000: {billetes_1000}")
                    print(f"Billetes de $500: {billetes_500}")
                    print(f"Billetes de $200: {billetes_200}")
                    print(f"Billetes de $100: {billetes_100}")
                    print(f"Total entregado: ${salida}")
                    print(f"Saldo restante del cajero: ${cajero}")

                    print("---------------------------------------------")

            elif op == 3:
                print("saliendo...")
                break

            else:
                print(Fore.ORANGE + "Opcion invalida...retornando")

            otra = int(input("Desea realizar otra operacion? \n 1- si.  \n 2- No."))
            if otra == 1:
                continue
            else:
                print("Saliendo..")
                break
    else:
        n += 1
        if n == 3:
            print(Fore.RED + f" Cuenta bloqueada, intentos fallidos {n} ")
            break
        else:
            restantes = 3 - n
            print(" Contraseña incorrecta, acceso denegado ")
            print(Fore.CYAN + f" Intento(s) restante(s): {restantes}. ")