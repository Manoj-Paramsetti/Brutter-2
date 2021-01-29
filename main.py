import os

def generate():
    pass
def getter():
    #intialization
    wordList=[]
    wordList.append('')
    #getting input for importing words
    print("How many words you wanna add?")
    NWords = int(input("=>"))
    for i in range(NWords):
        print("What is the word {}".format(i+1))
        wordList.append(input("=>"))
    print("Hey! you added all your words for wordlist, Check your list again,\n{}".format(wordList))
    Confirm = input("Are you okay to continue [y/n]\n=>"):
    validInput = 1
    #checking whether user is giving valid response
    while(validInput != 0):
        if(Confirm.lower() in ("y","yes","yup")):
            validInput = 0
            generate()
        elif(Confirm.lower() in ("n","no","nah")):
            validInput = 0
            getter()
        elif(Confirm.lower() == "exit")
            validInput = 0
        else:
            print("Enter the valid thing")

try:
    print("Welcome to brutter")
    print('Type "help" for the help or Type "about" to know more about the project')
    user = input("=>")
    user = user.lower()
    while(user != "exit"):
        if (user == "generate"):
            getter()
        user = input("=>")
except (KeyboardInterrupt):
    print('\nUse safe exit by typing "exit"')
