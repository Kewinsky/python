# Password generator
# Write a programme, which generates a random password for the user. Ask the user how long they want their password to be,
# and how many letters and numbers they want in their password. Have a mix of upper and lowercase letters,
# as well as numbers and symbols. The password should be a minimum of 6 characters long.

import random
import string
import os

# Baza stringow z ktorych losujemy litery i cyfry
# print(random.choice(string.ascii_letters))
# print(random.randint(0, 9))
haslo = ""
length = 0
letters = 0
numbers = 0



def random_pass():
    global haslo, length, letters
    haslo = ""
    try:
        length = int(input("How long should have your password? ( minimum 6 ) "))
        if length < 6:
            print("Enter at least '6'.")
            random_pass()
        letters = int(input("How many letters? "))

    except ValueError:
        print("Error: Must be integer !")
        random_pass()

    numbers = length - letters

    for i in range(0, letters, 1):
        haslo += random.choice(string.ascii_letters)

    for i in range(0, numbers, 1):
        haslo += str(random.randint(0, 9))

    haslo_conv = list(haslo)
    random.shuffle(haslo_conv)
    result = ''.join(haslo_conv)
    print(result)

    hasloOK = input("Password good? ( yes / no ) ")
    haslo_low = hasloOK.lower()
    if haslo_low == "no":
        random_pass()

    else:
        site = input("What site ? ")
        login = input("Enter login: ")
        fileName = ("Password_saver") + ".txt"
        myFile = open(fileName, 'a+')
        myFile.write("--------------------------")
        myFile.write("\n")
        myFile.write(site)
        myFile.write("\n")
        myFile.write(login)
        myFile.write("\n")
        myFile.write(result)
        myFile.write("\n")
        myFile.write("--------------------------")
        myFile.write("\n")
        myFile.write("||||||||||||||||||||||||||")
        myFile.write("\n")
        myFile.close()
        os.startfile(fileName)


random_pass()