from replit import clear

bids = {}
i = 0
winner = ['none', 0]

while i != 1:
    name = input('What is your name?')
    amount = int(input("What is your bid?"))
    bids[name] = amount
    clear()
    answer = input('Is there another bidder?')
    if answer == "no":
        i = 1
    clear()
for bidder in bids:
    if bids[bidder] > winner[1]:
        winner = [bidder, bids[bidder]]
print (winner[0],"is the winner with a bid of:", winner[1])
input()
