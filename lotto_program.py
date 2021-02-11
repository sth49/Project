#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from pathlib import Path
import random
import calendar
import datetime
import pickle
from glob import glob


# In[2]:


Lotto_List = []

def menu():
    print('='*15,'Menu','='*15)
    print('1. Creation             (C)')
    print('2. Display the Set      (D)')
    print('3. Save to file         (S)')
    print('4. Check the Result     (R)')
    print('5. Exit the Program     (Q)')
    print('='*36)
    
def creation():
    global Lotto_List
    game = int(input("Enter how many games you will buy : "))
    auto=game+1
    while(auto>game):
        
        auto  = int(input("Enter how many games you want to create automatically : "))
        if auto>game:
            print("Please input the correct number.")
    
        
    for i in range(auto):
        
        AutoNum = sorted(random.sample(range(1,45),6))
        AutoNum.insert(0,'a')
        Lotto_List.append(AutoNum)
    if game-auto > 0:
        print("\n")
        print("="*20)
        print("Input ex)7 15 4 2 43 28")
        print("Input ex)7,15,4,2,43,28")
        print("="*20)
        i=0
        for i in range(game-auto):
            lotto = False
            while lotto == False:
                user_input = input("Enter your number : ")
                try: user = sorted(int(x) for x in user_input.split(','))
                except: user = sorted(int(x) for x in user_input.split())
                length1 = len(user)
                length2 = len(list(set(user)))
                user.insert(0,'m')

                if length2 == 6:
                    Lotto_List.append(user)
                    lotto = True
                elif length1 > length2:
                    print('There are duplicate numbers.')
                else:
                    print('You have to choose six numbers.')
    #print(Lotto_List)
        
            
def display():
    print('='*15+"NumberSet"+'='*15)
    for i in Lotto_List:
        r = ""
        for j in range(1,7):
            r +=(lambda x: '  '+x if len(x)==1 else ' '+x)(str(i[j]))
        if i[0]=='a':
            print("a ::",r)
        elif i[0]=='m':
            print('m ::',r)


def save():
    print('\nsaveFile() :: Date save complete....\n')
    now1 = datetime.datetime.now()
    name = str(now1.year)+(lambda x: '0'+x if len(x)==1 else x)(str(now1.month))+(lambda x: '0'+x if len(x)==1 else x)(str(now1.day))+'-'+(lambda x: '0'+x if len(x)==1 else x)(str(now1.hour))+(lambda x: '0'+x if len(x)==1 else x)(str(now1.minute))
    
    global Lotto_List
    f = open(name+'.pkl','wb')
    
    pickle.dump(Lotto_List, f)
        
    f.close()
    Lotto_List = []

def result():
    win = {0: ' 7', 1: ' 6', 2: ' 5', 3: '*4', 4: '*3', 5: '*2', 6: '*1'}
    
    print('\n')
    print("="*20)
    print("Date ex)2018/09/15")
    print("Date ex)2018 09 15")
    print("="*20)

    is_saturday = 0
    while is_saturday !=5:
        user_input1 = input("Enter date : ")
        try: day = [int(x) for x in user_input1.split()]
        except: day = [int(x) for x in user_input1.split(',')]

        is_saturday = datetime.date(day[0], day[1], day[2]).weekday()
        if is_saturday != 5:
            print("Write the date again.")

    lotto_day = datetime.datetime(day[0],day[1],day[2],22,0,0)
    days = []
    for i in range(7):
        days.append(lotto_day - datetime.timedelta(days=6-i))
    results = []
    for j in days:
        name = str(j.year)+(lambda x: '0'+x if len(x)==1 else x)(str(j.month))+(lambda x: '0'+x if len(x)==1 else x)(str(j.day))

        for file in glob(name+"*.pkl"):
            f = open(file, 'rb')
            d = pickle.load(f)
            results += d
            f.close()
    print('\n')
    print("="*20)
    print("List ex)7 15 4 2 43 28")
    print("List ex)7,15,4,2,43,28")
    print("="*20)


    lotto = False
    while lotto == False:
        user_input2 = input("Enter list : ")
        try: lotto_num = sorted(int(x) for x in user_input2.split(','))
        except: lotto_num = sorted(int(x) for x in user_input2.split())
        length1 = len(lotto_num)
        length2 = len(list(set(lotto_num)))

        if length2 == 6:
            lotto = True
        elif length1 > length2:
            print('There are duplicate numbers. Please enter the list again.')
        else:
            print('You have to choose six numbers. Please enter the list again.')

    print("="*25+"Game Result"+"="*25)
    print("|  index     type          number            match    rank   |")
    i=0
    for game in results:
        match=0
        i += 1
        for k in lotto_num:
            if k in game:
                match += 1
        r = ""
        for j in range(1,7):
            r +=(lambda x: '  '+x if len(x)==1 else ' '+x)(str(game[j]))

        print("|Game   ",i," : ",game[0],"    ",r,"     ",match,"     ",win[match],"   |")
    print("="*62)

    


# In[3]:


p = Path('LotteryProgram')
try:
    p.mkdir()
    q = Path('LotteryProgram\\data')
    try:
        q.mkdir()
    except FileExistsError as e2:
        print(e2)
except FileExistsError as e:
    print(e)
os.chdir('LotteryProgram\\data')


# In[4]:


option = ''
while option != '5'and option != 'Q' and option !='q':
    menu()
    option=input('Select Menu : ')
    
    if option == '1' or option == 'c' or option == 'C':
        creation()
    
    elif option == '2' or option == 'd' or option == 'D':
        if Lotto_List == []:
            print('Please create the lotto numbers.')
        else:
            display()
    
    elif option == '3' or option == 's' or option == 'S':
        if Lotto_List == []:
            print('Please create the lotto numbers.')
        else:
            save()
    
    elif option == '4' or option == 'r' or option == 'R':
        result()
    
    elif option == '5' or option == 'q' or option == 'Q':
        continue
    
    else:
        print('\nPlease input the correct option\n')

print("Exit the Program")
