import pytest
from playwright.sync_api import sync_playwright

# Responsável: Matheus Gante Pinto


@pytest.fixture(scope="function")
def browser_context():
    """Fixture para criar e fechar o contexto do Playwright."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


def test_pesquisar_restaurante_brasileiro(browser_context):
    """
    Teste funcional: Pesquisar restaurantes por categoria (Brasileira).
    
    Assertions:
    1. Verifica se os restaurantes retornados contêm a categoria "Brasileira"
    2. Verifica se pelo menos um restaurante é exibido
    """
    page = browser_context.new_page()
    page.goto("https://local-eats-unisenac.vercel.app/")
    
    # Esperar a página carregar e clicar no botão de filtro "Brasileira"
    page.wait_for_load_state("networkidle")
    
    # Encontrar e clicar no filtro "Brasileira"
    brasileira_button = page.locator("button:has-text('Brasileira')")
    brasileira_button.click()
    
    # Esperar os resultados aparecerem
    page.wait_for_load_state("networkidle")
    
    # Assertion 1: Verificar se restaurantes com categoria Brasileira aparecem na página
    restaurante_cards = page.locator("div").filter(has_text="Brasileira")
    assert restaurante_cards.count() > 0, "Nenhum restaurante brasileiro foi encontrado"
    
    # Assertion 2: Verificar se pelo menos um restaurante está visível
    restaurantes = page.locator("div[class*='restaurant']")
    assert restaurantes.count() > 0, "Nenhum restaurante é exibido após o filtro"
    
    page.close()


def test_acessar_pagina_inicial_localeats(browser_context):
    """
    Teste funcional: Acessar a página inicial do LocalEats.
    
    Assertions:
    1. Verifica se o título "LocalEats" está presente na página
    2. Verifica se o campo de busca está presente na interface
    """
    page = browser_context.new_page()
    page.goto("https://local-eats-unisenac.vercel.app/")
    
    # Esperar a página carregar
    page.wait_for_load_state("networkidle")
    
    # Assertion 1: Verificar se o título LocalEats está na página
    page_title = page.locator("text=LocalEats")
    assert page_title.count() > 0, "O título 'LocalEats' não foi encontrado na página"
    
    # Assertion 2: Verificar se existe um campo de busca (input ou search box)
    search_input = page.locator("input[placeholder*='Buscar']")
    assert search_input.count() > 0, "Campo de busca não encontrado na página inicial"
    
    page.close()