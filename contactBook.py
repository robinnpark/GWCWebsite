myCont = {"Father":"562)522-4470", "Mother":"562)522-4471"}

addContact = True

while addContact == True:
    print("Would you like to add a Contact? (y/n)")
    answer = input().lower()
    if(answer == 'y'):
        print("What is the name?")
        name = input().lower()
        print("Do you want to add a number, address, both, or niether?")
        answer = input().lower()
        if(answer == 'number'):
            print("What is the number?")
            number = input()

            myCont[name] = number

        if(answer == 'address'):
            print("What is the address?")
            address = input()

            myCont[name] = address

        if(answer == 'both')
            print("What is the number?")
            number = input()

            print("What is the address?")
            address = input()

            myCont[name] = []
            myCont[name].append(number)
            myCont[name].append(address)

        if(answer =='neither')
           print()
            
        elif (answer == 'n'):
            print("Do you want to add an address?")
            address = input().lower()
            addContact = False

