from selenium import webdriver
import xlsxwriter


numero_mes = {
    '01': 'Janeiro',
    '02': 'Fevereiro',
    '03': 'Março',
    '04': 'Abril',
    '05': 'Maio',
    '06': 'Junho',
    '07': 'Julho',
    '08': 'Agosto',
    '09': 'Setembro',
    '10': 'Outubro',
    '11': 'Novembro',
    '12': 'Dezembro'
}

regiao = input('Qual a região que deseja viajar? ')

check_in = input('Qual a data de check-in? ')
check_in = check_in.split('/')
dia, mes, ano = check_in
check_in_correto = f'{ano}-{mes}-{dia}'
mes_check_in = f'{numero_mes[mes]} {ano}'

check_out = input('Qual a data de check_out? ')
check_out = check_out.split('/')
dia, mes, ano = check_out
check_out_correto = f'{ano}-{mes}-{dia}'
mes_check_out = f'{numero_mes[mes]} {ano}'

adultos = int(input('Por favor insira quantos adultos irão na viagem: '))
if not adultos:
    adultos = 1

# driver = webdriver.Chrome('C:/Users/Wilber Godoy/Documents/Aula5/chromedriver.exe')
driver = webdriver.Chrome('C:/drivers/chromedriver.exe')
driver.get('https://www.booking.com/index.pt-br.html')
driver.implicitly_wait(30)
driver.maximize_window()

# Seleciona região à ser viajada
regiao_selecionada = driver.find_element_by_id('ss')
regiao_selecionada.clear()
regiao_selecionada.send_keys(regiao)
primeiro_resultado = driver.find_element_by_css_selector('li[data-i="0"]').click()

# Seleciona datas de Check-In e Check-Out
lista_de_meses = list()

meses_apresentados = driver.find_elements_by_class_name('bui-calendar__month')
for elemento in meses_apresentados:
    lista_de_meses.append(elemento.text)

def loop_meses(mes_desejado, lista_de_meses):
    while mes_desejado not in lista_de_meses:
        driver.find_element_by_css_selector('div[data-bui-ref="calendar-next"]').click()
        month_list = driver.find_elements_by_class_name('bui-calendar__month')
        for month in month_list:
            lista_de_meses.append(month.text)

if mes_check_in not in lista_de_meses:
    loop_meses(mes_check_in, lista_de_meses)

driver.find_element_by_css_selector(f'td[data-date="{check_in_correto}"]').click()

if mes_check_out not in lista_de_meses:
    loop_meses(mes_check_out, lista_de_meses)

driver.find_element_by_css_selector(f'td[data-date="{check_out_correto}"]').click()

# Seleciona a quantidade de adultos
driver.find_element_by_id('xp__guests__toggle').click()

while True:
    driver.find_element_by_css_selector('button[aria-label="Diminuir número de Adultos"]').click()
    qtde_adultos = driver.find_element_by_id('group_adults').get_attribute('value')

    if int(qtde_adultos) == 1:
        break

increase_button_element = driver.find_element_by_css_selector('button[aria-label="Aumentar número de Adultos"]')
for _ in range(adultos - 1):
    increase_button_element.click()

# Confirma pesquisa
driver.find_element_by_css_selector('button[type="submit"]').click()

# Coleta nome do estabelecimento
resultados_pesquisa = driver.find_elements_by_css_selector('div[data-testid="property-card"]')
coleta_dados = []
for elemento in resultados_pesquisa:
    nome = elemento.find_element_by_css_selector('div[data-testid="title"]').text
    score = elemento.find_element_by_css_selector('div[data-testid="review-score"] div').get_attribute('aria-label')
    valor = elemento.find_elements_by_css_selector('div[data-testid="price-and-discounted-price"] span')[-1].text
    taxas = elemento.find_element_by_css_selector('div[data-testid="taxes-and-charges"]').text
    coleta_dados.append([nome, score, valor, taxas])

driver.quit()

# Criação de arquivo em Excel
#wb = xlsxwriter.Workbook(rf'C:/Users/Wilber Godoy/Documents/Aula5/{regiao}.xlsx')
wb = xlsxwriter.Workbook(rf'{regiao}.xlsx')
ws = wb.add_worksheet('Planilha1')
bold = wb.add_format({'bold':1})
ws.write('A1','Nome Hotel', bold)
ws.write('B1','Avaliação', bold)
ws.write('C1','Valor', bold)
ws.write('D1','Taxas', bold)
row, col = 1, 0
for line in coleta_dados:
    ws.write_string(row, col, line[0])
    ws.write_string(row, col+1, line[1])
    ws.write_string(row, col+2, line[2])
    ws.write_string(row, col+3, line[3])
    row +=1
wb.close()