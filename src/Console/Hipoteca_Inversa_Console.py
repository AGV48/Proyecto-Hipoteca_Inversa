# Lo importamos para poder incluir la ruta de busqueda python
import sys
sys.path.append("src")

# Se importa el modulo donde se realizarán los procesos
import Logic.Hipoteca_Inversa_Calculator as Calcular_Hipoteca_Inversa
from Logic.Hipoteca_Inversa_Calculator import *

# Se le da una bienvenida al usuario y se le muestra un menú con las opciones
def Bienvenida():
    print("-------------------------------------------")
    print("    BIENVENIDO A EL BANCO   ")
    print("¿Qué deseas hacer?")
    print(" 1. Obtener una hipoteca inversa \n 0. Salir")
    opcion = int(input("Elija una opción: "))
    print("--------------------------------------")
    # Se llama a la siguiente función y se le pasa como parametro la opción que el usuario eligió
    return desiciones(opcion)

def desiciones(opcion):
    # Se hace uso del metodo try para lanzar una excepción si algo falla
    try:
        # Se usa el ciclo while para verificar cual opción escogio el usuario
        while opcion != 0:
            # Se verifica si la opción escogida por el usuario no está definida
            if opcion < 0 or opcion > 1:
                print("------------------------------------------------------------------")
                print("                  EL BANCO            ")
                print("La opción ingresada no es correcta, intente de nuevo")
                print("-------------------------------------------------------------------")
                # Se llama nuevamente al metodo de Bienvenida para reiniciar el proceso
                Bienvenida()
            # Se verifica si el usuario quiere calcular una hipoteca inversa
            if opcion == 1:
                print("---------------------------------------------------------------------")
                print("                     EL BANCO                 ")
                print("DATOS PERSONALES")
                # Se obtienen los datos de entrada
                valor_inmueble = float(input("Por favor ingrese el valor de la vivienda: "))
                edad = int(input("Por favor ingrese su edad actual: "))
                estado_civil = input("Por favor ingrese su estado civil: ")
                estado_civil = estado_civil.lower()
                if estado_civil == "casado" or estado_civil == "casada":
                    edad_conyugue = int(input("Por favor ingrese la edad de su conyugue: "))
                    sexo_conyugue = input("Por favor ingrese el genero de su conyugue: ")
                else:
                    edad_conyugue = 0
                    sexo_conyugue = ""
                tasa_interes = float(input("Ingrese la tasa de interes: "))
                print("-------------------------------------------------------------------------")

                # Se calcula el valor de cada cuota de la hipoteca inversa
                resultado = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)

                #Verifica que el resultado se haya calculado correctamente
                if resultado == None:
                    Bienvenida()

                # Se muestra el resultado redondeado
                print(f"El valor de cada cuota de la hipoteca inversa es de: {round(resultado,2)}")
                break
        # Se le da al usuario un mensaje de despedida al usuario cuando finaliza todo el proceso
        print("------------------------------------------------------------------")
        print("                  EL BANCO            ")
        print("Gracias por visitarnos, vuelva pronto")
        print("-------------------------------------------------------------------")
    # Se lanza un mensaje de error cuando algo falla
    except ValueError:
        print("------------------------------------------------------------------")
        print("                  EL BANCO            ")
        print("Hubo un ERROR, revisa que los datos ingresados sean correctos")
        print("-------------------------------------------------------------------")
        Bienvenida()
    except Exception as exc:
        print("------------------------------------------------------------------")
        print("                  EL BANCO            ")
        print(f"{exc}, intentalo nuevamente")
        print("-------------------------------------------------------------------")
        Bienvenida()

# Se llama la funcion para dar inicio al programa
Bienvenida()