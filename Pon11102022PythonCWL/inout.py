import os

#Excersise 1, module input/output
def hello_world():
    print("Hello world")

#Excersise 2, module input/output
def input_data():
    print("Input your name, surname, age in one line\n:")
    data = input()
    print(data)

#Excersise 3, module input/output
def encryptPasswd():
    passwd = input("Input code (only letters):")
    passwd.lower();
    for letter in passwd:
        if(ord(letter) < 120):
            passwd = passwd.replace(letter, chr(ord(letter)+3))
        else:
            passwd = passwd.replace(letter, chr(ord(letter) + 3 - 26))
    return passwd

def decodePasswd(passwd):
    for letter in passwd:
        if(ord(letter) < 100):
            passwd = passwd.replace(letter, chr(ord(letter)+3 + 26))
        else:
            passwd = passwd.replace(letter, chr(ord(letter) - 3 ))
    return passwd

def Lock():
    passwd = encryptPasswd()
    print(passwd)
    inputpasswd = input("Print passwd:")
    decoded_passwd = decodePasswd(passwd)
    if(inputpasswd == decoded_passwd):
        print("Correct")
    else:
        print("Incorrect")

#EX1
if __name__ == "__main__":
    # Hello World
    print("----------------------------------------------------------")
    print("Ex1.1, Hello world:")
    hello_world()

    # Data input
    print("----------------------------------------------------------")
    print("Ex1.2, Data input:")
    input_data()

    # Encrypting lock
    print("----------------------------------------------------------")
    print("Ex1.3, Encrypting lock:")
    Lock();