import re
import random
import string

# max limit of password
length_of_pass = 100
copy_length_of_pass = length_of_pass

# the four variables below are the components/characters to make up ascii _____
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = "0123456789"
special = "!#$%&’()*+,-./:;<=>?[|]{}^~@_"
# variable that any of the chosen components (variables) above will be added to
new_pass_count=0
ascii_text = ""
new_pass=""
counter=0
# will determine which components/character groups of ascii will be in the password
def components():
    global counter
    global copy_length_of_pass
    def lower_def():
        global ascii_text
        global length_of_pass
        global counter
        try:
            lower_answer = int(input("\nHow many lower case letters you want? "))
            counter=counter+lower_answer
            print(counter)
        except ValueError:
            print("Please enter only Positive numbers")
            lower_def()
        if (lower_answer > 0 and lower_answer <= length_of_pass ) :
            length_of_pass=length_of_pass - lower_answer
            lowercases= ''.join(random.choice(lowercase) for i in range(lower_answer))
            ascii_text += lowercases
            #code required for the codition if length_of_pass=0
        elif (lower_answer == 0):
            None
        else: # if yes or no is not given, re-ask the question
            print("Please enter the value which is less than the given password length ")
            lower_def()
    if(counter<copy_length_of_pass):
    	lower_def()

    def upper_def():
        global ascii_text
        global length_of_pass
        global counter
        try:
            upper_answer = int(input("\nHow many uppercase case letters you want? "))
            counter=counter+upper_answer
        except:
            print("Please enter only Positive numbers")
            upper_def()
        if (upper_answer > 0 and upper_answer <= length_of_pass ) :
            length_of_pass=length_of_pass - new_pass_count
            uppercases = ''.join(random.choice(uppercase) for i in range(upper_answer))
            ascii_text += uppercases
            #code required for the codition if length_of_pass=0
        elif (upper_answer == 0):
            None
        else:
            print("Please enter the value which is less than the given password length ")
            upper_def()
    if(counter<copy_length_of_pass):
    	upper_def()
    
    def special_def():
        global ascii_text
        global length_of_pass
        global counter
        try:
            special_answer = int(input("\nHow many special charector you want? "))
            counter=counter+special_answer
        except:
            print("Please enter only Positive numbers")
            special_def()
        if (special_answer > 0 and special_answer <= length_of_pass ) :
            length_of_pass=length_of_pass - special_answer
            specials = ''.join(random.choice(special) for i in range(special_answer))
            ascii_text += specials
            #code required for the codition if length_of_pass=0
        elif (special_answer == 0):
            None
        else:
            print("Please enter the value which is less than the given password length ")
            special_def()
    if(counter<copy_length_of_pass):
    	special_def()
    
    def number_def():
        global ascii_text
        global length_of_pass
        global counter
        try:
            numbers_answer = int(input("\nHow many numbers charector you want? "))
            counter=counter+numbers_answer
        except:
            print("Please enter only Positive numbers")
            number_def()
        if (numbers_answer > 0 and numbers_answer <= length_of_pass ) :
            length_of_pass=length_of_pass - numbers_answer
            numberss = ''.join(random.choice(numbers) for i in range(numbers_answer))
            ascii_text += numberss
            #code required for the codition if length_of_pass=0
        elif (numbers_answer == 0):
            None
        else:
            print("Please enter the value which is less than the given password length ")
            number_def()
    if(counter<copy_length_of_pass):
    	number_def()

code_generate=components()

def password_generator(pass_length):
    #password = ''.join(random.choice(ascii_text) for i in range(pass_length))
    #print(ascii_text)
    # make something to make sure characters wanted are in password
    #for i in true:
        #if i p
    password=list(ascii_text)
    random.shuffle(password)
    print("\nPassword: \n" + "".join(password))
    del password
    diff_pass = input("\nNew password?\n").upper()
    if diff_pass == "YES" or diff_pass == "Y":
        print("\n")
        password_generator(length_of_pass)

password_generator(copy_length_of_pass)

