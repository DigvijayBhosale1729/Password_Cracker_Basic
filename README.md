# Password_Cracker_Basic
A simple command line python script to bruteforce passwords
Syntax
python passCracker.py <argument1> <argument2> <dictionary file>
argument1 
  -h for hashed and salted password
  -p for password in plaintext
argument2
  hashed and salted password when argument1 is -h
  plaintext password when argument1 is -p
  
Disclaimer - The -h option only works for passwords that have been hashed using the python crypt
