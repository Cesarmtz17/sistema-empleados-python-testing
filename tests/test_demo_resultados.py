

def test_demostracion_pasa():
    empleado_ventas = EmpleadoVentas(3, "Alice Johnson", 10)
    empleado_ventas.registrar_venta(1000)
    assert empleado_ventas.calcular_comision_total() == 100  # 10% de 1000

def test_demostracion_falla():
    empleado_ventas = EmpleadoVentas(3, "Alice Johnson", 10)
    empleado_ventas.registrar_venta(1000)
    # Falla intencional: la comisión correcta es 100, aquí esperamos 120
    assert empleado_ventas.calcular_comision_total() == 120


