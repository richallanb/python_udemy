"""
Dict Lesson
"""
# pretty print
from pprint import pprint as pretty

# Can copy array of tuples into dict
names_and_ages = [('Alice', 32), ('Bob', 48), ('Charlie', 28), ('Daniel', 33)]
d = dict(names_and_ages)
pretty(d)
# Can create dict from key arguments
phonetic = dict(a='alpha', b='bravo', c='charlie', d='delta', e='echo', f='foxtrot')
pretty(phonetic)

## Can copy using
copy = dict(phonetic)

## Adding to a dict
copy.update(d)
pretty(copy)

## Updating and adding values
stocks = {'GOOG': 891, 'AAPL': 416, 'IBM': 194}
stocks.update({'GOOG': 894, 'YHOO': 25})
pretty(stocks)

## Just extracting the values
for value in stocks.values():
    pretty(value)

## Getting the items (entry pairs)
for key, value in stocks.items():
    pretty('{key}: {value}'.format(key = key, value = value))

## in and not in only work on keys
pretty('YHOO' in stocks)
pretty(25 in stocks)

## Another way to add to dicts
m = {'a': 1, 'b': 2, 'c': 3}
m['d'] = 5
pretty(m)