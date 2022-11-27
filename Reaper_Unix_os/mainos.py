from googlesearch import search
import random
import os
from time import sleep

while True:
    cmd = input("")
    if cmd == 'credits':
        print("ceo/owner: Pranesh B \nIDE: Microsoft visual studio\nhelp source: Microsoft Bing")
        continue
    elif cmd == 'say':
        text = input("enter the text you want it to say: ")
        print(text)
        continue
    elif cmd == 'search':

        query = input("enter the text you want it to search: ")

        for i in search(query, num=200, stop=None, ):
            print(i)
            continue
    elif cmd == 'random':
        lis = input("enter the options right like :(option1, option2, option3 and so on and on)")
        random_num = random.choice(lis)
 
        print("Random selected number is : " + str(random_num))
    elif cmd == 'delete-account':
        def dele():
            os.remove("credintals.txt")
            execfile('mainrun.py')
            os._exit(0)
        def survey():
            my_file = open("surveyresult.txt","w+")
            a = input("why are you deleting your account: ")
            my_file.write("reason for deleting account: ")
            my_file.write(a)
            b = input("what do you think we should do to make you continue using reaper unix: ")
            my_file.write("\n")
            my_file.write("what to fix: ")
            my_file.write(b)
            c = input("do you think you will consider using reaper unix if we fix your problem: ")
            my_file.write("\n")
            my_file.write("do they want to use our software if we fix the problem: ")
            my_file.write(c)
            d = input("how much stars will you give us out of ten: ")
            my_file.write("\n")
            my_file.write("our software rating: ")
            my_file.write(d)
            e = input("your email address: ")
            my_file.write("\n")
            my_file.write("email address: ")
            my_file.write(e)



        delconf = input("type delete.acc to start the delete wizzard: ")
        if delconf == 'delete.acc':
            survey()
            dele()

        else:
            continue

        
