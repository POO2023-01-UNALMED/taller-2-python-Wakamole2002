class Auto:
    cantidadCreados = 0
    def __init__(self,modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        total = 0
        for i in self.asientos:
            if isinstance(i, Asiento):
                total += 1
        return total

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        else:
            for i in self.asientos:
                if i != self.registro:
                    return "Las piezas no son originales"
            else: 
                    return "Auto original"

class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        colores = ["rojo", "verde", "amarillo", "blanco", "negro"]
        if color in colores:
            self.color = color

class Motor:

    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros 
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self,registro):
        self.registro = registro

    def asignarTipo(self,tipo):
        if (tipo == "electrico") or (tipo == "gasolina"):
            self.tipo = tipo


        