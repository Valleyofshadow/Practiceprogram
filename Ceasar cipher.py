letters = [("a",1), ("b",2), ("c",3), ("d", 4), ("e", 5), ("f", 6), ("g",7),("h",8),("i",9),("j",10),("k",11),("l",12),("m",13),("n",14),("o",15),("p",16),("q",17),("r",18),("s",19),("t",20),("u",21),("v",22),("w",23),("x",24),("y",25),("z",26),(" ", 27)]

def encrypt(message,shift,letters):
    code = []
    shift = int(shift)
    for i in message:
        t = 0
        while t < len(letters):
            if letters[t][0] == i:
                code.append(letters[t-shift][0])
            t += 1
    code2 = code [0]
    z = 1
    while z < len(code):
        code2 += code[z]
        z += 1
    return code2

def decode(message, shift, letters):
    code = []
    shift = int(shift)
    for i in message:
        t = 0
        while t < len(letters):
            if letters[t][0] == i:
                if t+shift >= len(letters):
                    code.append(letters[((t + shift)-27)][0])
                else:
                    code.append(letters[t + shift][0])
            t += 1
    code2 = code [0]
    z = 1
    while z < len(code):
        code2 += code[z]
        z += 1
    return code2

cont = 0
while cont != 1:
    x = input ("Type '1' to encrypt, type '2' to derypt:\n")
    message = input("Type your message:\n")
    shift = input("Type the shift number:\n")
    if x == ("1"):
        print (encrypt(message,shift,letters))
    elif x == ("2"):
        print(decode(message, shift, letters))
    again = input('Would you like to try again?\n')
    if again == "no":
        cont = 1


input()