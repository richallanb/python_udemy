"""
Tuples lesson
"""

### Tuples
t = ("Norway", 4.953, 3)
print(t)

#### Iterate over tuple like an array
for item in t:
    print(item)

#### Append to the tuple
u = t + (123, 456)
print(u)

#### Duplicates data inside tuple
v = t * 2
print(v)

#### Nested tuples
w = ((220, 284), (1184, 1210), ('a', 'b', 'c'))
print(w)
print(w[2])
print(w[2][0])

#### Tuple literal with a single element
x = (391,)
#### Empty tuple
y = ()

#### Return a tuple
def minmax(items):
    return min(items), max(items)

z=minmax([83,33,84,32,85,31,86])
print(z)

#### Unpacking tuples
lowerVal, upperVal = z
print(lowerVal)
print(upperVal)

#### Nested tuple unpacking
(a, (b, (c,d))) = (4,(3, (2,1)))
print(a,b,c,d)

#### Swapping values using tuple construction and unpacking
a = 'jelly'
b = 'bean'
print(a, b)
a, b = (b, a)
print(a, b)

#### Tuple casting
tuple([1,2,3])
tuple("String value")

#### Testing for if item exists
print(5 in (3, 5, 17, 257))
print(5 not in (3, 5, 17, 257))

