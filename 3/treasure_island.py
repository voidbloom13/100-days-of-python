def main():
    print("Welcome to Treasure Island")
    print("Your mission is to find the treasure.")
    
    choice = input("You come across a crossroad. Do you go left or right? ").lower()
    if choice != "left":
        print("You fell into a hole.\nGame Over!")
        quit()
    
    choice = input("You've come to a lake. There is an island in the middle of the lake. Do you wait for a boat or swim across? ").lower()
    if choice != "wait":
        print("You were attacked by slaughterfish.\nGame Over!")
        quit()
    
    choice = input("You come across 3 doors: a red, a blue, and a yellow. Which do you open? ").lower()
    if choice == "blue":
        print("You were eaten by beasts.\nGame Over!")
        quit()
    elif choice == "red":
        print("You were burned in a fire.\nGame Over!")
        quit()
    elif choice == "yellow":
        print("You found the treasure.\nYou Win!")
        quit()
    else: print("Game Over!")
    quit()    

if __name__ == "__main__":
    main()