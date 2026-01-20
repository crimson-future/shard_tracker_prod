Welcome to the Shard Tracker! This is a small piece of code, designed to help manage
the mechanics, scaling, and growth of a system in my homebrew DND campaign. 

========OVERVIEW=========
Players have access to items called Dragon Shards within the campaign. These can be 
attuned to once found and acquired. An attuned player gains access to incrementally 
more powers and abilities as time goes on. Each level requires XP, called here 
"Corruption Points". Each level requires more. Points are gained from actions taken.
The amount of points gained is dependant on both the action taken and the current
level of corruption the player has. Removing attunement to free yourself from their 
influence is harder and harder the higher the player's corruption level is.

========USAGE========
This code requires python3 and the datafile.txt object in the same directory as the code.
When booting the code, the player stats will be read from JSON in the datafile.txt object
and loaded as "Players". First, select a player, then select the actions to take at will. 
The tracker will update the file accordingly, keeping track of both their points and 
their level. 

========FUTURE UPDATES========
1) Refactoring the code into modules
    - Actioning first
2) File OS tracking, easier usage via os module
3) Additional Menu options
4) Character creation/addition/removal support
5) Undo function, addition of older savestate/back up version
6) Action logging tracker

Author: Crimson Future
Campaign: The Dragon Star
