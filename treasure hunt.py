print("Welcome to treasure island your mission is to find treasure")
direction = input("Give your direction as left or right :").lower()
while True:
    if direction == "left":
        swim_or_not = input("Swim or wait : ").lower()
        if swim_or_not == "wait":
            door = input("Choose the door \nred\tyellow\tblue :").lower()
            if door == "yellow":
                print("You have win the game ")
                break
            else:
                print("Game over")
                break
        else:
            print("Game over")
            break
    else:
        print("Game over")
        break