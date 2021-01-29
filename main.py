try:
    def caller():
        user = input("=>")
        user = user.lower()
        while(user != "exit"):
            if (user == "generate"):
                getter()
            elif (user == "help"):
                helper()
            elif (user == "about"):
                storyTeller()
            user = input("=>").lower()
    def helper():
        print('''\n\n\nCOMMANDS
========

about:
 It will show a short description of this script
generate:
 It will start your work
 Further input is provided in the square bracket so, check that and give the write option to generate success. I'm a lazy guy so, not able to explain more.

help:
 It will show this message again so, Don't execute it once again. It's not a bug. it is a feature

 ''')
    def storyTeller():
        print('''\n\n\nBrutter is developed by Paramsetti Manoj. You can generate a wordlist using this script.

Disclaimer:
Use this script for educational purposes. The author doesn't claim any stupid thing which is done by you.

How to use this program?
It is having a command "help" which will explain to you a lot about how to use this script. I'll provide a short tutorial after some days so have a touch on my Github. visit my project and if you like this project then give a star. https://github.com/Manoj-Paramsetti/Brutter-2

When the project is created?
29 Jan 2021

Whether it got a license?
Yeah, Check the LICENSE file. It is an MIT license

Have you got any issues?
Raise an issue in my repository. Visit here https://github.com/Manoj-Paramsetti/Brutter-2/issues
Waiting to see the issues

''')
    def rate1(wordList):
        print("Do you want to save the file in seperate file or copy it manually[file/copy]: ")
        res = input("")
        if (res.lower() == "copy"):
            for i in wordList:
                print(i)
        elif(res.lower() == "exit"):
            exit()
        else:
            with open("pass.txt","a") as f:
                for i in wordList:
                    f.write(i)
                    f.write("\n")

    def rate2(wordList):
        final = []
        for i in wordList:
            for j in wordList:
                final.append(i+j)
        print("Do you want to save the file in seperate file or copy it manually[file/copy]: ")
        print("Default is copying in file")
        res = input("=>")
        if (res.lower() == "copy"):
            for i in final:
                print(i)
        elif(res.lower() == "exit"):
            exit()
        else:
            with open("pass.txt","a") as f:
                for i in final:
                    f.write(i)
                    f.write("\n")

    def rate3(wordList):
        final = []
        for i in wordList:
            for j in wordList:
                for k in wordList:
                    final.append(i+j+k)
        print("Do you want to save the file in seperate file or copy it manually[file/copy]: ")
        res = input("=>")
        if (res.lower() == "copy"):
            for i in final:
                print(i)
        elif(res.lower() == "exit"):
            exit()
        else:
            with open("pass.txt","a") as f:
                for i in final:
                    f.write(i)
                    f.write("\n")

    def rate4(wordList):
        final = []
        for i in wordList:
            for j in wordList:
                for k in wordList:
                    for l in wordList:
                        final.append(i+j+k+l)
        print("Do you want to save the file in seperate file or copy it manually[file/copy]: ")
        res = input("=>")
        if (res.lower() == "copy"):
            for i in final:
                print(i)
        elif(res.lower() == "exit"):
            exit()
        else:
            with open("pass.txt","a") as f:
                for i in final:
                    f.write(i)
                    f.write("\n")

    def rate5(wordList):
        final = []
        for i in wordList:
            for j in wordList:
                for k in wordList:
                    for l in wordList:
                        for m in wordList:
                            final.append(i+j+k+l+m)
        print("Do you want to save the file in seperate file or copy it manually[file/copy]: ")
        res = input("=>")
        if (res.lower() == "copy"):
            for i in final:
                print(i)
        elif(res.lower() == "exit"):
            exit()
        else:
            with open("pass.txt","a") as f:
                for i in final:
                    f.write(i)
                    f.write("\n")

    def rate6(wordList):
        final = []
        for i in wordList:
            for j in wordList:
                for k in wordList:
                    for l in wordList:
                        for m in wordList:
                            for n in wordList:
                                final.append(i+j+k+l+m+n)

        print("Do you want to save the file in seperate file or copy it manually[file/copy]: ")
        res = input("=>")
        if (res.lower() == "copy"):
            for i in final:
                print(i)
        elif(res.lower() == "exit"):
            exit()
        else:
            with open("pass.txt","a") as f:
                for i in final:
                    f.write(i)
                    f.write("\n")

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
    print(''' _                _   _
| |__  _ __ _   _| |_| |_ ___ _ __
| '_ \\| '__| | | | __| __/ _ \\ '__|
| |_) | |  | |_| | |_| ||  __/ |
|_.__/|_|   \\__,_|\\__|\\__\\___|_|

''')
    print("Disclaimer: use this script for educational purposes. The author doesn't claim any stupid thing which is done by you.")
    print("Welcome to brutter")
    print("Credits: Paramsetti Manoj")
    print('Type "help" for the help or Type "about" to know more about the project')
    caller()
except (KeyboardInterrupt):
    print('\nUse safe exit by typing "exit"')
