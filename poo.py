#1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área del rectángulo


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


mi_rectangulo = Rectangulo(10, 5)
print("El área del rectángulo es:", mi_rectangulo.calcular_area())


"""2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener como miembros:o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible.
Si se intenta beber un mate vacío, se debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. 
En ese caso la cantidad de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso: “Advertencia: 
el mate está lavado.” pero no se debe lanzar una excepción."""


"""class Mate:
    def __init__(self, n):
        self.n = n 
        self.cebadas_restantes = n
        self.estado = "vacío"  

    def cebar(self):
        if self.estado == "lleno":
            raise Exception("¡Cuidado! ¡Te quemaste!")
        self.estado = "lleno"

    def beber(self):
        if self.estado == "vacío":
            raise Exception("¡El mate está vacío!")
        
        self.estado = "vacío"
        
        if self.cebadas_restantes > 0:
            self.cebadas_restantes -= 1
        else:
            print("Advertencia: el mate está lavado.")

# Ejemplo de uso:
try:
    matecito = Mate(3)
    matecito.cebar()
    matecito.beber()
    matecito.cebar()
    matecito.beber()
    matecito.cebar()
    matecito.beber()
    matecito.cebar()
    matecito.beber()  
    matecito.beber()  
except Exception as e:
    print(e)
"""



"""3) Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya un corcho."""


"""class Corcho:
    def __init__(self, bodega):
        self.bodega = bodega


class Botella:
    def __init__(self, corcho):
        self.corcho = corcho  


class Sacacorchos:
    def __init__(self):
        self.corcho = None  

    def destapar(self, botella):
        if self.corcho is not None:
            raise Exception("Error: el sacacorchos ya tiene un corcho.")
        if botella.corcho is None:
            raise Exception("Error: la botella ya está destapada.")

        
        self.corcho = botella.corcho
        botella.corcho = None

    def limpiar(self):
        if self.corcho is None:
            raise Exception("Error: el sacacorchos ya está limpio.")
        self.corcho = None"""

"""4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos: restaurante_nombre y tipo_comida.
Cree un método describir_restaurante() que muestre estas piezas de información, y un método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los sabores de helado disponibles.
Escriba también un método que muestre estos valores, cree una instancia de la clase y llame al método."""


"""class Restaurante:
    def __init__(self, restaurante_nombre, tipo_comida):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = tipo_comida

    def describir_restaurante(self):
        print(f"Nombre del restaurante: {self.restaurante_nombre}")
        print(f"Tipo de comida: {self.tipo_comida}")

    def abrir_restaurante(self):
        print(f"El restaurante {self.restaurante_nombre} ahora está abierto.")



class Heladeria(Restaurante):
    def __init__(self, restaurante_nombre, sabores):
        super().__init__(restaurante_nombre, "helado")
        self.sabores = sabores  
    def mostrar_sabores(self):
        print("Sabores disponibles:")
        for sabor in self.sabores:
            print(f"- {sabor}")"""