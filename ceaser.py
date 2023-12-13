print("WELCOME TO THE CEASER CIPHER")

# print(type(message))
# print(message)
alpphabets=['a','b','c','d','e','f','g','h','i','j','k','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encode():
    message = input("enter the message you need to send\n").lower()
    message = str(message)
    num=0
    num=str(num)
    shifting= int(input("enter the number by which the message needs to be done with respect to \n"))
    encoded = ""
    for char in message:
        num=alpphabets.index(char)
        result=(alpphabets[num+shifting])
        encoded +=result
    print(f"your encoded message is \n {encoded}")

def decode():
    re_shifting=input("enter the message to be decoded\n")
    re_shifting_num=int(input("enter the shifting number\n"))
    decoded = ""
    for char in re_shifting:
        num1= alpphabets.index(char)
        result = (alpphabets[num1 - re_shifting_num])
        decoded += result
    print(f"your decoded message is {decoded}")

option=int(input('''enter wether you want to encode a message oor decode a prior encoded message
to encode press 1 and to decode press 2\n'''))
if option==1:
    encode()
elif option==2:
    decode()