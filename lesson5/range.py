"""
Range lesson
"""

for i in range(5):
    print(i)

z = list(range(2,5))
print(z)

# Step argument
z = list(range(0, 10, 2))
print(z)

# Don't use
x = [0, 1, 4, 6, 13]
for i in range(len(x)):
    print(x[i])

# Do either
for i in x:
    print(i)

# Or (will return a pair of index, value)
for index, value in enumerate(x):
    print(index, value)