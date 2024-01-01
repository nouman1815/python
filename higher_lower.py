from data_for_higher_lower import data
from art_for_higher_lower import logo,vs


from replit2 import db,clear
import random
A={}
B={}

score = 0


def compare():
    answer = input("WHO HAS MORE FOLLOWERS? A or B :").upper()
    global score, a, b, A, B, flag

    correct_answer = max(a, b)

    if answer == 'A' and correct_answer == a or answer == 'B' and correct_answer == b:
        score += 1
        print(f"your current score is :{score}")
        flag = False

    else:
        print(f"Your final score is : {score}")
        flag = True

    A = B
    B = random.choice(data)


def second():
    global a,b,A,B
    # print(logo)
   
    a = (A['follower_count'])
    a= int(a)
    print("\nNEXT COMPARISON\n")
    print(f"Compare A : {A['name']} a {A['description']} from {A['country']}")
    print(vs)

    
    b = (B['follower_count'])
    b= int(b)
    print(f"Against B:{B['name']} a {B['description']} from {B['country']}")
    compare()

    return a,b,A,B


print(logo)

A= random.choice(data)
a = (A['follower_count'])
a= int(a)
print(f"Compare A : {A['name']} a {A['description']} from {A['country']}")
print(vs)

B = random.choice(data)
b = (B['follower_count'])
b= int(b)
print(f"Against B:{B['name']} a {B['description']} from {B['country']}")
if A==B:
    B = random.choice(data)



flag=True
compare()




while not flag:
    second()





