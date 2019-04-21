print("what" "ever")
multi = """
<html>
    <body>
    </body>
</html>
"""
print(multi)

# raw strings (no escaping)
print(r'C:\Windows\System32\win.exe')

#strings are arrays
s = 'string'
for i in range(len(s)):
    print(s[i])

c = 'oslo'
print(c.upper())

## All strings are unicode (UTF-8) based

#byte literal
b = b'some bytes'
print(b.split())

l = list("stuff")
print(l)

waka = ['bear',
        'test',
        'what'
]
print (waka)

## dictionary -> javascript object
d = {'alice': '123', 'bob': '456', 'eve': {'bitch': True, 'number': '666'}}
print(d)
d['charles'] = '555'
print(d)

################################

cities = ['London', 'New York', 'Paris', 'Oslo', 'Helsinki']
for city in cities:
    print(city)

colors = {'crimson': 0xdc143c,
          'coral': 0xff7f50,
          'teal': 0x008080}
for color in colors:
    print (color, colors[color])

#functions
def square(x):
    return x * x

squareFunc = lambda x: x * x

print(square(2), squareFunc(2))
