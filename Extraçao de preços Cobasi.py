from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

# Lista de URLs para visitar
urls = [
    'https://www.cobasi.com.br/c/gatos/racao/racao-seca', 
    'https://www.cobasi.com.br/c/gatos/racao/racao-seca?page=2',
    # Adicione mais URLs conforme necessário
]

# Inicializando o WebDriver do Safari
driver = webdriver.Safari()

produtos = []

for url in urls:
    driver.get(url)
    time.sleep(5)  # Tempo para carregar o conteúdo JavaScript

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Encontrando os contêineres que contêm tanto os produtos quanto os preços
    contêineres = soup.find_all('div', class_='styles__ProductItem-sc-1ac06td-0 bNtpHK') # Substitua 'sua_classe_contêiner' pela classe correta

    for contêiner in contêineres:
        nome_produto = contêiner.find('h3', class_='styles__Title-sc-1ac06td-4 dPsqyZ')
        preço_produto = contêiner.find('span', class_='card-price')

        if nome_produto and preço_produto:
            produtos.append({
                'Produto': nome_produto.get_text().strip(),
                'Preço': preço_produto.get_text().strip()
            })

driver.quit()

# Criando um DataFrame com os dados coletados
df = pd.DataFrame(produtos)

# Salvando o DataFrame em um arquivo Excel
df.to_excel('/Users/user/Documents/DATABASES/arquivo.xlsx', index=False)

print("Dados salvos em Excel com sucesso.")
