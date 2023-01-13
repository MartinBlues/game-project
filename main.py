#BlackJack Game
import random

class Card:
    def __init__(self, value, name, suit):
        self.value = value
        self.name = name
        self.suit = suit
        
    def __str__(self):
        return f"{self.name} of {self.suit}"

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.points = 0
        self.is_stopped = False
        
    def draw_card(self):
        value = random.randint(6, 11)
        name = self.get_card_name(value)
        suit = self.get_card_suit()
        card = Card(value, name, suit)
        self.cards.append(card)
        self.points += value
        
    def get_card_name(self, value):
        if value == 11:
            return "Ace"
        elif value == 10:
            return "Jack"
        elif value == 9:
            return "Queen"
        elif value == 8:
            return "King"
        else:
            return str(value)
        
    def get_card_suit(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        return random.choice(suits)
    
class Computer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.is_stopped = False
        
    def play(self):
        self.draw_card()
            
class Game:
    def __init__(self):
        self.player = Player("Player1")
        self.computer = Computer("Computer")
        self.over = False
        
    def play(self):
        while not self.over:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.player.draw_card()
                self.computer.play()
                self.check_points()
                self.display_points()
                self.display_computer_card()
            elif choice == "2":
                self.player.is_stopped = True
                self.check_points()
                if self.player.points > self.computer.points and self.player.points <= 21 and self.computer.points <= 21:
                    self.over = True
                    print(f"{self.player.name} wins!\n")
                elif self.computer.points > self.player.points and self.computer.points <= 21 and self.player.points <= 21:
                    self.over = True
                    print(f"{self.computer.name} wins!\n")
                else:
                    self.over = True
                    print("It's a tie!\n")
                self.display_points()
                self.player.points = 0
                self.computer.points = 0
            elif choice == "3":
                self.over = True
                exit()
            else:
                print("Invalid choice. Please enter a valid option.\n")

    def display_computer_card(self):
        last_card = self.computer.cards[-1]
        print(f"{self.computer.name} drew: {last_card}\n")

    def display_menu(self):
        print("Blackjack Game\n")
        print("1. Draw a card")
        print("2. Stop")
        print("3. Exit\n")

    def display_points(self):
        print(f"\n{self.player.name} points: {self.player.points}")
        last_card = self.player.cards[-1]
        print(f"{self.player.name} drew: {last_card}\n")
        print(f"{self.computer.name} points: {self.computer.points}")
        
    def check_points(self):
        if self.player.points == 21:
            print(f"{self.player.name} wins with 21 points!\n")
            self.over = True
        elif self.computer.points == 21:
            print(f"{self.computer.name} wins with 21 points!\n")
            self.over = True
        elif self.player.points > 21:
            print(f"{self.player.name} lost with {self.player.points} points!\n")
            self.over = True
        elif self.computer.points > 21:
            print(f"{self.computer.name} lost with {self.computer.points} points!\n")
            self.over = True
        elif self.player.is_stopped and self.computer.points > self.player.points and self.computer.points <= 21:
            print(f"{self.computer.name} wins with {self.computer.points} points!\n")
            self.over = True
        elif self.computer.is_stopped and self.player.points > self.computer.points and self.player.points <= 21:
            print(f"{self.player.name} wins with {self.player.points} points!\n")
            self.over = True
        elif self.player.is_stopped and self.computer.is_stopped:
            if self.player.points == self.computer.points:
                print("It's a tie!")
            elif self.player.points > self.computer.points:
                print(f"{self.player.name} wins with {self.player.points} points!\n")
            else:
                print(f"{self.computer.name} wins with {self.computer.points} points!\n")

def test_game():
    game = Game()
    while True:
        game.play()
        if game.over:
            game.player.points = 0
            game.computer.points = 0
            game.over = False
        else:
            break

test_game()
