import os

def rate1():
    pass

def rate2():
    pass

def rate3():
    pass

def rate4():
    pass

def rate5():
    pass

def rate6():
    pass

def generate(wordList):
    rate = input("Set the combination rate(1-6)\n=>")
    if (rate = "1"):
        rate1()
    elif (rate = "2"):
        rate2()
    elif (rate = "3"):
        rate3()
    if (rate = "4"):
        rate4()
    if (rate = "5"):
        rate5()
    if (rate = "6"):
        rate6()

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
    Confirm = input("Are you okay to continue [y/n]\n=>")
    validInput = 1
    #checking whether user is giving valid response
    while(validInput != 0):
        if(Confirm.lower() in ("y","yes","yup")):
            validInput = 0
            generate(wordList)
        elif(Confirm.lower() in ("n","no","nah")):
            validInput = 0
            getter()
        elif(Confirm.lower() == "exit"):
            validInput = 0
            exit()
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
