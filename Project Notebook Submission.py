#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random #The program will have to randomly choose between rock, paper, scissors.

print ("Rock, Paper, Scissors game!") #Title of the game

while True:
    hand = input("Enter rock, paper, or scissors (press enter to quit): ") #Your turn to choose one of the three options.
    cpuHand = random.randint(1, 3) #Randomly chooses either 1(rock), 2(paper), or 3(scissors).
    if (hand == "rock"):
        print (hand) #To show you chose rock.
        if cpuHand == 2: #Paper beats rock.
            print ("paper")
            print ("You've lost!")
            break #Game stops.
        elif cpuHand == 3: #Rock beats scissors.
            print ("scissors")
            print ("You've won!")
            break #Game stops.
        else: #It's a tie between rock and rock, so the game still continues.
            print (hand)
            print ("It's a tie!")
    elif hand == "paper":
        print (hand) #To show you chose paper.
        if cpuHand == 3: #Scissors beat paper.
            print ("scissors")
            print ("You've lost!")
            break #Game stops.
        elif cpuHand == 1: #Paper beats rock.
            print ("rock")
            print ("You've won!")
            break #Game stops.
        else: #It's a tie between paper and paper, so the game still continues.
            print (hand)
            print ("It's a tie!")
    elif hand == "scissors":
        print (hand) #To show you chose scissors.
        if cpuHand == 1: #Rock beats scissors.
            print ("rock")
            print ("You've lost!")
            break #Game stops.
        elif cpuHand == 2: #Scissors beat paper.
            print ("paper")
            print ("You've won!")
            break #Game stops.
        else: #It's a tie between scissors and scissors, so the game still continues.
            print (hand)
            print ("It's a tie!")
    elif hand == "": #Press enter to quit.
        break #Quits the game.
    else: #If you don't type "rock," "paper," or "scissors."
        print ("Please enter the word correctly!")


# In[ ]:





# In[ ]:





# In[9]:


import random #For generating a new random password.

oldPassword = input("Enter your old password: ") #Enter old password
newPassword = "" #Where new password will be stored.
randomDistance = random.randint(1, 10) #Randomly choose a distance value for each character's ASCII numeric code.

for character in oldPassword:
    ordValue = ord(character) #Converts each character in the password to its ASCII numeric code.
    newOrdValue = ordValue + randomDistance #Random distance added to ASCII numeric code gives new ASCII numeric code for each character.
    newPassword = newPassword + chr(newOrdValue) #New ASCII numeric code is converted back to characters and creates the new password.
print("Here is your new password: " + newPassword) #New password is created.


# In[ ]:





# In[ ]:





# In[12]:


firstSide = int(input("Enter the first side: ")) #Value for first side of the triangle.
secondSide = int(input("Enter the second side: ")) #Value for second side of the triangle.
thirdSide = int(input("Enter the third side : ")) #Value for third side of the triangle.

if firstSide == secondSide and secondSide == thirdSide: #If all sides are equal, then it's equilateral.
    print ("The triangle is equilateral.")
else: #Otherwise, it not equilateral.
    print ("The triangle is not equilateral.")


# In[ ]:





# In[ ]:





# In[11]:


message = input("Enter the coded text: ") #Enter a coded text that uses a Caesar cipher to decrypt.
distanceValue = int(input("Enter the distance value: ")) #Give the distance value that will decrypt the message
code = "" #The decrypted code.
negativeDistance = -(distanceValue) #Distance value is now negative which will count backwards to reveal the message.

for ch in message:
    ordValue = ord(ch) #Converts each character in the message to its ASCII numeric code.
    cipherValue = ordValue + negativeDistance #Counts the ASCII numeric code with the negative distance value.
    code = code + chr(cipherValue) #ASCII code of the cipherValue is converted back to characters to reveal the message.
print(code) #Gives the decrypted message.


# In[ ]:





# In[ ]:





# In[12]:


import random #For the program to randomly guess your number.

smaller = int(input("Enter the smaller number: ")) #Provide smaller number.
larger = int(input("Enter the larger number: ")) #Provide larger number.

count = 0 #The game start out with 0 tries.

while True:
    count += 1 #Keeps track of the number of tries.
    myNumber = random.randint(smaller, larger) #Guesses the number between the smaller and larger number.
    print (str(smaller) + ", " + str(larger)) #Show what the numbers are in each try.
    print("Your number is " + str(myNumber)) #Program randomly guesses the number between smaller and larger number.
    choice = input('Enter =, <, or >: ') #Confirm if the program got the number.
    if choice == '=': #If the program guessed correctly.
        print("Hooray, I've got it in " + str(count) + " tries")
        break #Game stops
    elif smaller == larger: #If smaller number is equal to the larger number after a certain number of tries.
        print("I'm out of guesses, and you cheated!")
        break #Game stops
    elif choice == '<': #If the guessed number is less than the actual number.
        larger = myNumber - 1
    else: #If the guessed number is greater than the actual number.
        smaller = myNumber + 1


# In[ ]:





# In[ ]:





# In[14]:


def identifyPrime(number): #Define a function that identifies whether a given number is a prime number.
    import math #To use math.sqrt.
    if number > 1: #For all number above 1.
        m = int(math.sqrt(number)) #Square root of number is truncated by int and used for the range function.
        for i in range(2, m + 1): #Checks if number is divisible by numbers in a range of 2 and the square root.
            if (number % i) == 0: #If its divisible by any of those numbers in the range, then it's not prime.
                return False
        else: #If it's not divisible of any of those numbers in the range, then it is a prime.
            return True
    else: #If the number is 1, then it's not prime.
        return False

number = int(input("Enter the number: ")) #Provide any number.
print (number)
print (identifyPrime(number)) #Checks if the number is prime(True) or not(False).


# In[ ]:




