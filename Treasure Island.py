def island():
    print ("Welcome to Treasure Island.\n Your mission is to find the treasure.")
    x = input('You are at a cross road. Where do you want to go? Type "left or "right"\n')
    if x == 'right':
        return "Game over"
    x = input('you come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n')
    if x == ('swim'):
        return "Game over"
    x = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n')
    if x == 'red' or x == 'blue':
        return "Game over"
    elif x =='yellow':
        return "You win"
print (island())