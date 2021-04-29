import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True


print("Comp turn: Rock(r) Paper(p) Sisor(s)") 
comp = random.randint(1, 3)
if comp == 1:
    comp = 'r'
elif comp == 2:
    comp = 'p'
elif comp == 3:
    comp = 's'
you = input("Your turn: Rock(r) Paper(p) Sisor(s)") 
a = gameWin(comp, you)


print(f"Comp chose : {comp} ")
print(f"You chose : {you} ")
if a == True:
    print("Congratulations! You Win \n")
elif a == False:
    print("Sorry! You Lost")
elif a == None:
    print("Game is a tie! Let's Play Again!!")
