"""
List lesson
"""
s = "show how to index into sequences".split()

for i in range(1, len(s) + 1):
    print(s[len(s) - i])
    # is the same as
    print(s[-i])

## Slicing an array
### seq[start:stop] -> start inclusive, stop exclusive
y = s[1:4]
print(y)

## Slicing with negative indices
### Takes everything except the first and last
y = s[1:-1]
print(y)

## stop argument is optional (it's the length of the array by default)
x = s[3:len(s)]
print(x)
### same as
t = s[3:]
print(t)

## start argument is optional (it's 0 by default)
x = s[0:3]
print(x)
### same as
t = s[:3]
print(t)

## Can copy lists with
copy_list = s[:]
print(copy_list)
print('same list? {same}, equal? {equal}'.format(same=copy_list is s, equal=copy_list == s))

## Can also copy with
u = s.copy()
v = list(s)
print(s == v, s == u)

## List reptition (size initialization)
### Only copies references, not data
CONST_SIZE = 32
container = [0] * CONST_SIZE
print(container)

inner_list = [-1,1]
outer_list = [inner_list] * 5
print(outer_list)
inner_list[0] = 'fuck'
print(outer_list)

## Lookup
### Truthy
w = 'the quick brown fox jumps over the lazy dog'.split()
print('fox' in w)
print('shit' not in w)

### Location
print(w.index('fox'))

### Remove items
copy_w = list(w)
del copy_w[1]
print(copy_w)
#### same as
copy_w = list(w)
copy_w.remove('quick')
print(copy_w)


## Concatenation
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
# same as
a += b
print(a)

h = 'not perplexing do handwriting family where I illegibly know doctors'.split()
# Sorts on the list
## Sort by word length
h.sort(key = len)
print(h)
## Sort alphabetically and by case
h.sort()
print(h)
## Sort alphabetically ignoring case
h.sort(key = lambda x:x[0].lower())
print(h)

#A more functional approach
## Sorts on the second letter in the word
### Notice the ternary

k = sorted(h, key = lambda x: x[1].lower() if len(x) > 1 else x[0].lower())
print(k)
print(h)