
from abc import ABC, abstractmethod
from datetime import datetime

# ======================================================
# Sistema Integral de Gestión de Clientes, Servicios y Reservas - SOFTWARE FJ
# Practica - Fase 4
# ======================================================

# ======================================================
# FUNCION PARA REGISTRAR LOGS
# ======================================================

def registrar_log(mensaje):
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{datetime.now()} - {mensaje}\n")


# ======================================================
# EXCEPCIONES PERSONALIZADAS
# ======================================================

class ErrorCliente(Exception):
    pass


class ErrorServicio(Exception):
    pass


class ErrorReserva(Exception):
    pass


# ======================================================
# CLASE ABSTRACTA
# ======================================================

class Entidad(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass


# ======================================================
# CLASE CLIENTE
# ======================================================

class Cliente(Entidad):

    def __init__(self, nombre, documento):

        try:

            if not nombre.strip():
                raise ErrorCliente("El nombre del cliente está vacío")

            if not documento.strip():
                raise ErrorCliente("El documento del cliente está vacío")

            self.__nombre = nombre
            self.__documento = documento

            registrar_log(f"Cliente registrado: {nombre}")

        except ErrorCliente as e:
            registrar_log(str(e))
            raise

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - Documento: {self.__documento}"

    def obtener_nombre(self):
        return self.__nombre


# ======================================================
# CLASE ABSTRACTA SERVICIO
# ======================================================

class Servicio(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# ======================================================
# SERVICIO 1 - RESERVA DE SALA
# ======================================================

class ReservaSala(Servicio):

    def __init__(self, horas):

        super().__init__("Reserva de Sala")

        if horas <= 0:
            raise ErrorServicio("Las horas deben ser mayores a 0")

        self.horas = horas

    def calcular_costo(self):
        return self.horas * 50000

    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"


# ======================================================
# SERVICIO 2 - ALQUILER DE EQUIPOS
# ======================================================

class AlquilerEquipo(Servicio):

    def __init__(self, dias):

        super().__init__("Alquiler de Equipos")

        if dias <= 0:
            raise ErrorServicio("Los días deben ser mayores a 0")

        self.dias = dias

    def calcular_costo(self):
        return self.dias * 80000

    def descripcion(self):
        return f"Alquiler de equipos por {self.dias} días"


# ======================================================
# SERVICIO 3 - ASESORIA
# ======================================================

class Asesoria(Servicio):

    def __init__(self, horas):

        super().__init__("Asesoría Especializada")

        if horas <= 0:
            raise ErrorServicio("Las horas deben ser mayores a 0")

        self.horas = horas

    def calcular_costo(self):
        return self.horas * 100000

    def descripcion(self):
        return f"Asesoría especializada por {self.horas} horas"


# ======================================================
# CLASE RESERVA
# ======================================================

class Reserva:

    def __init__(self, cliente, servicio, duracion):

        try:

            if not isinstance(cliente, Cliente):
                raise ErrorReserva("Cliente inválido")

            if not isinstance(servicio, Servicio):
                raise ErrorReserva("Servicio inválido")

            if duracion <= 0:
                raise ErrorReserva("La duración debe ser mayor a 0")

            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "Pendiente"

            registrar_log("Reserva creada correctamente")

        except ErrorReserva as e:
            registrar_log(str(e))
            raise

    def confirmar(self):

        try:

            costo = self.servicio.calcular_costo()

            self.estado = "Confirmada"

        except Exception as e:

            registrar_log(f"Error al confirmar reserva: {e}")

            return "Error en la confirmación"

        else:

            registrar_log("Reserva confirmada")

            return (
                f"Reserva confirmada para "
                f"{self.cliente.obtener_nombre()} | "
                f"Servicio: {self.servicio.nombre} | "
                f"Costo: ${costo}"
            )

        finally:

            registrar_log("Proceso de confirmación finalizado")

    def cancelar(self):

        self.estado = "Cancelada"

        registrar_log("Reserva cancelada")

        return "La reserva fue cancelada"


# ======================================================
# SIMULACION DE OPERACIONES
# ======================================================

def simulacion():

    print("\n========== SIMULACION DEL SISTEMA ==========\n")

    # OPERACION 1
    try:
        cliente1 = Cliente("Juan", "1010")
        servicio1 = ReservaSala(2)
        reserva1 = Reserva(cliente1, servicio1, 2)

        print(reserva1.confirmar())

    except Exception as e:
        print(e)

    # OPERACION 2
    try:
        cliente2 = Cliente("", "")

    except Exception as e:
        print("Error:", e)

    # OPERACION 3
    try:
        cliente3 = Cliente("Ana", "")

    except Exception as e:
        print("Error:", e)

    # OPERACION 4
    try:
        cliente4 = Cliente("Carlos", "3030")
        servicio4 = AlquilerEquipo(3)
        reserva4 = Reserva(cliente4, servicio4, 3)

        print(reserva4.confirmar())

    except Exception as e:
        print(e)

    # OPERACION 5
    try:
        cliente5 = Cliente("Maria", "4040")
        servicio5 = Asesoria(5)
        reserva5 = Reserva(cliente5, servicio5, 5)

        print(reserva5.confirmar())

    except Exception as e:
        print(e)

    # OPERACION 6
    try:
        cliente6 = Cliente("Luis", "5050")
        servicio6 = ReservaSala(-1)

    except Exception as e:
        print("Error:", e)

    # OPERACION 7
    try:
        cliente7 = Cliente("Pedro", "6060")
        reserva7 = Reserva(cliente7, "Servicio falso", 2)

    except Exception as e:
        print("Error:", e)

    # OPERACION 8
    try:
        cliente8 = Cliente("Laura", "7070")
        servicio8 = AlquilerEquipo(1)
        reserva8 = Reserva(cliente8, servicio8, 1)

        print(reserva8.cancelar())

    except Exception as e:
        print("Error:", e)

    # OPERACION 9
    try:
        cliente9 = Cliente("Sofia", "8080")
        servicio9 = Asesoria(2)
        reserva9 = Reserva(cliente9, servicio9, 2)

        print(reserva9.confirmar())

    except Exception as e:
        print("Error:", e)

    # OPERACION 10
    try:
        cliente10 = Cliente("Miguel", "9090")
        servicio10 = ReservaSala(4)
        reserva10 = Reserva(cliente10, servicio10, 4)

        print(reserva10.confirmar())

    except Exception as e:
        print("Error:", e)

    print("\n========== FIN DE LA SIMULACION ==========\n")


# ======================================================
# EJECUCION PRINCIPAL
# ======================================================

if __name__ == "__main__":
    simulacion()
