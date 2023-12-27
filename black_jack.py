import random
def if_21():
# this function is called if your score exceeds 21
        print("You Loose")
        print(f"your final hand is  {your_empty_list} and your final score is {your_score} ")
        print(f"computer's final hand is: {computer_empty_list} and computer's final score is {computer_score}")

def choices():
    global your_score
    global computer_score

    if 11 in your_empty_list and your_score>21:
        your_empty_list.remove(11)
        your_empty_list.append(1)

    flag=False
    while not flag:
        choice = input("Type 'y' to get another card, type 'n' to pass:\n")
        if 11 in your_empty_list and your_score > 21:
            your_empty_list.remove(11)
            your_empty_list.append(1)

        if choice=='y':

            your_next_hand=random.sample(cards,1)
            computer_next_hand = random.sample(cards, 1)
            your_empty_list.extend(your_next_hand)
            computer_empty_list.extend(computer_next_hand)
            computer_score = sum(computer_empty_list)
            your_score = sum(your_empty_list)
            if 11 in your_empty_list and your_score > 21:
                your_empty_list.remove(11)
                your_empty_list.append(1)
            print(f"your cards are {your_empty_list} and your current score is {your_score} ")
            print(f"the computers first card is: {computer_empty_list[0]}")
            if your_score > 21:
                if_21()
        elif choice=='n'and your_score>computer_score and your_score<=21:
            print('YOU WIN')
            if_black_jack()
            flag = True
        elif choice=='n' and your_score<computer_score and computer_score<=21:
            print("YOU LOOSE")
            if_black_jack()
            flag=True



def if_black_jack():
    print(f"your final hand is  {your_empty_list} and your final score is {your_score} ")
    print(f"computer's final hand is: {computer_empty_list} and computer's final score is {computer_score}")


start=input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n")
computer_score=0
your_score=0
computer_empty_list=[]
your_empty_list=[]
cards=[11,2,3,4,5,6,7,9,10,10,10,10]
if start=='y':
    print('''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
      |  \/ K|                            _/ |                
      `------'                           |__/         ''')
else:
    exit()

# giving first two cards
your_first_hand=random.sample(cards,2)
computer_first_hand=random.sample(cards,2)
your_empty_list.extend(your_first_hand)
computer_empty_list.extend(computer_first_hand)
computer_score = sum(computer_empty_list)
your_score=sum(your_empty_list)

print(f"your cards are {your_empty_list} and your current score is {your_score} ")
print(f"the computers first card is: {computer_empty_list[0]}")

if your_score==21 and computer_score==21:
    print("draw")
    if_black_jack()

if your_score==21:
    print("BLACKJACK You Win")
    if_black_jack()

if computer_score==21:
    print(" COMPUTER'S BLACKJACK you loose")
    if_black_jack()

if your_score>21:
    if_21()

else:
    choices()










