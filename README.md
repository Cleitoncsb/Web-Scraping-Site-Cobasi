h1>Web Scraping Site Cobasi</h1>


![Imagem1](https://github.com/Cleitoncsb/meu-Portfolio/assets/142935223/b9bf12f2-c1a3-46af-a8a8-b2fade673657)


 <h2> 📌 Overview   </h2>
 
 Este projeto exemplifica o uso eficaz da automação e do web scraping na era digital para simplificar e 
 acelerar a coleta de dados de sites, uma tarefa normalmente demorada e propensa a erros. <br>
 Empregando scripts automatizados 
 para extrair dados de forma eficiente e precisa, ele oferece aplicações práticas em diversos campos, desde análise de mercado até pesquisa 
 acadêmica, destacando-se pela eficiência na redução de tempo e erros, além de sua adaptabilidade para diferentes tipos de dados e sites.

<h2> 🪒 Um pouco sobre Web Scraping</h2>

Web scraping é uma técnica de automação para extrair dados de websites, empregando scripts para coletar informações de forma rápida e estruturada.<br>
Por exemplo, pode ser usado por empresas de e-commerce para monitorar os preços dos concorrentes, ajustando suas próprias estratégias de preços e marketing com base nesses dados. 

<h2> 📊 Resultados e Insigths</h2>
O resultado do código acima, retorna um excel com 80 linhas sendo 40 linhas referente a cada uma das URLs contidas no código, sendo armazenadas 
os campos referente ao produto e ao preço.<br>
<br>

![Captura de Tela 2023-12-12 às 22 19 25](https://github.com/Cleitoncsb/Analise-de-Dados-de-uma-Cafeteria-com-Python/assets/142935223/cf4a7c5f-6d65-49a5-b907-faee89cc7470)
<br>

<h2>Sobre a Metodologia</h2>
A aplicaçāo utilizada no código, segue os seguintes passos:<br>
1. Inicialização do WebDriver do Safari: O código começa inicializando o Selenium WebDriver para o navegador Safari. 
Este WebDriver age como um navegador automatizado que pode ser controlado pelo script. <br>
2. Acessar URLs e Coletar Dados: O código então percorre uma lista de URLs específicas (neste caso, páginas de produtos de um site de e-commerce). 
Para cada URL, ele carrega a página e aguarda um tempo (5 segundos) para que todo o conteúdo, incluindo elementos gerados por JavaScript, seja carregado.<br>
3. Extração de Dados com BeautifulSoup: Após carregar a página, o código usa o BeautifulSoup para analisar o HTML da página. Ele procura por contêineres 
específicos que contêm informações sobre produtos e preços, usando as classes CSS para identificá-los.<br>
4. Armazenamento dos Dados: Para cada contêiner encontrado, o código extrai o texto do nome do produto e do preço. Essas informações são armazenadas em um 
dicionário e adicionadas a uma lista chamada produtos.<br>
5. Salvar Dados em Excel: Após coletar todos os dados necessários, o script converte a lista de dicionários em um DataFrame do Pandas e salva esses dados em um arquivo Excel.<br>
6. Encerramento do WebDriver: Por fim, o WebDriver é fechado para liberar recursos.<br>
