from reactpy import component, html

@component
def Character(item):
  return html.li(
    {"style": {"background": "#eeeeef", "list-style": "none", "width": 350}},
    html.div(
      {"style": {"height": 200, "width": "100%"}},
      html.img({"src": item["image"], "style": {"width": "100%", "height": "100%"}})),
    html.h3(item['name']),
    html.p(item['species']),
    html.p(item['gender']),
    html.p(item['type'])
  )
