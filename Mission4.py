#Your supervisor is extremely impressed with your work so far so he puts you on the toughest project yet. 
#Using the evidence provided by the Mars Rover Perserverance, you are going to produce a report which indicates 
   # whether the environmental conditions were potentially conducive to life and link it to the Mars Rover project objectives.

#Step 1: Collect the geological data by asking the rover if there is any sedimentary rocks (Yes or No), river chanels (Yes or No) and what types of minerals were found.

sedimentary_rocks = input("Are there any sedimentary rocks? (Yes/No) ")
river_channels = input("Are there any river channels? (Yes/No) ")
mineral_type = input("What minerals were found? ")


#Step 2: Set up a boolean (True or Talse) to help us later assess if water is or is not present 

water_present = False


#Step 3: Use if statements to change water_present to True if sedimentary_rocks or river_channels were found.

if sedimentary_rocks.lower() == "yes" or river_channels.lower() == "yes":
  water_present = True 
  print("Water is present. Life may be sustainable on planet.")


#Step 4: If 'Clay' or 'Carbonates' were detected under mineral_type, change water_present to True and print the statement below.

if "clay" in mineral_type.lower() or "carbonates" in mineral_type.lower():
  water_present = True
  print("Water is present. Life may be sustainable on planet.")

