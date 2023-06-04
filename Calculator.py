# "def()" is a function which allows us define certain value inside it
# "print" is a function which gives back the output
def add(x, y):
   print(x + y)
def sub(x, y):
    print(x - y)
def multi(x, y):
    print (x * y)
def div(x, y):
    print(x / y)
def power(x, y):
    print(x ** y)
   
print("""addition\nsubtraction\nmultiplication\ndivision\nexponent\n""") #print function display what we entered in the "" or ''

x = int(input("Enter the number\n"))# Here x is a variable where i can give a value to it and int is called integer similarly we have float, bool, complex, str ect..
y = int(input("Enter the number\n"))# "input" function allow's us to enter our own value
a = input("Enter what to do\n")

if a == "addition":# "if" is an condition statment followed by "elif" and "else"
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
# Follow me for python content
