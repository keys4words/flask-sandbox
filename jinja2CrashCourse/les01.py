from jinja2 import Template

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

# render templates with params
person = Person('james', 45)
template = Template("Hey, I am {{p.name.upper()}} and I'm {{p.getAge()-5}} years old")
msg = template.render(p=person)

print(msg)

# for loop & "-"% for removing \n in output stream
cities = [{'id': 1, 'city': 'Москва'},
            {'id': 2, 'city': 'Тверь'},
            {'id': 5, 'city': 'Владимир'},
            {'id': 7, 'city': 'Калуга'},
            {'id': 11, 'city': 'Ярославль'},
            {'id': 17, 'city': 'Смоленск'}]

print('='*35)
link = '''<select name="cities">
{% for city in cities -%}
{% if city.id > 6 -%}
    <option value="{{ city.id }}">{{ city.city }}</option>
{% else -%}
    {{city.city}}
{% endif -%}
{% endfor -%}
</select>'''
template2 = Template(link)
msg2 = template2.render(cities=cities)
print(msg2)
