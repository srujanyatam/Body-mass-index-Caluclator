import random
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+"
while 1:
    password_len=int(input("enter the length of the password"))
    password_count=int(input("how many passwords u want "))
    for x in range(0,password_count):
        password =" "
        for x in range(0,password_len):
            password_char=random.choice(chars)
            password=password_char+password
            print("Here is your password:", password)


