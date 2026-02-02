class Empleados:
    def __init__(self, idEmpleado, nombre):
        self.idEmpleado = idEmpleado
        self.nombre = nombre

    def mostrar_informacion(self):
        print(f"ID: {self.idEmpleado}, Nombre: {self.nombre}")

class Gerente(Empleados):
    def __init__(self, idEmpleado, nombre, sueldoBase):
        super().__init__(idEmpleado, nombre)
        self.sueldoBase = sueldoBase
        self.aumentos = []

    def aplicar_aumento(self, porcentaje):
        if porcentaje <= 0:
            raise ValueError("El porcentaje debe ser positivo")
        aumento = self.sueldoBase * (porcentaje / 100)
        self.sueldoBase += aumento
        self.aumentos.append(porcentaje)
        print(f"Nuevo sueldo base: {self.sueldoBase}")

    def historial_aumentos(self):
        print("Historial de aumentos:")
        for aumento in self.aumentos:
            print(f"Aumento del {aumento}%")

class Tecnico(Empleados):
    def __init__(self, idEmpleado, nombre, area):
        super().__init__(idEmpleado, nombre)
        self.area = area
        self.horas_extras = 0

    def registrar_horas_extras(self, horas):
        if horas <= 0:
            raise ValueError("Las horas deben ser positivas")
        self.horas_extras += horas
        print(f"Horas extras registradas: {self.horas_extras}")

    def calcular_paga_extra(self):
        return self.horas_extras * 50  # Suponiendo que se paga 50 por hora extra

class EmpleadoVentas(Empleados):
    def __init__(self, idEmpleado, nombre, comision):
        super().__init__(idEmpleado, nombre)
        self.comision = comision
        self.ventas = 0

    def registrar_venta(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        self.ventas += monto
        print(f"Venta registrada: {self.ventas}")

    def calcular_comision_total(self):
        return self.ventas * (self.comision / 100)