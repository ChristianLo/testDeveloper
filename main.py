import requests as r
from bs4 import BeautifulSoup as bs
import json

site = r.get('https://snifa.sma.gob.cl/Sancionatorio/Resultado', headers={'Content-Type': 'text/html; charset=utf-8'}).text
soup = bs(site, 'html.parser')

site_table = soup.find('table', {'id': 'myTable'})
site_table_rows = site_table.find_all('tr')

data = []

for row in site_table_rows:
    if row == site_table_rows[0]:
      continue
    else:
      row_data = row.find_all('td')
      data.append({
        'model': 'Tarea2.Sancionatorios',
        'fields': {
          'expediente': row_data[1].text,
          'region': row_data[5].text.strip('\n'),
          'estado': row_data[6].text.strip('\n'),
          'link': f'https://snifa.sma.gob.cl{row_data[7].find("a")["href"]}'
        }
      })
      
      for fiscalizacion in row_data[2].text.strip('\n').split('\n'):
        data.append({
          'model': 'Tarea2.Fiscalizacion',
          'fields': {
            'id_sanionatorio': row_data[1].text,
            'name': fiscalizacion
        }
      })
        
      for categoria in row_data[4].text.strip('\n').split('\n'):
        data.append({
          'model': 'Tarea2.Categoria',
          'fields': {
            'id_sanionatorio': row_data[1].text,
            'name': categoria
        }
      })
        
      for razon in row_data[3].text.strip('\n').split('\n'):
        data.append({
          'model': 'Tarea2.RazonSocial',
          'fields': {
            'id_sanionatorio': row_data[1].text,
            'name': razon
        }
      })

# save data in json file
with open('fixtures/data.json', 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
    