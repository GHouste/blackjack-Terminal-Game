import random

deck = [2,3,4,5,6,7,8,9,10,"jack","queen","king","ace"]

class player:
    def __init__(self, balance, points):
        self.balance = balance
        self.points = points
        self.hand = []
        self.bet = 0

    def betting(self, balance):
        bet_placed = False
        while bet_placed == False:
            user_input = input("how much money you want to bet: ")
            print(user_input)
            print(type(user_input))
            bet_money = int(user_input)
            print(f"bet money: {bet_money}")
            print(type(bet_money))
            
            if type(bet_money)  != int:
                print("Debil")
            if bet_money > self.balance:
                print(f"You dont have enough money")
            else:
                bet_placed = True
                self.balance = self.balance - bet_money
                self.bet = bet_money
    
    def draw_card(self):
        played_card = random.choice(deck)
        if played_cards.count(played_card) >= 4*decks:
            pass
        else:
            played_cards.append(played_card)
            self.hand.append(played_card)
            if played_card == "ace":
                if self.points + 11 > 21:
                    self.points = self.points + 1
                else:
                    self.points = self.points + 11
            elif played_card == "jack" or played_card == "king" or played_card == "queen":
                self.points = self.points + 10    
            else:
                self.points = self.points+ int(played_card)

def game_cycle():
    pass

def main():

    player_1 = player(100, 0)
    dealer = player(0, 0)
    global played_cards 
    played_cards = []
    global decks 
    decks = 1
    decks_number_choosen = False
    game_on = True
    turn = 1

    """
    print("-------Black Jack-------\n")
    while decks_number_choosen == False:
        user_input = input("how many decks you want to use(1-8): ")
        decks= int(user_input)
        if decks <1 or decks > 8:
            print("decks number should be between 1 and 8")
        else:
            decks_number_choosen = True
    """
    #while game_on ==True:
    print("-------Black Jack-------\n")
    print(played_cards)
    print(player_1.hand)
    print(player_1.points)
    player_1.draw_card()
    print(played_cards)
    print(player_1.hand)
    print(player_1.points)
    
main()


"""
to do list:
    error kiedy nie int
    ekonomia

"""