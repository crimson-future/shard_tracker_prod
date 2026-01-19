import json
import os
import time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


#======================================================================#
class Character:
    def __init__(self, player_name, tier_level, current_points, shard_count, shard_colors=None):
        self.player_name = player_name
        self.tier_level = int(tier_level)
        self.current_points = int(current_points)
        self.shard_count = int(shard_count)
        self.shard_colors = [] if shard_colors is None else shard_colors

    # HELPER
    #======================================================================#
    #Stat Show
    def __repr__(self):
        return (
            f"name: {self.player_name.capitalize()}\n"
            f"tier_level: {self.tier_level}\n"
            f"current_points: {self.current_points}\n"
            f"shard_count: {self.shard_count}\n"
            f"shard_colors: {self.shard_colors}\n"
        )

    #Output Conversion
    def to_dict(self):
        return {
            "name": self.player_name,
            "tier_level": self.tier_level,
            "current_points": self.current_points,
            "shard_count": self.shard_count,
            "shard_colors": self.shard_colors
        }
    #======================================================================#


    # DEBUG METHODS
    #======================================================================#
    def retrieve_stat(self):
        selected_attribute = input("Please select an attribute: ").lower()
        value = getattr(self, selected_attribute, "Attribute not found")
        print(
            f"The selected attribute {selected_attribute} for "
            f"{self.player_name.capitalize()} is {value}"
        )


    #======================================================================#


    # MENU ACTIONS
    #======================================================================#
    def calc_tier(self):
        tier = self.current_points//100
        self.tier_level = tier      

    def cast_a_spell(self):
        cast_incr = 2
        print("Casting a spell...")
        time.sleep(1.0)
        self.current_points += cast_incr
        self.calc_tier()
        print(f"{self.player_name.capitalize()}'s corruption points increased by {cast_incr}. The new points for the player is {self.current_points}. Their tier is {self.tier_level}.\n")
        savestate(players, "file_rw_practice/datafile.txt")

    def day_passed(self):
        day_incr = 10
        print("Taking a long rest...")
        time.sleep(1.0)
        self.current_points += day_incr
        self.calc_tier()
        print(f"{self.player_name.capitalize()}'s corruption points increased by {day_incr}. The new points for the player is {self.current_points}. Their tier is {self.tier_level}.\n")
        savestate(players, "file_rw_practice/datafile.txt")

    def char_downed(self):
        down_incr = 20
        print("Knocking character out...")
        time.sleep(1.0)
        self.current_points += down_incr
        self.calc_tier()
        print(f"{self.player_name.capitalize()}'s corruption points increased by {down_incr}. The new points for the player is {self.current_points}. Their tier is {self.tier_level}.\n")
        savestate(players, "file_rw_practice/datafile.txt")
    
    def detune_fail(self):
        fail_incr = 30
        print("Failing to break the curse...")
        time.sleep(1.0)
        self.current_points += fail_incr
        self.calc_tier()
        print(f"{self.player_name.capitalize()}'s corruption points increased by {fail_incr}. The new points for the player is {self.current_points}. Their tier is {self.tier_level}.\n")
        savestate(players, "file_rw_practice/datafile.txt")

    def detune_succ(self):
        succ_decr = -15
        print("Beating back the curse with willpower...")
        time.sleep(1.0)
        self.current_points += succ_decr
        self.calc_tier()
        print(f"{self.player_name.capitalize()}'s corruption points decreased by {abs(succ_decr)}. The new points for the player is {self.current_points}. Their tier is {self.tier_level}.\n")
        savestate(players, "file_rw_practice/datafile.txt")

    def recov_magic(self):
        rec_decr = -10
        print("Removing a fraction of the curse...")
        time.sleep(1.0)
        self.current_points += rec_decr
        self.calc_tier()
        print(f"{self.player_name.capitalize()}'s corruption points decreased by {abs(rec_decr)}. The new points for the player is {self.current_points}. Their tier is {self.tier_level}.\n")
        savestate(players, "file_rw_practice/datafile.txt")

#======================================================================#
#File Manager Functions, loadfile populates 'players' list with Character() class player objects
def loadfile(filename):
    chars = {}

    with open(filename, "r") as file:
        data = json.load(file)

    for entry in data:
        name = entry["name"].lower()
        chars[name] = Character(
            player_name=name,
            tier_level=entry["tier_level"],
            current_points=entry["current_points"],
            shard_count=entry["shard_count"],
            shard_colors=entry.get("shard_colors", [])
        )

    return chars

#Outputs current state to file, 'saves'.
def savestate(players, filename):
    savestate = [char.to_dict() for char in players.values()]
    with open (filename, "w") as f:
        json.dump(savestate, f, indent=2)



#======================================================================#
#Effectively the Main structure
def menu_framework(players): 
    selected_char = None
    players = players
    clear_screen()
    #Character Selection - Should be at highest scope for menu_framework, since it's only retrieving a character, not acting on one.
    def character_select(players): #Update to select from a predefined list by selecting index numbers
        while True:
            selected_char = input("Please input a character name, or type \"exit\" to go back: ").lower()
            if selected_char.lower() == "exit":
                return None
            if selected_char in players:
                selected_char = players[selected_char]
                return selected_char
            else:
                print("No such character, try again.")
                continue

    #Show current stats block for all players            
    def show_all(players):  
        for player in players:
            print(f"{players[player]}")    

    #Contains the objects for the menu options as a list of dicts    
    def print_actions():
        actions_list = [
        {
            "act_num": 0,
            "act_name": "Cast a spell"
        },{
            "act_num" : 1, 
            "act_name": "Mark that a day has passed"
        },{
            "act_num" : 2, 
            "act_name": "Character is downed"
        },{
            "act_num" : 3, 
            "act_name": "De-Attunement has failed"
        },{
            "act_num" : 4, 
            "act_name": "De-Attunement has succeeded"
        },{
            "act_num" : 5, 
            "act_name": "Recovery Magic Applied"
        },{
            "act_num" : 6, 
            "act_name": "Select Active Player" 
        },{
            "act_num" : 7, 
            "act_name": "Show All Stat Blocks" 
        },{
            "act_num" : 8, 
            "act_name": "Select Active Shard"
        },{
            "act_num" : 9, 
            "act_name": "Change Day Count"
        },{
            "act_num" : 10, 
            "act_name": "Change Shard Count"
        },{
            "act_num" : 11, 
            "act_name": "Clear XP"
        },{
            "act_num" : 12, 
            "act_name": "Show Thresholds"
        },{
            "act_num" : 13, 
            "act_name": "Exit"
        }
        ]

        print("Choose an action from the following list:\n===General Usage===")
        for i in range(0, 6):
            print(f"{actions_list[i]['act_num']}: {actions_list[i]['act_name']}")
        print("\n===Maintenance===")
        for i in range(6, 13):
            print(f"{actions_list[i]['act_num']}: {actions_list[i]['act_name']}")
        print("\n===Exit===")
        for i in range(13,14):
            print(f"{actions_list[i]['act_num']}: {actions_list[i]['act_name']}")
        return actions_list
    
    def get_action(): #Retrieves the action{} object for the chosen index as an action_flag
        actions_list = print_actions()  # show menu once, keep list
        while True:
            action_input = input("\nSelection: ")
            try:
                action_sel = int(action_input)
            except ValueError:
                clear_screen()
                print("\nBad input: please type a number selection from the list.")
                print_actions()
                continue
            if 0 <= action_sel < len(actions_list):
                return actions_list[action_sel]
            else:
                clear_screen()
                print("\nOut of range: choose one of the listed numbers.")
                print_actions()

    def take_action(action):
        nonlocal selected_char
        action_name = action["act_name"]
        action_num = action["act_num"]
        clear_screen()
        #Replace with Character.Exit() method, called if action_num ==13
        #Each Character.X() method needs a loop as well, with a "Confirm" or "Exit". Both options should allow for a display of current status.
        #Use action_name as a header for each method Character.X() for new menu selection. 

        if action_num == 0: #"Cast a spell"
            print(action_name)
            if selected_char != None:
                selected_char.cast_a_spell()
            else:
                print("No character selected! No changes made.\n")
            return action_num

        elif action_num == 1: #Take a Long Rest/Mark a Day as Passed
            print(f"Selected: {action_name}\n")
            if selected_char != None:
                selected_char.day_passed()
            else:
                print("No character selected! No changes made.\n")
            return action_num

        elif action_num == 2: #Character downed/knocked unconscious
            print(f"Selected: {action_name}\n")
            if selected_char != None:
                selected_char.char_downed()
            else:
                print("No character selected! No changes made.\n")
            return action_num

        elif action_num == 3: #De-attunement failed
            print(f"Selected: {action_name}\n")
            if selected_char != None:
                selected_char.detune_fail()
            else:
                print("No character selected! No changes made.\n")
            return action_num

        elif action_num == 4: #De-attunement successful
            print(f"Selected: {action_name}\n")
            if selected_char != None:
                selected_char.detune_succ()
            else:
                print("No character selected! No changes made.\n")
            return action_num

        elif action_num == 5: #Greater Restoration/Remove Curse applied
            print(f"Selected: {action_name}\n")
            if selected_char != None:
                selected_char.recov_magic()
            else:
                print("No character selected! No changes made.\n")
            return action_num

        elif action_num == 6: #Changes Active Character
            print(f"Selected: {action_name}\n")
            selected_char = character_select(players)
            clear_screen()
            return action_num

        elif action_num == 7: #Show all player stat blocks, overview, not Character() method but does leverage the __repr__(). 
            print(f"Selected: {action_name}\n")
            show_all(players)
            input("\nPress Enter to return to menu\n")
            clear_screen()
            return action_num 

#Not Yet Implemented - Placeholders
        elif action_num == 8:
            print(action_name)
            print("Placeholder, feature not yet implemented.")
            return action_num  
        elif action_num == 9:
            print(action_name)
            print("Placeholder, feature not yet implemented.")
            return action_num               
        elif action_num == 10:
            print(action_name)
            print("Placeholder, feature not yet implemented.")
            return action_num 
        elif action_num == 11:
            print(action_name)
            print("Placeholder, feature not yet implemented.")
            return action_num
        elif action_num == 12:
            print(action_name)
            print("Placeholder, feature not yet implemented.")
            return action_num  
        elif action_num == 13:
            print(action_name)
            return action_num
        else:
            return "Something went wrong."
    

#From here, execute a loop that sets, enters, actions, and exits the menu
    while True: #action_flag != 13:
        print(f"Selected Character: \n{selected_char}\n")
        action = get_action()
        result = take_action(action)
        if result == 13:
            clear_screen()
            print("+ + + + + + + + + + + + + + + + + + +\nExiting - Current character status:\n+ + + + + + + + + + + + + + + + + + +\n")
            show_all(players)
            print("\n+ + + + + + + + + + + + + + + + + + +\nGoodbye!\n+ + + + + + + + + + + + + + + + + + +")
            break


#Execution - Pre-Main
#======================================================================#
filename = "datafile.txt"
players = loadfile(filename)
menu_framework(players)
#======================================================================#


#+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + #


#Debug Options and test Actions
#======================================================================#
#print(f"{players['player_name']}\n\n") #DBP, displays created dict
# #players["Krivskan".lower()].retrieve_stat() #Turn into a method later

#selected_char = character_select(players)
i#print(selected_char)
#selected_char.show_all()

# selected_char.current_points += 1
# print(selected_char.current_points)

# #Set as a Write function for every Character override method
# savestate(players, "file_rw_practice/datafile.txt")
#======================================================================#
