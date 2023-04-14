#crear_cuenta_joven()

class Cuenta:
    def __init__(self, titular:None, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, nuevo_titular):
        self.__titular = nuevo_titular

    @property
    def cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print("Titular:", self.__titular.mostrar())
        print("Cantidad:", self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad: float = 0, bonificacion: float = 0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self._bonificacion

    @bonificacion.setter
    def bonificacion(self, value):
        if value < 0:
            raise ValueError("La bonificación debe ser un número positivo")
        self._bonificacion = value
'''
    def es_titular_valido(self):
        edad = date.today().year - self.titular.fecha_nacimiento.year
        return self.titular.es_mayor_de_edad() and edad < 25

    def retirar(self, cantidad: float):
        if not self.es_titular_valido():
            print("El titular no es válido para retirar dinero")
            return
        super().retirar(cantidad)

    def mostrar(self):
        return f"Cuenta Joven\nTitular: {self.titular}\nBonificación: {self.bonificacion}"

class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = edad

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        if len(dni) != 9:
            raise ValueError("El DNI debe tener 9 caracteres")
        self._dni = dni

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18
        '''