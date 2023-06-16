from reactpy import component, html, use_state
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from components import List
from styles import style

@component
def App ():
  initial = 1
  page, set_page = use_state(initial)
  
  def back_page ():
    set_page(page - 1) if page > 1 else set_page(1)
  
  def next_page ():
    set_page(page + 1) 
  
  return html.div({"style": {"display": "flex", "flex-direction": "column", "align-items": "center"}},
    html.h1({"style": { "color": "#2ad" }}, 'Rick And Morty'),
    List.ListItems(page),
    html.div(
      {"style": style.container_button},
      html.button({"on_click": lambda event: back_page(), "style": style.button}, 'back page'),
      html.p({"style": {"font-size": 20}}, f'Pagina {page}'),
      html.button({"on_click": lambda event: next_page(), "style": style.button}, 'next page')
    )
    
  )

app = FastAPI()
configure(app, App)