#test tecnico
from src.empleados import Tecnico

def test_registrar_horas_extras():
    tecnico = Tecnico(2, "Jane Smith", "IT")
    tecnico.registrar_horas_extras(5)
    assert tecnico.horas_extras == 5

def test_calcular_paga_extra():
    tecnico = Tecnico(2, "Jane Smith", "IT")
    tecnico.registrar_horas_extras(5)
    assert tecnico.calcular_paga_extra() == 250