#BlackJack

import random
import time
def print_hand():
    print(f"Your hand: {player_hand}", end="      ")
    time.sleep(1)
    print(f"Dealer hand: {dealer_hand}")

def calculate_sum(list):
    sum = 0
    for card in list:
        sum += card
    
    for check in list:
         if check == 11 and sum > 21:
              sum = sum -10
    return sum

def check_Winning(player_hand,dealer_hand,player_score,dealer_score ):
            if 21 > calculate_sum(player_hand) > calculate_sum(dealer_hand) or calculate_sum(dealer_hand) > 21:
                player_score += 1
                print("You WON!!!")
                
            elif calculate_sum(player_hand) == 21 and calculate_sum(dealer_hand) is not 21:
                player_score += 1
                print("You WON!!!")
            
            elif calculate_sum(player_hand) < calculate_sum(dealer_hand) and calculate_sum(dealer_hand) < 21: 
                dealer_score += 1
                print("Dealer WON")
            
            elif calculate_sum(dealer_hand) == 21 and calculate_sum(player_hand) is not 21:
                 dealer_score += 1
                 print("Dealer WON")
            
            elif calculate_sum(player_hand) == calculate_sum(dealer_hand):
                 print("Its A TIE...")

            return player_score, dealer_score

def final_battle(dealer_hand, player_score, dealer_score):
    while calculate_sum(dealer_hand) < 16 and calculate_sum(dealer_hand) <= calculate_sum(player_hand):
        dealer_hand.append(random.choice(deck))
        print_hand()
    
    return check_Winning(player_hand, dealer_hand,player_score, dealer_score)
        

print("----------Welcome To BlackJack Game----------")
print("")



deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4 # 4 סדרות
# 11 לאס, 10 לנסיך, מלכה, מלך
player_score = 0 
dealer_score = 0
player_hand = []
dealer_hand = []
dealer_sum = 0
player_sum  = 0
# תחילת המשחק
while True:
    start_stop = input("Prass enter to start :), press Q to stop playing: ").lower()


    if start_stop == "q":
         print(f"Player score {player_score} Dealer score {dealer_score}")
         break
    
 # קבלת קלפים בפעם הראשונה

    player_hand.append(random.choice(deck)) 
    player_hand.append(random.choice(deck)) 
    dealer_hand.append(random.choice(deck))
    print_hand()

    # שלב הבחירה

    choice = input("Stay or 1 more card? (C for check, G for give card):").lower()

    if choice == "c":
        dealer_hand.append(random.choice(deck))
        print_hand()
        time.sleep(1)
        player_score, dealer_score = final_battle(dealer_hand, player_score, dealer_score)
        #final_battle(dealer_hand,player_score,dealer_score)


    while choice == "g":
        player_hand.append(random.choice(deck))
        print_hand()
        if calculate_sum(player_hand) > 21:
            dealer_score += 1
            print("Dealer WIN")
            break
        choice1 = input("Stay or 1 more card? (C for check, G for give card):").lower()
        if choice1 == "c":
            player_score, dealer_score = final_battle(dealer_hand, player_score, dealer_score)
         #   final_battle(dealer_hand,player_score,dealer_score)
            break
    player_hand = []
    dealer_hand = []
    
