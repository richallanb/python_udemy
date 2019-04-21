"""
Strings lesson
"""

## Join function
colors = ';'.join(['#45ff23', '#2321fa', '#1298a3', '#a32312'])
print(colors)

print(colors.split(';'))

## partition function
departure, _, arrival = 'London:Edinburgh'.partition(':')
print('Departing', departure, 'and arriving in', arrival)

## format function
t = 'The age of {name} is {age}'.format(name='Jim', age=32)
print(t)

import math
print('Math constants: pi={m.pi:.3f}, e={m.e:.3f}'.format(m=math))

obj = {'name':'Jim', 'age':32, 'asshole': {'often': True, 'rarely': False}}
print("The age of {name} is {age}. He's an asshole often?{asshole[often]}".format(**obj))