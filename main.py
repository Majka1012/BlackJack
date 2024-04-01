import random
import art
import os 


def add(tab):
    score=0 
    for i in tab:
        if i==11:
            if score>10:
                i=1
         
        score+=i
    
    return score    
   

def result(tab1,tab2):
    """Return False when computer wins and True when player won.
       Return none when it's draw"""
    
    score1=add(tab1)
    score2=add(tab2)
    
    if score1>21:
        return False
    if score1<=21 and score2>21:
        return True
    if score1==score2:
        return 
    if score1<=21 and score2<=21:
        if score1>score2:
            return True
        if score2>score1:
            return False
        
        
def winner(truefalse):
    if truefalse==True:
        print("WYGRAŁEŚ!!")
    if truefalse==False:
        print("PRZEGRAŁEŚ :/")
    if truefalse==None:
        print("REMIS")
    




deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
again=True
while again:
    
    print(art.logo)
    print("Welcome to BlackJack.")

    cards=[deck[random.randint(0,len(deck)-1)],deck[random.randint(0,len(deck)-1)]]

    print(f"Your cards: {cards}. Sum: {add(cards)}")

    computer=[deck[random.randint(0,len(deck)-1)]]

    print(f"Computer's first card: {computer}. Sum: {add(computer)}")

    another=input("Type 'y' to get another card, type 'n' to pass: ")
    end=False
    while end==False:
        if another=="n":
            computer.append(deck[random.randint(0,len(deck)-1)])
            
            while add(computer)<17  and add(computer)<=21:
                computer.append(deck[random.randint(0,len(deck)-1)])
                
            print(f"Computer's cards: {computer}. Sum: {add(computer)}")
            winner(result(cards,computer))
            end=True
        if another=="y":
            cards.append(deck[random.randint(0,len(deck)-1)])
            print(f"Your cards: {cards}. Sum: {add(cards)}")
            if add(cards)>21:
                print("PRZEGRAŁES :/")
                break
            another=input("Type 'y' to get another card, type 'n' to pass:  ")
            
    again=input("Do you want to try again? y/n  ")
    if again=="y":
        again=True
        os.system('cls||clear')
    else:
        again=False
        os.system('cls||clear')
    
            