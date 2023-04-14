#Natalia Jiménez - C23319

'''
#7 Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:
• Un constructor, donde los datos pueden estar vacíos.
• Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
• mostrar(): Muestra los datos de la cuenta.
• ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
• retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.'''

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        while cantidad < 0:
            cantidad = int(input("Ingrese Un Monto Positivo: "))
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

    # Método para mostrar los datos de la cuenta
    def mostrar(self):
        print(f"Titular: {self.__titular}")
        print(f"Cantidad: {self.__cantidad}")

    # Método para ingresar dinero en la cuenta
    def ingresar(self, cantidad):
        while cantidad <= 0:
            print('La cantidad debe ser positiva')
            cantidad = float(input('Ingrese otro monto, que sea positivo: '))
        self.__cantidad += cantidad

    # Método para retirar dinero de la cuenta
    def retirar(self, cantidad):
        self.__cantidad -= cantidad

# Método para crear la cuenta
def crear_cuenta():
    print('\nHola. Vamos a crear una cuenta!')
    titular = input('Ingresa tu nombre: ')
    cantidad = float(input('¿Cuánto quieres depositar para inicializar tu cuenta?: '))
    while cantidad < 0:
        cantidad = float(input('Ingrese un monto positivo: '))
    cuenta1 = Cuenta(titular,cantidad)
    print('Genial! Hemos creado tu cuenta con éxito!')
    cuenta1.mostrar()

    print('¿Deseas realizar algún movimiento en tu cuenta?')
    respuesta=input('S/N: ')
    if respuesta == 'S':
        rta=input('¿Depositar o Retirar?, Marca "D" si deseas Depositar o "R" si deseas Retirar: ')
        if rta == 'D':
            deposito1=float(input('¿Cuánto deseas depositar?: '))
            cuenta1.ingresar(deposito1)
            cuenta1.mostrar()
        else:
            retiro=float(input('¿Cuánto deseas retirar?: '))
            #Si no quiero que quede en números rojos, uso esto:
            #while retiro > cantidad:
                #retiro=float(input('Saldo Insuficiente. Intenta nuevamente: '))
            cuenta1.retirar(retiro)
            cuenta1.mostrar()
    else:
        print('Hasta pronto\n')

crear_cuenta()

'''
#8 Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuentaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:
• Un constructor.
• Los setters y getters para el nuevo atributo.
• En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
• Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
• El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta. '''

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, value):
        if value < 0:
            raise ValueError("Labonificación debe ser un número positivo")
        self.__bonificacion = value

    def es_titular_valido(self):
        edad = int(input('Ingresa tu edad: '))
        return 18 <= edad < 25

    def retirar(self, monto):
        if not self.es_titular_valido():
            print('El titular no es válido para retirar dinero.')
            return
        super().retirar(monto)

    def mostrar(self):
        print('\nCuenta Joven')
        print(f'Bonificación (Entre 0% y 100%): {self.bonificacion}%')
        super().mostrar()

def crear_cuenta_joven():
    print('\nHola. Vamos a crear una cuenta Joven!')
    titular = input('Ingresa tu nombre: ')
    cantidad = float(input('¿Cuánto quieres depositar para inicializar tu cuenta?: '))
    while cantidad < 0:
        cantidad = float(input('Ingrese un monto positivo: '))
    bonificacion = float(input('Ingresa el porcentaje de bonificación (Entre 0% y 100%): '))
    cuenta_joven = CuentaJoven(titular,cantidad,bonificacion)

    print('\nGenial! Hemos creado tu cuenta joven con éxito!')
    cuenta_joven.mostrar()

    respuesta = input('\n¿Deseas realizar algún movimiento en tu cuenta? (S/N): ')
    if respuesta == 'S':
        rta = input('¿Depositar o Retirar? Marca "D" si deseas Depositar o "R" si deseas Retirar: ')
        if rta == 'D':
            deposito1 = float(input('¿Cuánto deseas depositar?: '))
            cuenta_joven.ingresar(deposito1)
            cuenta_joven.mostrar()
        else:
            retiro = float(input('¿Cuánto deseas retirar?: '))
            while retiro > cantidad:
                retiro=float(input('Saldo Insuficiente. Intenta nuevamente: '))
            cuenta_joven.retirar(retiro)
            cuenta_joven.mostrar()
    else:
        print('Hasta pronto\n')

crear_cuenta_joven()