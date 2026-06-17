# print("hello world")
# print("hello\ni am soumistha")
# print("learning"+" "+"python")
# remember to call in command prompt saying python trail.py

#inputs
#print("hello " + input("what is your name? "))

# variables
# name = input("what is your name ")
# print(name)
# length = len(name)#not really a good practise but for now ok
# print(length)

#------------------------------------------------------------------------------------

#calc project
# print("Welcome to the tip calculator!")
# price =float( input("What was the total bill? "))
# tip = float(input("How much do u want to tip "))
# ppl = int(input("how many ppl to split: "))
# total = price + (price*(tip/100))
# share = total/ppl
# print(f"each person pays: {round(share,2)}")

#------------------------------------------------------------------------------------

#if-else statements
# height = int(input("what is your height??? "))
# if height>=120:
    # print("welcome")
    # age = int(input("what is your age "))
    # if(age<=12):
        # print("pay $7")
    # elif (age<18):
        # print("pay $10")
    # else:
        # print("pay $12")
# else:
    # print("not allowed")

#------------------------------------------------------------------------------------

#modulo operator

# no = int(input("number : "))
# if (no%2 == 0):
    # print("even")
# else:
    # print("odd")

#------------------------------------------------------------------------------------

#Pizza program

# print("welcome to the pizza house")
# size = input("what size ? 'S','M','L':")

# total =0
# if (size == "S"):
    # total += 15
# elif (size == "M"):
    # total += 20
# else:
    # total += 25
    
# pepperoni = input("Do you want extra pepperoni? 'N','Y':")

# if (pepperoni == "Y"):
    # total += 2
# else:
    # total += 0
 
# cheese = input("Do you want extra cheese? 'N','Y':")

 
# if (cheese == "Y"):
    # total += 1
# else:
    # total += 0

# print(f"your final bill is ${total}")

#------------------------------------------------------------------------------------

# treasure island

# print("welcome to this island. \nTo escape u need to find the treasure \nALL THE BEST!!!!")
# dire = input("left or right: ")

# if(dire == "left"):
    # swim = input("swim or wait: ")
    # if(swim == "wait"):
        # door = input("which door (red,blue,yellow): ")
        # if(door == "yellow"):
            # print("yeaa you wonn!!")
        # elif(door == "red"):
            # print("Game Over.")
        # elif(door == "blue"):
            # print("Game Over.")
        # else:
            # print("invalid input")
    # elif(swim == "swim"):
            # print("Game Over.")
    # else:
        # print("invalid input")
# elif(dire == "right"):
    # print("Game Over.")
# else:
    # print("invalid input")

#------------------------------------------------------------------------------------

#randomization

import random as r 

# print(r.randint(1,10))
# print(r.random())#generates a number b/w 0 and 1
# print(r.uniform(1,10))#generates a float number b/w 1 and 10

#------------------------------------------------------------------------------------

#lists

#indexing starts from 0
#-1 is the last item in the list
# append will add in the last of the list

# lil = ["hello","bye"]
# print(lil)
# lil.append("hi")
# print(lil)

#who will pay

# friends = ["alice","sara","hay","zade","sahil","nilla"]
# ran = r.randint(0,5)
# print(f"{friends[ran]} will pay the bill")

#ROCK PAPER SCISSORS
# options = ["ROCK","PAPER","SCISSORS"]
# user = int(input("what do you choose? 0 for rock , 1 for paper and 2 for scissors "))
# ran = r.randint(0,2)
# print(ran)
# if user == ran:
    # print("draw")
# elif user+1==ran:
    # print("i wonnn")
# elif ran+1 == user:
    # print(":( you won")
# elif user == 0 and ran == 2:
    # print(":( you won")
# elif ran == 0 and user == 2:
    # print("i wonnn")
# else:
    # print("invalid") 
    
#------------------------------------------------------------------------------------

#for loops

# score = [123,234,345,765,235,87,23,67,5372,876,7182,6543,987654,4376,2947]
# m =0
# for i in score:
    # if(i>m):
        # m = i

# print(m)
# print(max(score))

# s =0 
# for i in range(1,101):
    # s +=i
# print(s)
# in range funct it goes to start to last-1

# PASSWORD GENERATOR
# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           # 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           # 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           # 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Number of letters, symbols, and numbers to include
# nr_letters = 4
# nr_symbols = 2
# nr_numbers = 2

# Hard level password generation
# password_list = []

# for char in range(0, nr_letters):
    # password_list.append(random.choice(letters))

# for char in range(0, nr_symbols):
    # password_list.append(random.choice(symbols))

# for char in range(0, nr_numbers):
    # password_list.append(random.choice(numbers))

# print("Before shuffling:", password_list)

# random.shuffle(password_list)

# print("After shuffling:", password_list)

# password = ""
# for char in password_list:
    # password += char

# print(f"Your password is: {password}")

#------------------------------------------------------------------------------------

#creating function

# def func():
    # print("hello");
    # print("testing");

# func()

#love calc

# def calculate_love_score(name1,name2):
    
    # name1 = name1.lower()
    # name2 = name2.lower()
    # names = name1 + name2
    # t = names.count('t')
    # r = names.count('r')
    # u = names.count('u')
    # e = names.count('e')
    # true= t + r + u + e
    
    # l = names.count('l')
    # o = names.count('o')
    # v = names.count('v')
    # love = l + o + v + e
    
    # print(f'{true}{love}')
    
# name1 = input("enter first name: ")
# name2 = input("enter sec name: ")
    
# score = calculate_love_score(name1,name2)
# print(score)

#------------------------------------------------------------------------------------

#caesar cipher

# alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# def encrypt(text,n):
    # encrypted = ""
    # for i in text:
        # shifted = alphabets.index(i)+n
        # shifted %= len(alphabets)
        # encrypted += alphabets[shifted]
    # print(encrypted)

        
# def decrypt(text,n):
    # encrypted = ""
    # for i in text:
        # shifted = alphabets.index(i)- n
        # shifted %= len(alphabets)
        # encrypted += alphabets[shifted]
    # print(encrypted)

# choose = input("what do u want do? ")

# if choose == 'encrypt':
    # text = input("write the msg: ").lower().replace(" ","")
    # n = int(input("write the number of shifts: "))
    # encrypt(text,n)
# elif choose == 'decrypt':
    # text = input("write the msg: ").lower().replace(" ","")
    # n = int(input("write the number of shifts: "))
    # decrypt(text,n)
# else:
    # print("wrong choice")    


#------------------------------------------------------------------------------------

#dictionary

# student_scores = {
    # "Harry": 81,
    # "Ron": 78,
    # "Hermione": 99, 
    # "Draco": 74,
    # "Neville": 62,
# }

# student_grades = {}


# for student in student_scores:
    # score = student_scores[student]
    # if score > 90:
        # student_grades[student] = "Outstanding"
    # elif score > 80:
        # student_grades[student] = "Exceeds Expectations"
    # elif score > 70:
        # student_grades[student] = "Acceptable"
    # else:
        # student_grades[student] = "Fail"


# print(student_grades)

#nesting

# student = {
    # "Harry": 81,
    # "Ron": 78,
    # "Hermione": [67,98,46],
    # "Draco": 74,
    # "Neville": 62,
# }

# print(student["Hermione"][1])

# secret bidding

##without clearing
# bids = {}
# cont = True

# while cont:
    # name = input("What's the name: ")
    # b = int(input("Enter the bid: "))
    # bids[name] = b
    # c = input("Do you want to continue (y/n): ").lower()
    
    # if c == 'n':
        # cont = False

        # highest_bidder = max(bids, key=bids.get)
        # print(f"The highest bidder is {highest_bidder} with a bid of ₹{bids[highest_bidder]}")

##with the clearing of the screen
# import os

# bids = {}
# cont = True

# def clear_screen():
    # os.system('cls' if os.name == 'nt' else 'clear')

# while cont:
    # name = input("What's the name: ")
    # b = int(input("Enter the bid: ₹"))
    # bids[name] = b

    # c = input("Do you want to continue? (y/n): ").lower()
    # if c == 'n':
        # cont = False
        # clear_screen()
        # highest_bidder = max(bids, key=bids.get)
        # print(f"The highest bidder is {highest_bidder} with a bid of ₹{bids[highest_bidder]}")
    # else:
        # clear_screen()


#------------------------------------------------------------------------------------

# #calculator
# def calc(a,b,o):
    # if o == '+':
        # return a+b
    # elif o == '-':
        # return a-b
    # elif o == '*':
        # return a*b    
    # elif o == '/':
        # return a/b

# n1 = int(input("what is the first number: "))
# def input_num(n1):
    
    # print("+\n-\n*\n/")
    # o = input("pick an operation:")
    # n2 = int(input("what is the second number: "))
    # return calc(n1,n2,o)
# ans = input_num(n1)
# print(ans)
# cont = input(f"do you wanna continue with {ans}(c) or start a new calc(n) or exit(e) :")
# while cont !="e":
    # if cont == "c":
        # input_num(ans)
    # elif cont == "n":
        # n1 = int(input("what is the first number: "))
        # ans = input_num(n1)
        # print(ans)
    
    
# def calc(a, b, o):
    # if o == '+':
        # return a + b
    # elif o == '-':
        # return a - b
    # elif o == '*':
        # return a * b    
    # elif o == '/':
        # return a / b
    # else:
        # return "Invalid operator"

# def input_num(n1):
    # print("+\n-\n*\n/")
    # o = input("Pick an operation: ")
    # n2 = int(input("What is the next number: "))
    # return calc(n1, n2, o)

# # Initial calculation
# n1 = int(input("What is the first number: "))
# ans = input_num(n1)
# print(f"Result: {ans}")

# # Loop for continuation
# while True:
    # cont = input(f"\nDo you want to continue with {ans} (c), start new (n), or exit (e)? ").lower()
    
    # if cont == 'c':
        # ans = input_num(ans)
        # print(f"Result: {ans}")
    # elif cont == 'n':
        # n1 = int(input("What is the first number: "))
        # ans = input_num(n1)
        # print(f"Result: {ans}")
    # elif cont == 'e':
        # print("Goodbye!")
        # break
    # else:
        # print("Invalid choice. Please enter 'c', 'n', or 'e'.")




#title case
# name = 'soumistha bhuyan'

# print(name)
# print(name.title())

#leap year
# def is_leap_year(year):
    # if year % 4 == 0:
        # if year % 100 == 0:
            # if year % 400 == 0:
                # return True
            # else:
                # return False
        # else:
            # return True
    # else:
        # return False
# docstring or multiline comment or string

