#GLOBAL VARIABLES
codeWords = []
realWords = []



#FUNCTIONS
def createCodeWords():

    codingWords = True 
    
    
    while codingWords:
        print("Would you like to add a word to your code word? (y/n)")
        answer = input().lower()

        if (answer == 'y'):
            print("What is the real word?")
            real = input().lower()
            realWords.append(real)
            print("What is the code word?")
            code = input().lower()
            codeWords.append(code)
        elif (answer == 'n'):
            print("Your code words have been saved!")
            codingWords = False
            

        else:
            print("Security break! Abort mission")
            exit()


def encryptMessage():

    print()
    print("________________")
    print()

    print("What is your message that you would like encrypted?")
    message = input().lower()
    wordList = message.split()

    codedMessage = ""
    for word in wordList:
        for realWord in realWords:
            #print("Checking words " + word + " and " +realWord)
            if (word == realWord):
                #print("I FOUND A MATCH!")
                codedMessage = codedMessage + " " + codeWords[0]
                
            else:
                codedMessage = codedMessage + " " + word

    print(codedMessage)    

#RUNNING CODE
createCodeWords()
encryptMessage()
