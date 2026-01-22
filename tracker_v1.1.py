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


    #RUNNING METHODS
    #======================================================================#
    def calc_tier(self):
        if self.current_points < 0:
            self.current_points = 0
        self.tier_level = self.current_points//100      

    # MENU ACTIONS
    #======================================================================#
    def cast_a_spell(self): #0
        cast_incr = 2
        print("Casting a spell...")
        time.sleep(1.0)
        self.current_points += cast_incr
        self.calc_tier()
        print(f"{self.player_name.capitalize()}'s corruption points increased by {cast_incr}. The new points for the player is {self.current_points}. Their tier is {self.tier_level}.\n")
        savestate(players, filename)

    def day_passed(self): #1
        day_incr = 10
        print("Taking a long rest...")
        time.sleep(1.0)
        self.current_points += day_incr
        self.calc_tier()
        print(f"{self.player_name.capitalize()}'s corruption points increased by {day_incr}. The new points for the player is {self.current_points}. Their tier is {self.tier_level}.\n")
        savestate(players, filename)

    def char_downed(self): #2
        down_incr = 20
        print("Knocking character out...")
        time.sleep(1.0)
        self.current_points += down_incr
        self.calc_tier()
        print(f"{self.player_name.capitalize()}'s corruption points increased by {down_incr}. The new points for the player is {self.current_points}. Their tier is {self.tier_level}.\n")
        savestate(players, filename)
    
    def detune_fail(self): #3
        fail_incr = 30
        print("Failing to break the curse...")
        time.sleep(1.0)
        self.current_points += fail_incr
        self.calc_tier()
        print(f"{self.player_name.capitalize()}'s corruption points increased by {fail_incr}. The new points for the player is {self.current_points}. Their tier is {self.tier_level}.\n")
        savestate(players, filename)

    def detune_succ(self): #4
        succ_decr = -15
        print("Beating back the curse with willpower...")
        time.sleep(1.0)
        self.current_points += succ_decr
        self.calc_tier()
        print(f"{self.player_name.capitalize()}'s corruption points decreased by {abs(succ_decr)}. The new points for the player is {self.current_points}. Their tier is {self.tier_level}.\n")
        savestate(players, filename)

    def recov_magic(self): #5
        rec_decr = -10
        print("Removing a fraction of the curse...")
        time.sleep(1.0)
        self.current_points += rec_decr
        self.calc_tier()
        print(f"{self.player_name.capitalize()}'s corruption points decreased by {abs(rec_decr)}. The new points for the player is {self.current_points}. Their tier is {self.tier_level}.\n")
        savestate(players, filename)

    
    def edit_shards(self): # 8
        while True:
            print(f"Current shard list for {self.player_name}: {self.shard_colors}\n")
            choice = input("Welcome to the shard editor. What would you like to do? Enter a number to select:\n0: Go back without changing anything\n1: Add a shard to the character\n2: Remove a shard from the character\n3: Change the character's shard\n\n Selection: ")
            if choice == "0": 
                clear_screen()
                print("No further changes made. Returning to menu.")
                time.sleep(1.0)
                break
            else: 
                while True:
                    clear_screen()
                    print(f"Current shard list: {self.shard_colors}\n")
                    #Add to list
                    if choice == "1": 
                        clear_screen()
                        color=input("Please enter a shard color to add, or type 0 to quit. Example: Red\n")
                        while True:
                            clear_screen()
                            if color=="0":
                                clear_screen()  
                                print("No further changes made. Returning to menu.")
                                break
                            else:
                                color=color.capitalize()
                                self.shard_colors.append(color)
                                clear_screen()
                                print(f"\n Shard added.\n")
                                savestate(players, filename)

                                break
                        break
                    #Remove from list
                    elif choice == "2":
                        clear_screen()
                        print("Pick a shard the player will remove by number, or type 0 to go back: ") #0 is set as Exit option to avoid complications around the incremented choice numbers
                        while True:
                            # If there are no shards left, exit
                            if not self.shard_colors:
                                print("No shards, returning...")
                                time.sleep(1.0)
                                clear_screen()
                                print("No shards left to remove.\n")
                                break
                            print("0: Return to shard menu")
                            for i, shard in enumerate(self.shard_colors, start=1):
                                print(f"{i}: {shard}")
                            shard_choice = input("\nSelection: ")
                            if shard_choice == "0":
                                time.sleep(1.0)
                                clear_screen() 
                                print("No further changes made. Returning to menu.")
                                break
                            try:
                                index = int(shard_choice) - 1
                                if index < 0 or index >= len(self.shard_colors):
                                    print("That shard number doesn't exist. Please try again.")
                                    continue
                                print(f"Removing shard {self.shard_colors[index]} from the list for self...")
                                time.sleep(1.0)
                                del self.shard_colors[index]
                                savestate(players, filename)
                                break
                            except ValueError:
                                print("Bad input (not a number). Please try again.")
                        break
                    #Change a list value
                    elif choice == "3":
                        clear_screen()
                        print("Pick a shard the player will modify by number, or type 0 to go back: ") #0 is set as Exit option to avoid complications around the incremented choice numbers
                        while True:
                            # If there are no shards left, exit
                            if not self.shard_colors:
                                time.sleep(1.0)
                                clear_screen()
                                print("No shards to edit.")
                                break
                            print("0: Return to shard menu")
                            for i, shard in enumerate(self.shard_colors, start=1):
                                print(f"{i}: {shard}")
                            shard_choice = input("\nSelection: ")
                            if shard_choice == "0":
                                time.sleep(1.0)
                                clear_screen()
                                print("No further changes made. Returning to menu.")
                                break
                            try:
                                index = int(shard_choice) - 1
                                if index < 0 or index >= len(self.shard_colors):
                                    print("That shard number doesn't exist. Please try again.")
                                    continue
                                selection = input("What would you like to replace this shard value with?\n")
                                print("Replacing shard...")
                                time.sleep(1.0)
                                self.shard_colors[index] = selection
                                clear_screen()
                                print("Shard changed successfully!")  
                                savestate(players, filename)
                                break
                            except ValueError:
                                print("Bad input (not a number). Please try again.")
                            
                        break             

    def reset_char(self): #11
        while True:
            choice=input(f"Are you sure you want to reset all values for {self.player_name}? y/n: ")
            if choice.lower()=='n':
                print("Aborting character stat clear, no changes made.\n")
                break
            elif choice.lower()=='y':
                print("Purging the curse entirely...")
                time.sleep(1.0)
                self.current_points=0
                self.calc_tier()
                self.shard_count=0
                self.shard_colors=[]
                savestate(players, filename)
                print(f"{self.player_name.capitalize()}'s save data has been cleared and set to 0. No shards are in their inventory, and all stats are cleared.\n")
                break
            else:
                print("Bad input. Please try again. ")
                continue


#6 is currently Character Select
#7 is currently Show All Characters
#6 should be Failed Second Attunement, move 6 and 7 to 7 and 8
#Set 9 to Select Shard

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
            "act_name": "Edit Player Shards"
        },{
            "act_num" : 9, 
            "act_name": "placeholder - Change Day Count"
        },{
            "act_num" : 10, 
            "act_name": "placeholder - Change Shard Count"
        },{
            "act_num" : 11, 
            "act_name": "Clear XP for Selected Character"
        },{
            "act_num" : 12, 
            "act_name": "placeholder - Show Thresholds"
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

    def take_action(action): #Selective actions that load the requested Character object and run Character methods based on the selected menu option
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
            if selected_char != None:
                selected_char.calc_tier() #Set to autocalc tier early in case changes were made manually, to avoid confusion
            savestate(players, filename) #saving early autocalc on player load, to ensure stats are set accurately in the file on launch
            clear_screen()
            return action_num

        elif action_num == 7: #Show all player stat blocks, overview, not Character() method but does leverage the __repr__(). 
            print(f"Selected: {action_name}\n")
            show_all(players)
            input("\nPress Enter to return to menu\n")
            clear_screen()
            return action_num 

        elif action_num == 8: #Edit the shards of the selected player (likely not gonna get much use)
            print(f"Selected: {action_name}\n")
            if selected_char != None:
                selected_char.edit_shards()
            else:
                print("No character selected! No changes made.\n")
            return action_num

#Not Yet Implemented - Placeholders
        elif action_num == 9:
            print(action_name)
            print("Placeholder, feature not yet implemented.")
            return action_num               
        elif action_num == 10:
            print(action_name)
            print("Placeholder, feature not yet implemented.")
            return action_num 

        #Implemented
        elif action_num == 11:
            print(f"Selected: {action_name}\n")
            if selected_char != None:
                selected_char.reset_char()
            else:
                print("No character selected! No changes made.\n")
            return action_num
        
        elif action_num == 12:
            print(action_name)
            print("Placeholder, feature not yet implemented.")
            return action_num  

        #Exit key, no additions needed
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
#print(selected_char)
#selected_char.show_all()

# selected_char.current_points += 1
# print(selected_char.current_points)

# #Set as a Write function for every Character override method
# savestate(players, "file_rw_practice/datafile.txt")
#======================================================================#
