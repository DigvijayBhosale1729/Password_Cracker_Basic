## Made by FoxSinOfGreed1729

import crypt
import sys
def passTest1(password):
    salt=password[0:2]
    #the password salt is the first two charachters and string[x:y] is syntax of substring from x(inclusive) to but not inclusive of y
    dictfile=open(sys.argv[3],'r')
    #reads the dictionary file
    for word in dictfile:
        word=word.strip('\n')
        #strips the line of all spaces
        cryptword=crypt.crypt(word,salt)
        if cryptword==password:
            print("Password is -->   ",word)
            exit()
    print("Password Not Found")
    exit()
def passTest2(password):
    dictfile=open(sys.argv[3],'r')
    #reads dictionary file
    for word in dictfile:
        word=word.strip('\n')
        if word == password:
            print("Password is -->   ",word)
            exit()
    print("Password Not Found")
    exit()

if len(sys.argv)<2:
    print("Syntax is <argument1> <argument2> <passwords.txt>")
    print("Argument1 is -h for passing hash ")
    print("Argument1 is -p for plaintext")
    print("Argument2 is the password or Hash depending upon what argument 1 is ")
    exit()
password=sys.argv[2]
if sys.argv[1]=='-p':
    passTest2(password)
if sys.argv[1]=='-h':
    passTest1(password)
