from kivy.app import App


from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup


import sys
sys.path.append("src")

from Logic.Hipoteca_Inversa_Calculator import Calcular_Hipoteca_Inversa
from Logic.Hipoteca_Inversa_Calculator import *

class PaymentApp(App):
    def build(self):
        contenedor = GridLayout(cols=2,padding=20,spacing=20)

        contenedor.add_widget( Label(text="Ingrese el valor del inmueble") )
        self.valor_inmueble = TextInput(font_size=30 )
        contenedor.add_widget(self.valor_inmueble)
        
        contenedor.add_widget( Label(text="Ingrese su edad") )
        self.edad = TextInput(font_size=30 )
        contenedor.add_widget(self.edad)
        
        contenedor.add_widget( Label(text="Ingrese su estado civil") )
        self.estado_civil = TextInput(font_size=30 )
        contenedor.add_widget(self.estado_civil)
        
        contenedor.add_widget( Label(text="Ingrese la edad de su conyugue") )
        self.edad_conyugue = TextInput(font_size=30 )
        contenedor.add_widget(self.edad_conyugue)
        
        contenedor.add_widget( Label(text="Ingrese el sexo de su conyugue") )
        self.sexo_conyugue = TextInput(font_size=30 )
        contenedor.add_widget(self.sexo_conyugue)
        
        contenedor.add_widget( Label(text="Ingrese la tasa de interes") )
        self.tasa_interes = TextInput(font_size=30 )
        contenedor.add_widget(self.tasa_interes)
        
        self.calcular = Button(text = "Calcular cuota")
        contenedor.add_widget(self.calcular)    
        
        self.calcular.bind(on_press = self.calcular_cuota)

        self.resultado = Label(text = "Valor de la cuota")
        contenedor.add_widget(self.resultado)
        
        return contenedor
    
    def calcular_cuota (self, sender):
        
        try:
        
            valor_inmueble = float(self.valor_inmueble.text)
            edad = int (self.edad.text)
            estado_civil = str (self.estado_civil.text)
            edad_conyugue = int (self.edad_conyugue.text)
            sexo_conyugue = str (self.sexo_conyugue.text)
            tasa_interes = float (self.tasa_interes.text)
            
            result = Calcular_Hipoteca_Inversa.Logica(valor_inmueble, edad, estado_civil, edad_conyugue, sexo_conyugue, tasa_interes)
            self.resultado.text = str (round(result,2))
        except Exception as err:
            self.resultado.text = str( err )
            
            
if __name__ == "__main__":
    PaymentApp().run()



            
