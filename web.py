import requests
from bs4 import BeautifulSoup

site = "https://www.fundsexplorer.com.br/funds/"

html = requests.get(site).content

dados = BeautifulSoup(html, 'html.parser')

preco = dados.find("span", class_="price")
ultimo_rendimento = dados.find_all("span", class_="indicator-value")
liquidez_diaria = dados.find_all("span", class_="indicator-value")
dividend_yield = dados.find_all("span", class_="indicator-value")
patrimonio_liquido = dados.find_all("span", class_="indicator-value")
valor_patrimonial = dados.find_all("span", class_="indicator-value")
rentabilidade_mes = dados.find_all("span", class_="indicator-value")
p_vp = dados.find_all("span", class_="indicator-value")
print("Preço:", preco.text[19:])
print("Ultimo Rendimento:", ultimo_rendimento[1].text[20:])
print("Liquidez Diária:", liquidez_diaria[0].text[16:])
print("Dividend Yield:", dividend_yield[2].text[17:])
print("Patrimônio Líquido:", patrimonio_liquido[3].text[16:])
print("Valor Patrimonial:", valor_patrimonial[4].text[16:])
print("Rentabilidade No Mes:", rentabilidade_mes[5].text[16:])
print("P/VP", p_vp[6].text[16:])
