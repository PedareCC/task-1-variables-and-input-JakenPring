#You quickly realise that one of the scientists has a habit of writing IN ALL CAPS and it drives you insane. You've asked him to stop, but he's a mad man. 

#Step 1: Prompt the scientist to write a mission description using 'input.' Then in the print statement underneath, use the .lower function to make his writing lower case.

mission_description = input("Write a mission description: ")
mission_description_lowercase = mission_description.lower()
print(mission_description_lowercase)


#Step 2: NASA has a strict word count for how long a mission description can be. Keep it simple- it's not rocket science!:P 
#Use a print statement with the len function to find out how many characters are in the mission_description.

description_length = len(mission_description)
print(description_length)


#Step 3: To create a top secret mission code for this project, you have been asked to take the first three letters of the mission name and the last three letters 
# of the mission name and combine them. 
# Below is an example from a previous mission where they used the second and second to last letters. 
       #Underneath the example have a go at making a mission code for the current mission.

                  
# mission_name = "Pluto Mission"
# second_char = mission_name[1]    
# second_to_last_chars = mission_name[-2]
# mission_code = first_three_chars + last_two_chars
# print(f"The mission code is: {mission_code}")

mission_name = "Mars' New Rover"
first_char = mission_name[0]
second_char = mission_name[1]
third_char = mission_name[2]
first_three_chars = first_char + second_char + third_char
second_to_last_chars = mission_name[-2]
last_char = mission_name[-1]
last_two_chars = second_to_last_chars + last_char
mission_code = first_three_chars + last_two_chars
print(f"The mission code is: {mission_code}")