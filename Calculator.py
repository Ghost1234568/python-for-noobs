#def() is a function which allows us define certain value inside it
#return is a function which gives back the output
def add(x, y):
    return (x + y)
def sub(x, y):
    return (x - y)
def multi(x, y):
    return (x * y)
def div(x, y):
    return (x / y)
def power(x, y):
    return (x ** y)


print("""addition\nsubtraction\nmultiplication\ndivision\nexponent\n""")


x = int(input("Enter the number\n"))
y = int(input("Enter the number\n"))

a = input("Enter what to do\n")

if a == "addition":
    add(x, y)
elif a == "subtraction":
    sub(x, y)
elif a == "multiplication":
    multi(a, y)
elif a == "division":
    div(x, y)
elif a == "exponent":
    power(x, y)
else:
    print("Invalid command")
