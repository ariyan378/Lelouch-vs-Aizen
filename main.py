import random

class Character:
    '''
    We are creating a class called character that storesthe character name and its all power attribute he can use in the fight
    
    we will also shows these attribute to the user so that they can see using show_stats() function
    '''
    
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes  

    def show_stats(self):
        print(f"\n--- {self.name}'s Arsenal ---")
        for i, (attr, score) in enumerate(self.attributes, 1):
            print(f"{i}-> {attr}")

class BattleEngine:
    def __init__(self, player_char, computer_char):
        self.player = player_char
        self.computer = computer_char

    def start_clash(self):
       
        player_hp = 100
        comp_hp = 100

        print(f"{self.player.name} vs {self.computer.name}")

        while True:

            self.player.show_stats()
            print(f"\n {self.player.name}: {player_hp} Hp | {self.computer.name}: {comp_hp} Hp")

            try:
                choice = int(input(f"Choose an attribute for {self.player.name} (1-8): ")) - 1
                p_attr, p_val = self.player.attributes[choice]
            except (ValueError, IndexError):
                print("Invalid command! You lose this round's focus.")
                continue 
                
            c_choice = random.randint(0, 7)
            c_attr, c_val = self.computer.attributes[c_choice]

            luck_l = random.randint(-5, 5)
            luck_a = random.randint(-5, 5)
            total_player_power = p_val + luck_l
            total_computer_power = c_val + luck_a

            print(f"\n{self.player.name} uses: {p_attr} ({p_val}) + Luck ({luck_l}) = {total_player_power}")
            print(f"{self.computer.name} counters with: {c_attr} ({c_val}) + Luck ({luck_a}) = ({total_computer_power})")
            print("____________________________\n")
            
            
            if total_player_power > total_computer_power:
                print(f"Outcome: {self.player.name} outmaneuvered the enemy!")
                comp_hp -= random.randint(10, 20) 
            elif total_player_power < total_computer_power:
                print(f"Outcome: {self.computer.name} dominates the field!")
                player_hp -= random.randint(10, 20) 
            else:
                print("Outcome: A perfect stalemate!")
                    
            
            if player_hp <= 0 and comp_hp <= 0:
                print("\n---  draw  ----")
                break
            elif player_hp <= 0:
                print(f"\n WINNER: {self.computer.name} - 'Since when were you under the impression you were winning?'")
                break
            elif comp_hp <= 0:
                print(f"\nWINNER: {self.player.name} - 'All Hail Lelouch!'")
                break

lelouch_stats = [
    ("Strategic Genius", 10), ("Chess Mastery", 8), ("Political Cunning", 10),
    ("Willpower", 7), ("Geass Eye", 10), ("Leadership (Zero)", 10),
    ("Immortality", 10), ("Knightmare Pilot", 6)
]

aizen_stats = [
    ("Kyoka Suigetsu", 10), ("Spiritual Pressure", 10), ("Hogyoku Power", 10),
    ("Strategic Mind", 10), ("Manipulation", 10), ("Swordsmanship", 9),
    ("Kido Mastery", 9), ("Flash Steps", 9)
]

print("Charcater List: \
    1.Lelouch Vi Britania\
    2.Aizen\n")
CharacterChoice= int(input('Enter your Choice 1/2 :'))
if CharacterChoice==1:
    player= Character("Lelouch Vi Britannia", lelouch_stats)
    computer = Character("Sosuke Aizen", aizen_stats)
else:
    computer= Character("Lelouch Vi Britannia", lelouch_stats)
    player = Character("Sosuke Aizen", aizen_stats)


game = BattleEngine(player, computer)
game.start_clash()