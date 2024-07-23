#First things first, you need to create a basic menu system scientists can store information about their current space mission.

#Step 1: A print statement has been used to welcome the scientist to the menu system.
#Use a print statement underneath which reads "Please provide details of the current mission."

print("Hello earthling scientist!")


#Step 2: Below, the lead astronaut's name will be stored as a variable called 'lead_astronaut.'
#Use the variable named 'mission_name' to store "Mars Rover Mission" and 'launch_year' to store "2035."


lead_astronaut = input("Enter the lead astronaut's name: ")
mission_name = input("What is the mission name? ")
launch_year = 2035

#Step 3: Fill in the variable names between the strings provided to create a mission brief. Make sure to use a print statement to view the mission brief.

mission_brief = print(f"{mission_name} will commence in {int(launch_year)} lead by {lead_astronaut}")


#Step 4: The project gets delayed by 3 years because *beaucracy*. Go back to step 2 and add 3 to the launch year. Run the code to check if it works.
