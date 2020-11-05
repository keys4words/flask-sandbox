from jinja2 import Template, escape

# raw string
data = '''{% raw %}Модуль Jinja вместо
определения {{ name }}
подставляет соответствующее значение{% endraw %}'''

template = Template(data)
msg = template.render(name='Maximus')
print(msg)


#  string with escaped symbols
link = '''В HTML-документе ссылки определяются так:
<a href="#">Ссылка</a>'''

print('='*35)
template2 = Template("{{ link | e }}")
msg2 = template2.render(link=link)
print(msg2)

#  string with escaped symbols by escape

print('='*35)
link2 = '''В HTML-документе ссылки определяются так:
<a href="#">Ссылка</a>'''
msg3 = escape(link2)
print(msg3)