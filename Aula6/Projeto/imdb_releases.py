import os
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import datetime
import xlsxwriter
import time

print('Inicializando etapa de coleta...'.center(50, '*'))
print('\n')
options = webdriver.ChromeOptions() # Remove logs "aleatórios" so Selenium ao abrir o WebDriver
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('./chromedriver.exe', options=options) # Chama o chromedriver para a automação
driver.maximize_window() # Maximiza a tela do Chrome
driver.implicitly_wait(30) # Configura um tempo de espera de 30 segundos
driver.get('https://www.imdb.com/') # Acessa o site do IMDB
driver.find_element_by_id('imdbHeader-navDrawerOpen--desktop').click() # Clica para abrir o menu (ao lado do cabeçalho)
time.sleep(5) # Aguarda 5 segundos antes de continuar
driver.find_element_by_css_selector('div[data-testid="list-container"] a').click() # Clica no "Calendário de Lançamento" | "Calendar Releases"
pais_lancamentos = input('Por favor insira o país (em inglês) em que deseja ver os lançamentos:\nR: ') # Solicita um país para filtrar a lista
pais_lancamentos = pais_lancamentos.title() # Trata país fornecido para sempre deixar a primeira letra maiúscula
pais = driver.find_element_by_link_text(pais_lancamentos) # Coleta elemento web do país
pais.location_once_scrolled_into_view # Efetua um "scroll" até o país desejado
pais.click() # Clica no país desejado
lista_lancamentos = [] # Cria uma lista vazia
elemento_lista = driver.find_element_by_id('main') # Coleta o "pai" da lista de filmes
qtde_datas = elemento_lista.find_elements_by_tag_name('ul') # Pega todos os elementos de tag "ul" que são filhas ao DIV de ID "main"
for indice in range(len(qtde_datas)): # Gera um looping com base na contagem de elementos
    indice += 1 # Incrementa +1 na variável índice
    lista_filmes = driver.find_elements_by_xpath(f'//div[@id="main"]/ul[{indice}]/li/a') # Coleta os elementos web que possuem as informações dos filmes
    for filme in lista_filmes: # Gera um looping com base nos elementos web recuperados em "lista_filmes"
        filme.location_once_scrolled_into_view # Efetua um "scroll" até o filme em que está sendo coletado
        data = driver.find_element_by_xpath(f'//div[@id="main"]/h4[{indice}]').text # Colta a data em que o filme será lançado
        data = datetime.datetime.strptime(data, "%d %B %Y") # Formata a data no formato String (03 February 2022) para Datetime (datetime.datetime(2022,02,03,0,0))
        data = data.strftime('%d/%m/%Y') # Devolve a data que estava no formado Datetime para String com a formatação DD/MM/YYYY
        link = filme.get_attribute('href') # Coleta o link do IMDB para mais detalhes do filme que está sendo coletado
        html = requests.get(link) # Efetua o "download" do HTML da página com maiores detalhes sobre o filme
        soup = BeautifulSoup(html.text, 'html.parser') # Configura o HTML no formato de "parse" para varrer o HTML
        resumo = soup.find('p', {"data-testid": "plot"}) # busca pela sinopse do filme na página do IMDB
        if resumo: # Se a variável não tiver vazia, entrará nessa condicional
            resumo = resumo.text
        lista_lancamentos.append(
            [
                filme.text,
                data,
                resumo,
                link,
                pais_lancamentos
            ]
        ) # Adiciona uma lista contendo o nome do filme, data de lançamento, a sinopse, o link e o país em que será lançado na lista "lista_lancamentos"
driver.close()
driver.quit()
print('Finalizado etapa de coleta...'.center(50, '*'))
print('\n')

print('Inicializando etapa de Excel...'.center(50, '*'))
print('\n')
ano = datetime.datetime.today().year # Coleta o ano em que será lançado os filmes
pais_lancamentos = pais_lancamentos.replace(' ', '_') # Substitui espaços por underline para gerar o nome do arquivo
pais_lancamentos = pais_lancamentos.lower() # Deixa o nome do país com todas as letras minúsculas para gerar o nome do arquivo

wb = xlsxwriter.Workbook(f'filmes_lançados_{pais_lancamentos}.xlsx') # Gera arquivo Excel contendo o nome do país
ws = wb.add_worksheet(f'Ano {ano}') # Cria uma aba no Excel com o ano de lançamento dos filmes
bold = wb.add_format({'bold':1}) # Cria configuração para colocar Negrito nas fontes
ws.write('A1', 'Nome Filme', bold) # Cria cabeçalho "Nome Filme" em Negrito
ws.write('B1', 'Data de Lançamento', bold) # Cria cabeçalho "Data de Lançamento" em Negrito
ws.write('C1', 'Sinopse', bold) # Cria cabeçalho "Resumo" em Negrito
ws.write('D1', 'Link', bold) # Cria cabeçalho "Link" em Negrito
ws.write('E1', 'Pais de lançamento', bold) # Cria cabeçalho "Pais de lançamento" em Negrito
row, col = 1, 0 # Instancia o local inicial do Excel para o looping
for line in lista_lancamentos: # Efetua um looping na lista de listas que contém os dados coletados do IMDB
    ws.write_string(row, col, line[0])
    ws.write_string(row, col+1, line[1])
    ws.write_string(row, col+2, line[2] or "")
    ws.write_string(row, col+3, line[3])
    ws.write_string(row, col+4, line[4])
    row += 1
wb.close() # Fecha o Excel salvando-o
print('Etapa de Excel finalizada...'.center(50, '*'))
print('\n')
print('Automação concluída com êxito!'.center(50, '*'))