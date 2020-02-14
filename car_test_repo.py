from Shiny_parts_test import *

print('Testing make part')
print(make_parts('metals', 'labours') == 'Shiny Parts')

print('Testing build_cars')
print(build_car('Shiny Parts') == 'making car')