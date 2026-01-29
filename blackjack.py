import random

deck = [2,3,4,5,6,7,8,9,10,"jack","queen","king","ace"]

class player:
    def __init__(self, balance, points):
        self.balance = balance
        self.points = points
        self.hand = []
        self.bet = 0
        self.betted = False

    def betting(self):
        bet_placed = False
        while bet_placed == False:
            user_input = input("how much money you want to bet: ")
            bet_money = int(user_input)
            print(f"you betted: {bet_money}$")

            if bet_money > self.balance:
                print(f"You dont have enough money")

            else:
                bet_placed = True
                self.balance = self.balance - bet_money
                self.bet = bet_money
    
    def draw_card(self):
        drawn = False
        while drawn == False:
            played_card = random.choice(deck)

            if played_cards.count(played_card) >= 4*decks:
                pass

            else:
                played_cards.append(played_card)
                self.hand.append(played_card)

                if played_card == "ace":
                    if self.points + 11 > 21:
                        self.points = self.points + 1
                        drawn = True

                    else:
                        self.points = self.points + 11
                        drawn = True

                elif played_card == "jack" or played_card == "king" or played_card == "queen":
                    self.points = self.points + 10    
                    drawn = True

                else:
                    self.points = self.points+ int(played_card)
                    drawn = True

    def add_money(self, money):
        self.balance = self.balance + money
    
def game_cycle(player, ai):

    player_doubledown = False
    player_insured = False
    
    if player.points < 21 or ai.points < 21 or player_doubledown != True and len(player.hand) != 3:
        print("-------Black Jack-------\n")
        print(f"Your side:")
        print(f"- Balance: {player.balance}$")
        print(f"- Betted: {player.bet}")
        print(f"- Hand: {player.hand}")
        print(f"- Points: {player.points}\n")
        print(f"Dealer`s side:")
        print(f"- Hand: {ai.hand}")
        print(f"- Points: {ai.points}\n")
       
        if len(player.hand) == 1 and "ace" in ai.hand:
            print(f"- - - - - - - - - - - - - - -")
            print(f"(1) Hit")
            print(f"(2) pass")
            print(f"(3) insurance")
            player_choice = input("your decision: ")
                
            match player_choice:
                case "1":
                    player.draw_card()
                    ai.draw_card()
                            
                case "2":
                    ai.draw_card()

                case "3":
                    player_insured = True
                                
                case _:
                    print("error try normal option")

        if len(player.hand) == 2 and player_insured == False:
            print(f"- - - - - - - - - - - - - - -")
            print(f"(1) Hit")
            print(f"(2) pass")
            print(f"(3) double down")
            player_choice = input("your decision: ")
                
            match player_choice:
                case "1":
                    player.draw_card()
                    ai.draw_card()
                            
                case "2":
                    ai.draw_card()
                    
                case "3":
                    player_doubledown = True
                    player.draw_card()
                    ai.draw_card()
                                
                case _:
                    print("error try normal option")

        else:
                print(f"- - - - - - - - - - - - - - -")
                print(f"(1) Hit")
                print(f"(2) pass")
                player_choice = input("your decision: ")
                
                match player_choice:
                    case "1":
                        player.draw_card()
                        ai.draw_card()
                            
                    case "2":
                        ai.draw_card()
                                
                    case _:
                        print("error try normal option")
    
    if player_doubledown ==True and len(player.hand) == 3:
        if player.points < 21 and player.points > ai.points:
            print("-------Black Jack-------\n")
            print(f"Your side:")
            print(f"- Hand: {player.hand}")
            print(f"- Points: {player.points}\n")
            print(f"Dealer`s side:")
            print(f"- Hand: {ai.hand}")
            print(f"- Points: {ai.points}\n")
            print(f"you won {4 * player.bet}$")
            player.betted = False
            player.points = 0
            ai.points = 0
            player.hand.clear()
            ai.hand.clear()
            played_cards.clear()
            player.add_money(4 * player.bet)

        else:
            print("-------Black Jack-------\n")
            print(f"Your side:")
            print(f"- Hand: {player.hand}")
            print(f"- Points: {player.points}\n")
            print(f"Dealer`s side:")
            print(f"- Hand: {ai.hand}")
            print(f"- Points: {ai.points}\n")
            print(f"you lost {2 * player.bet}$")
            player.betted = False
            player.points = 0
            ai.points = 0
            player.hand.clear()
            ai.hand.clear()
            played_cards.clear()                                

    if player.points >= 21 and player_insured == False:
        print("-------Black Jack-------\n")
        print(f"Your side:")
        print(f"- Hand: {player.hand}")
        print(f"- Points: {player.points}\n")
        print(f"Dealer`s side:")
        print(f"- Hand: {ai.hand}")
        print(f"- Points: {ai.points}\n")
        print(f"you lost {player.bet}$")
        player.betted = False
        player.points = 0
        ai.points = 0
        player.hand.clear()
        ai.hand.clear()
        played_cards.clear()

    if player.points >= 21 and player_insured == True:
        print("-------Black Jack-------\n")
        print(f"Your side:")
        print(f"- Hand: {player.hand}")
        print(f"- Points: {player.points}\n")
        print(f"Dealer`s side:")
        print(f"- Hand: {ai.hand}")
        print(f"- Points: {ai.points}\n")
        print(f"you insurred and lost 0$")
        player.betted = False
        player.points = 0
        ai.points = 0
        player.add_money(player.bet)
        player.hand.clear()
        ai.hand.clear()
        played_cards.clear()


    elif ai.points >=21:
        print("-------Black Jack-------\n")
        print(f"Your side:")
        print(f"- Hand: {player.hand}")
        print(f"- Points: {player.points}\n")
        print(f"Dealer`s side:")
        print(f"- Hand: {ai.hand}")
        print(f"- Points: {ai.points}\n")
        print(f"you won {2 * player.bet}$")
        player.betted = False
        player.points = 0
        ai.points = 0
        player.hand.clear()
        ai.hand.clear()
        played_cards.clear()
        player.add_money(2 * player.bet)
        
    
def main():
    player_1 = player(100, 0)
    dealer = player(0, 0)
    global played_cards 
    played_cards = []
    global decks 
    decks = 1
    decks_number_choosen = False
    game_on = True
    global betted
    betted = False
    
    
    print("-------Black Jack-------\n")
    while decks_number_choosen == False:
        user_input = input("how many decks you want to use(1-8): ")
        decks= int(user_input)
        if decks <1 or decks > 8:
            print("decks number should be between 1 and 8")
        else:
            decks_number_choosen = True
   
    while game_on == True:
        if player_1.betted == False:
            print("-------Black Jack-------\n")
            print(f"your balance {player_1.balance}$")
            player_1.betting()
            player_1.betted = True
        elif player_1.balance == 0:
            game_on = False
            print("You lost everything")
        else:    
            game_cycle(player_1, dealer)
    
main()


