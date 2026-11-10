# Responsável: Matheus Gante Pinto
# Regra 1: Verificar valor mínimo do pedido

def pedido_atingiu_valor_minimo(valor_pedido):
    """
    Verifica se um pedido atingiu o valor mínimo de R$ 30,00.
    
    Args:
        valor_pedido (float): O valor do pedido em reais.
        
    Returns:
        bool: True se o pedido é >= R$ 30,00, False caso contrário.
        
    Raises:
        ValueError: Se o valor do pedido for negativo.
    """
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")
    
    return valor_pedido >= 30.00