import random
def gamewin(comp, you):
    if comp == you:
        return None
        # if computer chose snake(s)
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
            # if computer chose water(w)
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True                
            # if computer chose gun(g)
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("comp turn: Snake(s), Water(w), Gun(g)?")
randno=random.randint(1,3)

if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'

you= input("Your turn: Snake(s), Water(w), Gun(g)?")

a= gamewin(comp, you)

print(f"Computer Chose {comp}")
print(f"You Chose {you}")

if a == None:
    print("the game is tie!...")
elif a:
    print("you win!...")
else:
    print("you lose!...")

