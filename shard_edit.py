import time
import os

shard_colors=["Red","Blue","Green","Orange"]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def edit_shards(): 
    while True:
        print(f"Current shard list: {shard_colors}")
        choice = input("Welcome to the shard editor. What would you like to do? Enter a number to select:\n0: Go back without changing anything\n1: Add a shard to the character\n2: Remove a shard from the character\n3: Change the character's shard\n\n Selection: ")
        if choice == "0": 
            print("No further changes made. Returning to menu.")
            time.sleep(1.0)
            break
        else: 
            while True:
                clear_screen()
                print(f"Current shard list: {shard_colors}")

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
                            shard_colors.append(color)
                            print(f"\n Shard added.")
                            time.sleep(1.0)
                            break
                    break

                #Remove from list
                elif choice == "2":
                    clear_screen()
                    print("Pick a shard the player will remove by number, or type 0 to go back: ") #0 is set as Exit option to avoid complications around the incremented choice numbers
                    while True:
                        # If there are no shards left, exit
                        if not shard_colors:
                            print("No shards left to remove.")
                            break
                        print("0: Return to shard menu")
                        for i, shard in enumerate(shard_colors, start=1):
                            print(f"{i}: {shard}")
                        shard_choice = input("\nSelection: ")
                        if shard_choice == "0":
                            clear_screen()  
                            print("No further changes made. Returning to menu.")
                            break
                        try:
                            index = int(shard_choice) - 1
                            if index < 0 or index >= len(shard_colors):
                                print("That shard number doesn't exist. Please try again.")
                                continue
                            print(f"Removing shard {shard_colors[index]} from the list for self...")
                            time.sleep(1.0)
                            del shard_colors[index]
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
                        if not shard_colors:
                            print("No shards to edit.")
                            break
                        print("0: Return to shard menu")
                        for i, shard in enumerate(shard_colors, start=1):
                            print(f"{i}: {shard}")
                        shard_choice = input("\nSelection: ")
                        if shard_choice == "0":
                            clear_screen()  
                            print("No further changes made. Returning to menu.")
                            break
                        try:
                            index = int(shard_choice) - 1
                            if index < 0 or index >= len(shard_colors):
                                print("That shard number doesn't exist. Please try again.")
                                continue
                            selection = input("What would you like to replace this shard value with?\n")
                            print("Replacing shard...")
                            time.sleep(1.0)
                            shard_colors[index] = selection
                            clear_screen()
                            print("Shard changed successfully!")  
                            break
                        except ValueError:
                            print("Bad input (not a number). Please try again.")
                    break             
        


edit_shards()