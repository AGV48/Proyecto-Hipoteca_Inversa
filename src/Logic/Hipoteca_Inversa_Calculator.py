# CONSTANTES
# Maximun age allowed / Edad maxima permitida
ESPERANZA_VIDA_HOMBRES = 84
ESPERANZA_VIDA_MUJERES = 86

# Minimun age allowed / Edad minima permitida
EDAD_MINIMA = 62

# Minimum age allowed in months / Edad minima permitida en meses
MAXIMO_TIEMPO_RESTANTE = 252

# Months of the year / Meses del año
MESES_AÑO = 12

# Minimum property value / Valor minimo de la propiedad
VALOR_MINIMO_INMUEBLE = 10000000

# Maximun and minimun intrest rate allowed / Tasa de interes maxima y minima permitidas
INTERES_MINIMO = 6
INTERES_MAXIMO = 43

ESTADOS_CIVILES = ["soltero", "viudo", "casado", "divorciado", "soltera", "viuda", "casada", "divorciada"]
SEXOS = ["masculino", "femenino", "hombre", "mujer", "nn", ""]

# EXCEPCIONES
class Hipoteca_Exception(Exception):
    """ 
    Custom exception for property value above maximum, below minimum and zero

    Excepción personalizada para el valor de la propiedad por encima del máximo, 
    por debajo del mínimo y cero
    """
    def __init__(self, valor_inmueble):
        super().__init__(f"El valor: {valor_inmueble} es invalido, la propiedad debe tener un valor minimo de {VALOR_MINIMO_INMUEBLE}")

class Edad_Minima_Exception(Exception):
    """ 
    Custom exception for age below minimum

    Excepción personalizada para la edad por debajo del mínimo
    """
    def __init__(self, edad):
        super().__init__(f"La edad: {edad} es invalida, para aplicar a una hipoteca inversa se necesita tener una edad entre {EDAD_MINIMA} y {ESPERANZA_VIDA_HOMBRES}")

class Tasa_Exception(Exception):
    """ 
    Custom exception for interest rate above maximum, below minimum and zero

    Excepción personalizada para tasa de interés por encima del máximo, 
    por debajo del mínimo y cero
    """
    def __init__(self, interes):
        super().__init__(f"La tasa de interes: {interes} es invalida, El interes no debe ser menor a {INTERES_MINIMO} ni debe ser mayo a {INTERES_MAXIMO} ")

class Negative_Exception(Exception):
    """ 
    Custom exception for negative values

    Excepción personalizada para valores negativos
    """
    def __init__(self):
        super().__init__(f" No pueden haber valores negativos ")

class None_Exception(Exception):
    """ 
    Custom exception for None values

    Excepción personalizada para valores que sean None
    """
    def __init__(self):
        super().__init__(f" No pueden haber campos vacios ")


# Calcula el valor de las cuotas mensuales que el banco pagaría por una hipoteca inversa de una vivienda
#valor: valor de la propiedad
#interes: tasa de intereses mensual, expresado como porcentaje (multiplicada por 100)
#tiempo_restante: tiempo de vida estimado de la persona

class Calcular_Hipoteca_Inversa:
    def Calcular_Cuota_Mensual(valor_inmueble: float, interes: float, tiempo_restante: int):
        """
            Calculate the monthly payment for a reverse mortgage

            Calcula la cuota a pagar por una hipoteca inversa

            Parameters
            ----------

            valor_inmueble : float
                property value / valor del inmueble

            interes : float
                must not be zero or less than
                INTERES_MINIMO / Tasa minima de interes, valor positivo mayor que INTERES_MINIMO
                and must not be zero or greater than
                INTERES_MAXIMO / Tasa minima de interes, valor positivo mayor que INTERES_MAXIMO
            
            tiempo_restante : int
                Remaining life of the person in months / Tiempo de vida restante de la persona en meses

            Returns
            -------
            payment : float
                Monthly payment calculated. Not rounded / Pago mensual calculado. El resultado no esta redondeado
            
            Raises
            ------
            HipotecaException
                When the property value is zero or less than the value defined in VALOR_MINIMO_INMUEBLE

            EdadMinimaException
                When the person's age is below the value defined in EDAD_MINIMA

            TasaException
                When the interest rate is higher or lower than the value defined in INTERES_MINIMO, INTERES_MAXIMO

            NegativeException
                When any value is zero 
        """

        # Divide el porcentaje de la tasa por 100 para que quede en decimales
        porcentaje_tasa = interes / 100

        
        
        # Calcula el valor de la cuota mensual
        cuota_mensual = (valor_inmueble * porcentaje_tasa) / tiempo_restante
        return cuota_mensual


    def Logica(valor_inmueble: float, edad: int, estado_civil: str, edad_conyugue: int, sexo_conyugue: str, tasa_interes: float):
        
        Calcular_Hipoteca_Inversa.verificarValor_Inmueble(valor_inmueble)

        Calcular_Hipoteca_Inversa.verificarEdad(edad, edad_conyugue)

        Calcular_Hipoteca_Inversa.verificarValores_negativos(valor_inmueble, tasa_interes, edad)

        Calcular_Hipoteca_Inversa.verificarValores_vacios(valor_inmueble, tasa_interes, edad)
        
        Calcular_Hipoteca_Inversa.verificarTasa_Interes(tasa_interes)

        if estado_civil.lower() not in ESTADOS_CIVILES:
            raise Exception("Hubo un error con su estado civil, debe ingresar si es: soltero/a, viudo/a, casado/a, divorciado/a")
            
        elif sexo_conyugue.lower() not in SEXOS:
            raise Exception("Hubo un error con el sexo de su conyugue, debe ingresar si es: masculino, femenino, hombre, mujer")

        else:
            # Se calcula el tiempo restante de la persona en meses, teniendo en cuenta que la esperanza de vida de los hombres es de 84 años y de las mujeres es de 86 años
            if sexo_conyugue.lower() == "hombre" or sexo_conyugue.lower() == "masculino" or estado_civil.lower() == "viuda" or estado_civil.lower() == "soltera" or estado_civil.lower() == "divorciada":      
                tiempo_restante = (ESPERANZA_VIDA_MUJERES - edad) * MESES_AÑO
                tiempo_restante_conyugue = (ESPERANZA_VIDA_HOMBRES - edad_conyugue) * MESES_AÑO
            else:
                tiempo_restante = (ESPERANZA_VIDA_HOMBRES - edad) * MESES_AÑO
                tiempo_restante_conyugue = (ESPERANZA_VIDA_MUJERES - edad_conyugue) * MESES_AÑO
            # Se pregunta si la persona no tiene conyugue, para así calcular la hipoteca inversa solo con él/ella
            if estado_civil.lower() == "viudo" or estado_civil.lower() == "soltero" or estado_civil.lower() == "divorciado" or estado_civil.lower() == "viuda" or estado_civil.lower() == "soltera" or estado_civil.lower() == "divorciada":
                return Calcular_Hipoteca_Inversa.Calcular_Cuota_Mensual(valor_inmueble, tasa_interes, tiempo_restante)
            # Se pregunta si la persona tiene conyugue, para así calcular cual de los dos vivirá más
            elif estado_civil == "casado" or estado_civil == "casada":
                if tiempo_restante > tiempo_restante_conyugue and edad >= EDAD_MINIMA:
                    return Calcular_Hipoteca_Inversa.Calcular_Cuota_Mensual(valor_inmueble, tasa_interes, tiempo_restante)
                else:
                    if tiempo_restante > tiempo_restante_conyugue and edad >= EDAD_MINIMA:
                        return Calcular_Hipoteca_Inversa.Calcular_Cuota_Mensual(valor_inmueble, tasa_interes, tiempo_restante)
                    else:
                        if tiempo_restante > tiempo_restante_conyugue and edad_conyugue >= EDAD_MINIMA:
                            return Calcular_Hipoteca_Inversa.Calcular_Cuota_Mensual(valor_inmueble, tasa_interes, tiempo_restante_conyugue)
                        else:
                            return Calcular_Hipoteca_Inversa.Calcular_Cuota_Mensual(valor_inmueble, tasa_interes, tiempo_restante)
        
    # Verifica que la tasa de interes no sea 0, que no este por debajo del valor minimo y que no supere el valor maximo
    def verificarTasa_Interes(interes):
        if interes < INTERES_MINIMO:
            raise Tasa_Exception(interes)
        if interes > INTERES_MAXIMO:
            raise Tasa_Exception(interes)

    # Verifica que ningun valor sea negativo
    def verificarValores_negativos(valor_inmueble, interes, tiempo_restante):
        if valor_inmueble < 0 or interes < 0 or tiempo_restante < 0:
            raise Negative_Exception()
        
    # Verifica que ningun campo haya quedado vacio
    def verificarValores_vacios(valor_inmueble, interes, tiempo_restante):
        if valor_inmueble == None or interes == None or tiempo_restante == None:
            raise None_Exception()

    # Verifica que la edad del usuario no esté por debajo del limite
    def verificarEdad(edad, edad_conyugue):
        if edad < EDAD_MINIMA and edad_conyugue < EDAD_MINIMA or edad > ESPERANZA_VIDA_HOMBRES:
            raise Edad_Minima_Exception(edad)

    # Verifica que el valor de la propiedad no sea menor al minimo
    def verificarValor_Inmueble(valor_inmueble):
        if valor_inmueble < VALOR_MINIMO_INMUEBLE:
            raise Hipoteca_Exception(valor_inmueble)