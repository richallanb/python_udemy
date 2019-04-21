from math import factorial as fac
n = 100
k = 2
print(fac(n) / (fac(k) * fac(n - k)))
print(len(str(fac(n))))

binary = 0b10
octal = 0o10
hex = 0x10
print(binary, octal, hex)

parsedInt = int("-192") + 2
print(parsedInt)
## Won't auto convert
## print(2 + "-192")

print(3e8, 1.616e-35)
a = None # null value
print(a)
print(a is None)

#bool(0) = false
#bool(23) = true
#bool(-1) = true
#bool(0.0) = false
#bool(0.1) = true
#bool([]) = false
#bool([1,2,3]) = true
#bool("") = false
#bool("Spam")

# Can't convert true & false strings
# bool("False") = true

if True:
    print("It's true!")

if  False:
    print ("It's false")

if bool("eggs"):
    print("Eggs!")

if "eggs":
    print ("More eggs!")

h = 12
if h > 50:
    print("Greater than 50")
elif h < 20:
    print("Less than 20")
else:
    print("50 or smaller")

c = 5
while c > 0:
    print(c)
    c -= 1


# analogous to 
# do {
# ..
# } while(someCondition);

while True:
    response = input()
    if int(response) % 7 == 0:
        print ("You finally guessed it! (", response, ")")
        break

