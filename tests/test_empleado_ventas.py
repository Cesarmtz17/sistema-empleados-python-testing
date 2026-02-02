#empleado ventas
from src.empleados import EmpleadoVentas

def test_registrar_venta():
    empleado_ventas = EmpleadoVentas(3, "Alice Johnson", 5)
    empleado_ventas.registrar_venta(10000)
    assert empleado_ventas.ventas == 10000

def test_calcular_comision_total():
    empleado_ventas = EmpleadoVentas(3, "Alice Johnson", 5)
    empleado_ventas.registrar_venta(10000)
    assert empleado_ventas.calcular_comision_total() == 500

