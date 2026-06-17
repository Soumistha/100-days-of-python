#add the cards shouldnt go over 21 if it goes it is a bust(lose) else highest sum wins
#if dealer and u score the same then its draw if the dealer gets less than 17 then draw another cards

#unlimited deck
#jack = king = queen = 10
#ace is 11 or 1 if the total sum is above 21
#comp is dealer

import random as r

def fix(hand):
    total = sum(hand)
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)
    return total

def blackjack():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    dealer =[]
    player =[]
    
    for i in range (0,2):
        d = r.randint(0,12)
        dealer.append(cards[d])
        
        p = r.randint(0,12)
        player.append(cards[p])
        
    dsum = fix(dealer) 
    psum = fix(player)

        
    print("your cards : ",player)
    
    while (dsum <17):
        d = r.randint(0,12)
        dealer.append(cards[d])
        dsum = fix(dealer)
    
    print("dealers first card : ",dealer[0])
    
    n = input("\ndo you want to deal another card?? (y/n) ")
    
    if (n == 'y'):
        p = r.randint(0,12)
        player.append(cards[p])
        psum = fix(player)
        print("your cards : ",player)
        
    #elif (n == 'n'):
    print("Game results!!!!!\n") 
    if psum > 21:
        print("BUSTED!!!!")
    elif dsum > 21:
        print("Dealer BUSTED!!! You win")
    elif psum == dsum:
        print("DRAWWW!!!")
    elif psum > dsum:
        print("You WONNN!!!!")
    else:
        print("BUSTED you lost")

        
    
def main():
    print("welcome to BLACKJACK!!!")
    
    blackjack()
    
    c = input("do you want to play again :")
    if(c =='y'):
        blackjack()
    else:
        print("Thank you !!!!!!")
        
main()