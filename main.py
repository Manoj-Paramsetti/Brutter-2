import os

def rate1(wordList):
    print("Do you want to save the file in seperate file or copy it manually[file/copy]: ")
    res = input("")

def rate2(wordList):
    final = []
    for i in wordList:
        for j in wordList:
            final.append(i+j)
    print(final)
    print("Do you want to save the file in seperate file or copy it manually[file/copy]: ")
    res = input("")

def rate3(wordList):
    print("Do you want to save the file in seperate file or copy it manually[file/copy]: ")
    res = input("")

def rate4(wordList):
    print("Do you want to save the file in seperate file or copy it manually[file/copy]: ")
    res = input("")

def rate5(wordList):
    print("Do you want to save the file in seperate file or copy it manually[file/copy]: ")
    res = input("")

def rate6(wordList):
    print("Do you want to save the file in seperate file or copy it manually[file/copy]: ")
    res = input("")

def generate(wordList):
    rate = input("Set the combination rate(1-6)\n=>")
    if (rate == "1"):
        rate1(wordList)
    elif (rate == "2"):
        rate2(wordList)
    elif (rate == "3"):
        rate3(wordList)
    elif (rate == "4"):
        rate4(wordList)
    elif (rate == "5"):
        rate5(wordList)
    elif (rate == "6"):
        rate6(wordList)
    else:
        print("Out of limit or invalid input")
        generate(wordList)
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
