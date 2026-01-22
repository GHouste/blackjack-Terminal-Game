import random


# game variables
global deck 
deck = [2,3,4,5,6,7,8,9,10,"jack","queen","king","ace"]
turn = 1
played_cards = []
decks = 0
betting_box = 0
global bet_placed
bet_placed = False

# dealer variables
dealer_hand = []
dealer_points = 0

# player variables
player_hand = []
balance = 100

def draw(points):
    played_card = random.choice(deck)
    print(played_card)
    if played_cards.count(played_card) >= 4*decks:
        pass
    else:
        if played_card == "ace":
            pass
        elif played_card == "jack" or played_card == "king" or played_card == "queen":
            points = points + 10
            return points
        else:
            points + int(played_card)
            return points 




def betting():
    while bet_placed == False:
        user_input = input("how much money you want to bet: ")
        print(user_input)
        print(type(user_input))
        bet_money = int(user_input)
        print(f"bet money: {bet_money}")
        print(type(bet_money))
        
        if type(bet_money)  != int:
            print("Debil")
        if bet_money > balance:
            print(f"You dont have enough money")
        else:
            bet_placed = True
            break
                
def game_cycle():
    pass

def main():

    player_points = 0

    print("-------Black Jack-------\n")
    print(f"Balance: {balance}")
    print(player_points)
    draw(player_points)
    print(player_points)
    betting()

main()


"""
to do list:
    error kiedy nie int
    ekonomia

"""