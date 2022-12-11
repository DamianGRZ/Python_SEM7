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

def main():
    Lock();

if __name__ == "__main__":
    main()