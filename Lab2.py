name = input("What is your name? ")
print("Hello " + name)

choice = True
while choice == True:
        num = int(input("enter number between 1 and 100: "))
        if num < 0 or num > 100:
                print("invalid number try again "+ name)
        else:
                if num %2 != 0 and num < 60:
                        print(f"{num} odd and less than 60")
                elif num % 2 ==0 and num > 2 and num < 25:
                        print(f"{num} even and less than 25")
                elif num % 2 ==0 and num >= 26 and num < 60:
                        print(f"{num} even and between 26 and 60")
                elif num % 2 ==0 and num > 60:
                        print(f"{num} even and greater than 60")
                elif num % 2 !=0 and num > 60:
                        print(f"{num} odd and greater than 60")
                choice = input(("would you like to continue the program " + name + "? y/n "))
                while choice == 'y':
                        if choice == 'y':
                                choice = True
                        elif choice == 'n':
                                choice = False


