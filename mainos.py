from googlesearch import search
import random
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