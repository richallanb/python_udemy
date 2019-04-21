import time

# Default argument is only evaluated once before function execution
def show_default(arg=time.ctime()):
    print(arg)

# Evaluated once, so it keeps re-using the same default argument object
def add_spam(menu=[]):
    menu.append("spam")
    return menu

breakfast = ['bacon', 'eggs']
print(add_spam(breakfast))
lunch = ['baked_beans']
print(add_spam(lunch))
print(add_spam())
print(add_spam())

print('''
------------spam2----------
''')
# Set the default value to None as a means to initialize the value each function execution
def add_spam2(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu

breakfast = ['bacon', 'eggs']
print(add_spam2(breakfast))
lunch = ['baked_beans']
print(add_spam2(lunch))
print(add_spam2())
print(add_spam2())