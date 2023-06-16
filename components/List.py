import requests
from reactpy import component, html
from components import Item

def fetchData (page):
  response = requests.get(f'https://rickandmortyapi.com/api/character/?page={page}')
  if response.status_code == 200:
      data = response.json()
      return data
  else:
      print('Error:', response.status_code)
      return None

@component
def ListItems(page):
  data = fetchData(page)
  componente = [Item.Character(item) for item in data['results']]
  return html.ul({"style": {"width": "100%", "display": "flex", "flex-wrap": "wrap", "gap": 20, "justify-content": "center"}}, componente)

