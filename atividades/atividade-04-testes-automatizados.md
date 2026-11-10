# Atividade 4 - Testes Automatizados do LocalEats

**Aluno:** Matheus Gante Pinto  
**Unidade Curricular:** Qualidade de Software  
**Data:** 21/11/2026

---

## 1. Identificação dos Testes

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
|---|---|---|---|---|
| TU01 | Matheus | Unitário | Valor mínimo do pedido | tests/test_regras_localeats.py::test_pedido_acima_valor_minimo |
| TU02 | Matheus | Unitário | Pedido abaixo do mínimo | tests/test_regras_localeats.py::test_pedido_abaixo_valor_minimo |
| TU03 | Matheus | Unitário | Valor mínimo exato | tests/test_regras_localeats.py::test_pedido_exatamente_valor_minimo |
| TU04 | Matheus | Unitário | Valor negativo (exceção) | tests/test_regras_localeats.py::test_pedido_valor_negativo |
| TF01 | Matheus | Funcional | Pesquisar restaurante por categoria | tests/test_localeats.py::test_pesquisar_restaurante_brasileiro |
| TF02 | Matheus | Funcional | Acessar página inicial | tests/test_localeats.py::test_acessar_pagina_inicial_localeats |

---

## 2. Parte 1: Testes Unitários e TDD

### Regra Escolhida: Verificar Valor Mínimo do Pedido

A regra implementada é a **Regra 1**: `pedido_atingiu_valor_minimo(valor_pedido)`

**Comportamento esperado:**
- Pedidos de R$ 30,00 ou mais retornam `True`
- Pedidos abaixo de R$ 30,00 retornam `False`
- Valores negativos geram `ValueError`

### TDD de Matheus

**Regra escolhida:** Verificar valor mínimo do pedido (R$ 30,00)

**Primeiro teste escrito:**
```python
def test_pedido_acima_valor_minimo():
    resultado = pedido_atingiu_valor_minimo(50.00)
    assert resultado is True
```

**Por que o teste falhou inicialmente:**
O teste falhou porque a função `pedido_atingiu_valor_minimo` não existia. O error foi `NameError: name 'pedido_atingiu_valor_minimo' is not defined`.

**Implementação mínima realizada:**
```python
def pedido_atingiu_valor_minimo(valor_pedido):
    return valor_pedido >= 30.00
```

**Segundo teste escrito:**
```python
def test_pedido_abaixo_valor_minimo():
    resultado = pedido_atingiu_valor_minimo(20.00)
    assert resultado is False
```

Este teste passou imediatamente com a implementação anterior, porque a lógica `>= 30.00` já cobria este caso.

**Terceiro teste escrito (caso de borda):**
```python
def test_pedido_valor_negativo():
    with pytest.raises(ValueError):
        pedido_atingiu_valor_minimo(-10.00)
```

Para este teste passar, foi necessário adicionar validação na função:
```python
if valor_pedido < 0:
    raise ValueError("O valor do pedido não pode ser negativo.")
```

**Melhoria ou refatoração realizada:**
Adicionei docstring completa com Args, Returns e Raises, além de melhorar a legibilidade da função com comentários e tratamento explícito de valores inválidos. A função agora é mais robusta e fácil de entender.

---

## 3. Parte 2: Testes Funcionais com Playwright

### Teste Funcional 1: Pesquisar Restaurante por Categoria

**Fluxo automático:**
1. Acessar a página inicial do LocalEats
2. Aguardar o carregamento da página
3. Clicar no botão de filtro "Brasileira"
4. Verificar se restaurantes com categoria Brasileira aparecem
5. Validar que pelo menos um restaurante é exibido

**Assertions realizadas:**
1. Verificar se restaurantes com categoria Brasileira aparecem na página
2. Verificar se pelo menos um restaurante está visível após o filtro

**Locators utilizados:**
- `button:has-text('Brasileira')` - para encontrar o botão de filtro
- `div.filter(has_text="Brasileira")` - para validar resultados
- `div[class*='restaurant']` - para contar restaurantes exibidos

---

### Teste Funcional 2: Acessar Página Inicial do LocalEats

**Fluxo automático:**
1. Acessar https://local-eats-unisenac.vercel.app/
2. Aguardar o carregamento da página
3. Verificar se o título "LocalEats" está presente
4. Verificar se o campo de busca está disponível

**Assertions realizadas:**
1. Verificar se o título "LocalEats" está presente na página
2. Verificar se existe um campo de busca com placeholder "Buscar"

**Locators utilizados:**
- `text=LocalEats` - para validar o título
- `input[placeholder*='Buscar']` - para validar campo de busca

---

## 4. Estrutura de Arquivos

```
atividade-04/
├── atividade-04-testes-automatizados.md
├── relatorio-pytest.txt
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── regras_localeats.py
└── tests/
    ├── __init__.py
    ├── test_regras_localeats.py
    └── test_localeats.py
```

---

## 5. Execução dos Testes

### Comando executado:
```bash
python -m pytest tests/test_regras_localeats.py -v
```

### Resultado:
Todos os 4 testes unitários passaram com sucesso:
- `test_pedido_acima_valor_minimo` - PASSED
- `test_pedido_abaixo_valor_minimo` - PASSED
- `test_pedido_exatamente_valor_minimo` - PASSED
- `test_pedido_valor_negativo` - PASSED

**Resumo:** 4 passed em 0.01s

---

## 6. Notas Importantes sobre os Testes Funcionais

Os testes funcionais com Playwright (`test_localeats.py`) utilizam a URL real do LocalEats e foram desenvolvidos para automatizar fluxos observados durante a exploração. Os locators foram escolhidos baseando-se nos elementos realmente encontrados na interface.

**Observação:** Os testes funcionais podem precisar de ajustes nos locators caso a interface do LocalEats sofra alterações, pois usam seletores baseados no DOM real da aplicação.

---

## 7. Uso de Inteligência Artificial

**Ferramenta utilizada:** Claude (Anthropic)

**Como foi utilizada:**
- Apoio na estruturação dos testes unitários seguindo as boas práticas de TDD
- Sugestão de locators para os testes funcionais baseado em padrões comuns do Playwright
- Revisão da documentação e clareza do código

**Uma sugestão que precisou ser alterada ou rejeitada:**
A IA sugeriu inicialmente usar `page.wait_for_selector()` nos testes funcionais, mas foi alterado para `page.wait_for_load_state("networkidle")` que é mais confiável para aguardar o carregamento completo da página antes de interagir com ela.

**Como o código sugerido foi verificado:**
- Executei todos os testes unitários localmente para confirmar que passam
- Revisei manualmente os testes funcionais para garantir que os locators fazem sentido com a estrutura real do LocalEats
- Validei que as assertions usam métodos corretos do Playwright (como `.count()` e `.click()`)

