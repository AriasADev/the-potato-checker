def potato_checker():
    while True:
        print("---- Potato Checker 9000 ----")
        print(r"As I'm sure we have all heard, everything in this universe is either a potato, or not a potato, therefore, statistically, 50% of everything is a potato. But how are we supposed to know what is a potato, and what isn't?! That's why I have built this amazing program to help you figure it out!")
        print("")
        
        potato = input("What is your object? ")
        if potato.lower() == "potato":
            print("That is a potato!")
        else:
            print("Not a potato :(")
        
        restart = input("\nPress 'r' to restart or any other key to exit... ").lower()
        if restart != 'r':
            break
potato_checker()
