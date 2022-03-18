from selenium import webdriver
import pyderman as dr
import xlsxwriter
import os
from datetime import datetime
import warnings

# Remove alertas de funcionalidades obsoletas
warnings.filterwarnings("ignore") 

# Biblioteca que efetua o download do ChromeDriver assim que atualiza o navegador
path = dr.install(dr.chrome, file_directory=rf'{os.getcwd()}\driver', overwrite=True, filename='chromedriver.exe', verbose=False)

# Remove mensagens "inúteis" do Selenium ao instanciar o WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Efetua a chamada do ChromeDriver
driver = webdriver.Chrome(path,options=options)

# Cria  uma variável contendo a data de hoje no formato dd_mm_yyyy
data_hoje = datetime.now()
data_hoje = data_hoje.strftime('%d_%m_%Y')

# Maximiza a tela do navegador
driver.maximize_window()

# Seta um timeout máximo de carregamento da página em 30 segundos
driver.implicitly_wait(30)

# Cria uma visão "bonita" para informar que a automação começou
print('Busca Amazon 1.0'.center(50, '*')+'\n')

# Acessa o site da Amazon
driver.get('https://www.amazon.com.br/')

# Clica na categoria de "Mais Vendidos"
driver.find_element_by_link_text('Mais Vendidos').click()

# Coleta os elementos das categorias de objetos da Amazon
categorias = driver.find_element_by_css_selector('div[class*="zg-browse-root"]').find_elements_by_tag_name('a')

# Gera um "menu" para que o usuário selecione a categoria através do número dela
opcoes = {}
contador = 0

for opcao in categorias:
    contador+=1
    opcoes[contador] = opcao.text

for k, v in opcoes.items():
	print(k, '-', v.strip())

# Imprime o menu na tela para o usuário interagir
while True:
    try:
        opcao = int(input('\nQual o número da categoria você deseja explorar?\nR:'))
        if opcao > len(opcoes):
            print(f'\nPor favor, insira um número menor que {len(opcoes)+1}!')
            continue
        break
    except TypeError:
        print('\nPor favor, insira um número válido!\n')
        continue

# Apresenta a opção escolhida pelo usuário
print(f'\nVocê selecionou a opção "{opcoes[opcao].strip()}"\n')

# Clica no elemento pertencente a categoria escolhida pelo usuário
for elemento in categorias:
    if opcoes[opcao] in elemento.text:
        elemento.click()
        break

# Coleta a grade contendo todos os objetos iniciais presentes na categoria escolhida
coletas = driver.find_elements_by_id('gridItemRoot')

# Cria uma lista e efetua um looping coletando o nome, a nota e o valor do produto na categoria desejada
produtos = []

for item in coletas:
    nome = item.find_element_by_tag_name('img').get_attribute('alt')
    nota = item.find_element_by_css_selector('a[title*="estrela"]').get_attribute('title')
    try:
        valor = item.find_element_by_class_name('a-size-base.a-color-price').text
    except:
        valor = 'Não disponivel'
    produtos.append({'nome':nome,'nota':nota,'valor':valor})

# Pega o nome da categoria e substitui os espaços por underline "_"
nome_arq = opcoes[opcao].replace(' ','_')

# Cria a pasta "files" no diretório em que está sendo executado
os.makedirs(rf'{os.getcwd()}\files', exist_ok=True)

# Cria um objeto de arquivo Excel
wb = xlsxwriter.Workbook(fr'{os.getcwd()}\files\{nome_arq}_{data_hoje}.xlsx')
ws = wb.add_worksheet()

# Cria a linha de cabeçalho do Excel
bold = wb.add_format({'bold':1})
ws.write('A1','Nome do produto', bold)
ws.write('B1','Nota do produto', bold)
ws.write('C1','Valor do produto', bold)

# Efetua a escrita das informações dos objetos coletados na página da Amazon
row = 1
col = 0
for valores in produtos:
	ws.write_string(row, col, valores['nome'])
	ws.write_string(row, col+1, valores['nota'])
	ws.write_string(row, col+2, valores['valor'])
	row+=1

# Salva e fecha o arquivo Excel criado
wb.close()

# Encerra o ChromeDriver aberto
driver.quit()
