import random

class Character:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes  # This is a list of tuples (Name, Score)

    def show_stats(self):
        print(f"\n--- {self.name}'s Arsenal ---")
        for i, (attr, score) in enumerate(self.attributes, 1):
            print(f"{i}. {attr} ---- {score}")

class BattleEngine:
    def __init__(self, player_char, computer_char):
        self.player = player_char
        self.computer = computer_char

    def start_clash(self):
        print(f"BATTLE START: {self.player.name} vs {self.computer.name}")
        
        # Game runs for 3 rounds
        player_score = 0
        comp_score = 0
        
        for round_num in range(1, 4):
            print(f"\n--- ROUND {round_num} ---")
            self.player.show_stats()
            
            # 1. Player Choice
            try:
                choice = int(input(f"Choose an attribute for {self.player.name} (1-8): ")) - 1
                p_attr, p_val = self.player.attributes[choice]
            except (ValueError, IndexError):
                print("Invalid command! You lose this round's focus.")
                continue

            # 2. Computer Choice (Random attribute from Aizen's list)
            c_choice = random.randint(0, 7)
            c_attr, c_val = self.computer.attributes[c_choice]

            # 3. The "Strategist" Luck Factor
            # We add a random "Chaos Factor" between -1 and +2
            luck = random.randint(-1, 2)
            total_player_power = p_val + luck

            print(f"\n{self.player.name} uses: {p_attr} ({p_val}) + Luck ({luck}) = {total_player_power}")
            print(f"{self.computer.name} counters with: {c_attr} ({c_val})")

            # 4. Determine Round Winner
            if total_player_power > c_val:
                print(f"Outcome: {self.player.name} outmaneuvered the enemy!")
                player_score += 1
            elif total_player_power < c_val:
                print(f"Outcome: {self.computer.name} dominates the field!")
                comp_score += 1
            else:
                print("Outcome: A perfect stalemate!")

        # Final Result
        print("\n========================")
        if player_score > comp_score:
            print(f"FINAL WINNER: {self.player.name} - 'All according to plan.'")
        elif comp_score > player_score:
            print(f"FINAL WINNER: {self.computer.name} - 'You were under my hypnosis the whole time.'")
        else:
            print("FINAL RESULT: It's a draw. The world remains in balance.")

# --- Character Data ---
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

# --- Initialize and Run ---
char1 = Character("Lelouch Vi Britannia", lelouch_stats)
char2 = Character("Sosuke Aizen", aizen_stats)

game = BattleEngine(char1, char2)
game.start_clash()