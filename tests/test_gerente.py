#test gerente
from src.empleados import Gerente

def test_aplicar_aumento():
    gerente = Gerente(1, "John Doe", 5000)
    gerente.aplicar_aumento(10)
    assert gerente.sueldoBase == 5500

def test_historial_aumentos(capsys):
    gerente = Gerente(1, "John Doe", 5000)
    gerente.aplicar_aumento(10)
    gerente.aplicar_aumento(5)
    gerente.historial_aumentos()
    captured = capsys.readouterr()
    assert "Historial de aumentos" in captured.out
    assert "10%" in captured.out
    assert "5%" in captured.out