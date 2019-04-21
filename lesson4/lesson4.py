p = [1,2,3]
q = [1,2,3]
# Value equality
print(p == q)
# Reference equality
print(p is q)
## id(obj) returns the object reference id
print(id(p), id(q))

m = [9, 15, 24]
def modify(k):
    # has a side-effect on the object referenced
    k.append(39)
    print('k = ', k)

print(m)
# passing in object reference
modify(m)
print(m)

# Responsibility of the function to make a copy of the object
f = [14, 23, 37]
def replace(g):
    # Assigns new object to variable g
    g = [17, 28, 45]
    print("g = ", g)

print(f)
replace(f)
print(f)

def replace_contents(g):
    rep = [17, 28, 45]
    for i in range(len(g)):
        g[i] = rep[i]
    print("g = ", g)

print(f)
replace_contents(f)
print(f)

# All functions pass by reference
test = lambda x: x
c = [6, 10, 16]
e = test(c)
print(c is e)

# Default arguments
## Default arguments must come after arguments without defaults
def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner('Norwegian Blue')

#Calling functions with named arguments
banner(border='~', message='Hello from Earth')