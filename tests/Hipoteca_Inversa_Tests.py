# Todas las pruebas unitarias importan la biblioteca unittest
import unittest

# Lo importamos para poder incluir la ruta de busqueda python
import sys
sys.path.append("src")

# Las pruebas importan el modulo que va a realizar todo el trabajo
import Logic.Hipoteca_Inversa_Calculator as Calcular_Hipoteca_Inversa
from Logic.Hipoteca_Inversa_Calculator import *

# Debe existir por lo menos una clase que contenga las pruyebas unitarias
# descediente de unittest.TestCase
class Hipoteca_Inversa_Test(unittest.TestCase):
    """
    Unit Tests for the calculate of a Reverse mortgage

    Pruebas Unitarias para el cálculo de una Hipoteca Inversa
    """
    # CASOS DE PRUEBA NORMALES (6)
    # Cada prueba unitaria es un metodo la clase
    def test_1(self):
        """ Hipoteca inversa normal con todos los parametros correctos """
        # DATOS DE ENTRADA
        valor_inmueble = 200000000
        edad = 70
        estado_civil = "divorciado"
        edad_conyugue = 0
        sexo_conyugue = "nn"
        tasa_interes = 9.8

        resultado = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)
        cuota =  116666.67
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )

    def test_2(self):
        """ Hipoteca inversa normal con todos los parametros correctos """
        # DATOS DE ENTRADA
        valor_inmueble = 50000000
        edad = 66
        estado_civil = "divorciado"
        edad_conyugue = 0
        sexo_conyugue = "nn"
        tasa_interes = 9.5

        resultado = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)
        cuota =  21990.74
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )

    def test_3(self):
        """ Hipoteca inversa normal con todos los parametros correctos """
        # DATOS DE ENTRADA
        valor_inmueble = 105000000
        edad = 75
        estado_civil = "casado"
        edad_conyugue = 80
        sexo_conyugue = "mujer"
        tasa_interes = 6.1

        resultado = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)
        cuota =  59305.56
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )
    
    def test_4(self):
        """ Hipoteca inversa normal con todos los parametros correctos """
        # DATOS DE ENTRADA
        valor_inmueble = 30000000
        edad = 70
        estado_civil = "casado"
        edad_conyugue = 75
        sexo_conyugue = "mujer"
        tasa_interes = 6.8

        resultado = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)
        cuota =  12142.86
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )

    def test_5(self):
        """ Hipoteca inversa normal con todos los parametros correctos """
        # DATOS DE ENTRADA
        valor_inmueble = 85000000
        edad = 76
        estado_civil = "casado"
        edad_conyugue = 79
        sexo_conyugue = "mujer"
        tasa_interes = 6.36

        resultado = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)
        cuota =  56312.50
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )

    def test_6(self):
        """ Hipoteca inversa normal con todos los parametros correctos """
        # DATOS DE ENTRADA
        valor_inmueble = 105000000
        edad = 65
        estado_civil = "divorciada"
        edad_conyugue = 0
        sexo_conyugue = "nn"
        tasa_interes = 7.9

        resultado = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)
        cuota =  32916.67
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )

    # CASOS DE PRUEBA EXCEPCIONALES (6)
    def testExcepcional_1(self):
        """ Hipoteca inversa con edad la persona cumple el requisito minimo, pero la edad del conyugue está por debajo de la edad minima """
        # DATOS DE ENTRADA
        valor_inmueble = 1000000000
        edad = 65
        estado_civil = "casado"
        edad_conyugue = 33
        sexo_conyugue = "mujer"
        tasa_interes = 7.9
        
        resultado = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)
        cuota =  346491.23
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )

    def testExcepcional_2(self): 
        """ Hipoteca inversa con edad de la persona por debajo de la edad minima, pero la edad del conyugue si cumple el requisito minimo"""
        # DATOS DE ENTRADA
        valor_inmueble = 1000000000
        edad = 47
        estado_civil = "casado"
        edad_conyugue = 78
        sexo_conyugue = "mujer"
        tasa_interes = 7.9

        resultado = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)
        cuota =  822916.67
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )

    def testExcepcional_3(self):
        """ Hipoteca inversa normal con todos los parametros correctos, pero la persona es soltero/a"""
        # DATOS DE ENTRADA
        valor_inmueble = 500000000
        edad = 66
        estado_civil = "soltero"
        edad_conyugue = 0
        sexo_conyugue = "nn"
        tasa_interes = 11.5

        resultado = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)
        cuota =  266203.7
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )

    def testExcepcional_4(self):
        """ Hipoteca inversa normal con todos los parametros correctos, pero la persona es viudo/a"""
        # DATOS DE ENTRADA
        valor_inmueble = 75000000
        edad = 70
        estado_civil = "viudo"
        edad_conyugue = 0
        sexo_conyugue = "nn"
        tasa_interes = 15.2

        resultado = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)
        cuota =  67857.14
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )

    def testExcepcional_5(self):
        """ Hipoteca inversa normal con todos los parametros correctos, pero la persona es viudo/a"""
        # DATOS DE ENTRADA
        valor_inmueble = 55000000
        edad = 65
        estado_civil = "viuda"
        edad_conyugue = 0
        sexo_conyugue = "nn"
        tasa_interes = 33.2

        resultado = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)
        cuota =  72460.32
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )

    def testExcepcional_6(self):
        """ Hipoteca inversa normal con todos los parametros correctos, pero la persona es soltero/a"""
        # DATOS DE ENTRADA
        valor_inmueble = 1000000000
        edad = 77
        estado_civil = "soltera"
        edad_conyugue = 0
        sexo_conyugue = "nn"
        tasa_interes = 7.2

        resultado = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)
        cuota =  666666.67
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )

    # CASOS DE PRUEBA DE ERROR (8)
    def testNegativo(self):
        """Hipoteca Inversa con algún dato negativo"""
        # DATOS DE ENTRADA
        valor_inmueble = 250000000
        edad = 80
        tasa_interes = -3
        estado_civil = "casado"
        edad_conyugue = 74
        sexo_conyugue = "mujer"
        self.assertRaises(Negative_Exception, Calcular_Hipoteca_Inversa.Logica, valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)

    def testCero_Hipoteca(self):
        """Hipoteca Inversa con valor del inmueble cero"""
        # DATOS DE ENTRADA
        valor_inmueble = 0
        edad = 82
        tasa_interes = 6.2
        estado_civil = "soltero"
        edad_conyugue = 0
        sexo_conyugue = "nn"
        self.assertRaises(Hipoteca_Exception, Calcular_Hipoteca_Inversa.Logica, valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)

    def testEdad_Fuera_del_Rango(self):
        """Hipoteca Inversa con las edades por debajo del requisito minimo"""
        # DATOS DE ENTRADA
        valor_inmueble = 1000000000
        edad = 57
        tasa_interes = 9.7
        estado_civil = "casado"
        edad_conyugue = 55
        sexo_conyugue = "mujer"
        self.assertRaises(Edad_Minima_Exception, Calcular_Hipoteca_Inversa.Logica, valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)

    def testCero_Tasa(self):
        """Hipoteca Inversa con valor de taza cero"""
        # DATOS DE ENTRADA
        valor_inmueble = 90000000
        edad = 65
        tasa_interes = 0
        estado_civil = "casado"
        edad_conyugue = 74
        sexo_conyugue = "mujer"
        self.assertRaises(Tasa_Exception, Calcular_Hipoteca_Inversa.Logica, valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)

    def testMinima_Hipoteca(self):
        """Hipoteca Inversa con valor del inmueble por debajo del minimo"""
        # DATOS DE ENTRADA
        valor_inmueble = 7000000
        edad = 63
        tasa_interes = 9.76
        estado_civil = "divorciado"
        edad_conyugue = 0
        sexo_conyugue = "nn"
        self.assertRaises(Hipoteca_Exception, Calcular_Hipoteca_Inversa.Logica, valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)

    def testCero_Tasa_2(self):
        """Hipoteca Inversa con valor de taza cero"""
        # DATOS DE ENTRADA
        valor_inmueble = 66000000
        edad = 66
        tasa_interes = 0
        estado_civil = "viudo"
        edad_conyugue = 0
        sexo_conyugue = "nn"
        self.assertRaises(Tasa_Exception, Calcular_Hipoteca_Inversa.Logica, valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)

    def testMaxima_Tasa(self):
        """Hipoteca Inversa con valor de taza por encima del valor maximo"""
        # DATOS DE ENTRADA
        valor_inmueble = 300000000
        edad = 82
        tasa_interes = 44
        estado_civil = "casado"
        edad_conyugue = 66
        sexo_conyugue = "mujer"
        self.assertRaises(Tasa_Exception, Calcular_Hipoteca_Inversa.Logica, valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)

    def testMinima_Tasa(self):
        """Hipoteca Inversa con valor de taza por debajo del valor minimo"""
        # DATOS DE ENTRADA
        valor_inmueble = 100000000
        edad = 69
        tasa_interes = 4.2
        estado_civil = "soltero"
        edad_conyugue = 0
        sexo_conyugue = "nn"
        self.assertRaises(Tasa_Exception, Calcular_Hipoteca_Inversa.Logica, valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)

# Ejecuta todos los test        
if __name__ == '__main__':
    unittest.main()