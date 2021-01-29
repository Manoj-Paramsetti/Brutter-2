import os

def generate():
    wordList=[]
    print("How many words you wanna add?")
    NWords = int(input("=>"))
    for i in range(NWords):
        print("What is the word {}".format(i+1))
        wordList.append(input("=>"))
    print(wordList)

try:
    print("Welcome to brutter")
    print('Type "help" for the help or Type "about" to know more about the project')
    user = input("=>")
    user = user.lower()
    while(user != "exit"):
        if (user == "generate"):
            generate()
        user = input("=>")
except (KeyboardInterrupt):
    print('\nUse safe exit by typing "exit"')
