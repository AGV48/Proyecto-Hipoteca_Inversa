from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from Logic.Hipoteca_Inversa_Calculator import Calcular_Hipoteca_Inversa

class PaymentApp(App):
    def build(self):
        container = GridLayout(cols=2, padding=20, spacing=20)

        container.add_widget(Label(text="Ingrese el valor del inmueble"))
        self.valor_inmueble = TextInput(font_size=30)
        container.add_widget(self.valor_inmueble)

        container.add_widget(Label(text="Ingrese su edad"))
        self.edad = TextInput(font_size=30)
        container.add_widget(self.edad)

      
        estados_civiles = ["soltero/a", "viudo/a", "casado/a", "divorciado/a"]
        estado_civil_dropdown = DropDown()
        for estado in estados_civiles:
            btn = Button(text=estado, size_hint_y=None)
            btn.bind(on_release=lambda btn: estado_civil_dropdown.select(btn.text))
            estado_civil_dropdown.add_widget(btn)
        main_button_estado_civil = Button(text='Seleccione')
        main_button_estado_civil.bind(on_release=estado_civil_dropdown.open)
        estado_civil_dropdown.bind(on_select=lambda instance, x: setattr(main_button_estado_civil, 'text', x))
        container.add_widget(Label(text="Ingrese su estado civil"))
        container.add_widget(main_button_estado_civil)

        container.add_widget(Label(text="Ingrese la edad de su cónyuge"))
        self.edad_conyugue = TextInput(font_size=30)
        container.add_widget(self.edad_conyugue)
        
 
        sexos = ["masculino", "femenino"]
        sexo_dropdown = DropDown()
        for sexo in sexos:
            btn = Button(text=sexo, size_hint_y=None)
            btn.bind(on_release=lambda btn: sexo_dropdown.select(btn.text))
            sexo_dropdown.add_widget(btn)
        main_button_sexos = Button(text='Seleccione')
        main_button_sexos.bind(on_release=sexo_dropdown.open)
        sexo_dropdown.bind(on_select=lambda instance, x: setattr(main_button_sexos, 'text', x))
        container.add_widget(Label(text="Ingrese el sexo de su cónyuge"))
        container.add_widget(main_button_sexos)

        container.add_widget(Label(text="Ingrese la tasa de interés"))
        self.tasa_interes = TextInput(font_size=30)
        container.add_widget(self.tasa_interes)

        self.calcular = Button(text="Calcular cuota")
        container.add_widget(self.calcular)
        self.calcular.bind(on_press=self.calcular_cuota)

        self.resultado = Label(text="Valor de la cuota")
        container.add_widget(self.resultado)

        return container

    def calcular_cuota(self, sender):
        try:
            valor_inmueble = float(self.valor_inmueble.text)
            edad = int(self.edad.text)
            estado_civil = self.estado_civil_dropdown.text 
            edad_conyugue = int(self.edad_conyugue.text)
            sexo_conyugue = self.sexo_dropdown.text 
            tasa_interes = float(self.tasa_interes.text)

            result = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)
            self.resultado.text = str(round(result, 2))
        except Exception as err:
            self.resultado.text = str(err)
            
    def Validar(self, sender):
        try:
            valor_inmueble = self.validar_valor(self.valor_inmueble.text)
            edad = self.validar_edad(self.edad.text)
            estado_civil = self.estado_civil_dropdown.text 
            edad_conyugue = self.validar_edad(self.edad_conyugue.text)
            sexo_conyugue = self.sexo_dropdown.text 
            tasa_interes = self.validar_tasa(self.tasa_interes.text)

            result = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)
            self.resultado.text = str(round(result, 2))
        except ValueError as ve:
            self.resultado.text = "Error: " + str(ve)
        except Exception as err:
            self.resultado.text = "Error: " + str(err)

    def validar_Valor(self, valor):
        valor_float = float(valor)
        if valor_float <= 0:
            raise ValueError("El valor del inmueble debe ser mayor que cero.")
        return valor_float

    def validar_Edad(self, edad):
        edad_int = int(edad)
        if edad_int <= 0:
            raise ValueError("La edad debe ser mayor que cero.")
        return edad_int

    def validar_Tasa(self, tasa):
        tasa_float = float(tasa)
        if tasa_float <= 0:
            raise ValueError("La tasa de interés debe ser mayor que cero.")
        return tasa_float


if __name__ == "__main__":
    PaymentApp().run()



            
