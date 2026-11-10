import pytest
from src.regras_localeats import pedido_atingiu_valor_minimo

# Responsável: Matheus Gante Pinto


def test_pedido_acima_valor_minimo():
    """Teste para um comportamento válido: pedido acima do mínimo."""
    resultado = pedido_atingiu_valor_minimo(50.00)
    assert resultado is True


def test_pedido_abaixo_valor_minimo():
    """Teste para um comportamento inválido: pedido abaixo do mínimo."""
    resultado = pedido_atingiu_valor_minimo(20.00)
    assert resultado is False


def test_pedido_exatamente_valor_minimo():
    """Teste de limite: pedido exatamente no valor mínimo."""
    resultado = pedido_atingiu_valor_minimo(30.00)
    assert resultado is True


def test_pedido_valor_negativo():
    """Teste de exceção: valor negativo deve gerar ValueError."""
    with pytest.raises(ValueError):
        pedido_atingiu_valor_minimo(-10.00)