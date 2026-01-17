import random


# game variables
deck = [2,3,4,5,6,7,8,9,10,"jack","queen","king","ace"]
turn = 1
played_cards = []
decks = 0
betting_box = 0
bet_placed = False

# dealer variables
dealer_hand = []
dealer_points = 0

# player variables
player_hand = []
player_points = 0
balance = 100

def draw():
    pass



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
            break
                
def game_cycle():
    pass

def main():
    print("-------Black Jack-------\n")
    print(f"Balance: {balance}")
    betting()
    print(f"Balance: {balance}")
main()


"""
to do list:
    error kiedy nie int
    ekonomia

"""