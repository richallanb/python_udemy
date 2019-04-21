# Strong and dynamically typed
def add(a, b):
    return a+b

print(add(5,7))
print(add(3.1, 2.4))
print(add("news", "paper"))
print(add([1,2], [3,4]))

#No implicit type conversion
add("The answer is", 42)