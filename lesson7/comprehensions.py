words = 'Why sometimes I have believed as many as six impossible things before breakfast'.split()
comp = [len(word) for word in words]
print(comp)

from math import factorial
f = [factorial(x) for x in range(20)]
print(f)

## composition
import functools
import numpy
data = ['id1', 'id2', 'id3', 'id4']
rel = [{'id':'id5', 
        'from':'id1', 
        'to':'id3'}, 
    {'id':'id6', 
     'from':'id2', 
      'to':'id4'}, 
    {'id':'id7', 
     'from':'id3', 
     'to':'id2'}]
getRelId = lambda id: [currRel['id'] for currRel in rel if currRel['from'] == id or currRel['to'] == id]
relIdList = functools.reduce(lambda acc, id: acc + getRelId(id), data, [])
relIdList = numpy.unique(relIdList)

print(relIdList)

country_to_capital = {'United Kingdom': 'London',
                    'Brazil': 'Brazilia',
                    'Morocco': 'Rabat',
                    'Sweden': 'Stockholm'}
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
print(capital_to_country)

words = ['hi', 'hello', 'foxtrot', 'hotel']
wut = functools.reduce(lambda acc, word: acc.update({word[0]: [word] if word[0] not in acc else acc[word[0]] + [word]}) or acc, 
                        words, dict())
print(wut)
