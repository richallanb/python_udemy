"""Demonstrate scoping."""

count = 0

def show_count():
    print('count = ', count)
def set_count(c):
    ## Needed to address count in outside scope
    global count
    ## This would otherwise create a local variable count
    count = c
