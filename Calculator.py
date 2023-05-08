from replit import clear

def multiply(x,y):
    return x * y
def subtract(x,y):
    return x-y
def add(x,y):
    return x + y
def divid(x,y):
    return x / y
def solve(n1, s, n2):
    if s == "+":
        return add(n1,n2)
    if s == "-":
        return subtract(n1,n2)
    if s == "*":
        return multiply(n1,n2)
    if s == "/":
        return divid(n1,n2)

x = 0

while x != 1:
    n1 = float(input("What's the first number?: "))
    s = str(input("+\n-\n*\n/\nPick an operation: "))
    n2 = float(input("What's the next number?: "))
    solution = solve(n1, s, n2)
    print (n1,s, n2, "=", solution)
    print (" Type 'y' to continue calculating with", n1, "or type 'n' to start a new calculation: ")
    t = input()
    if t == 'n':
        clear()
    elif t == 'end':
        x = 1
    elif t == 'y':
        n1 = solution
