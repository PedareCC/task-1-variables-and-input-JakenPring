# It's time to perform some more serious calculations using integers and floats (integers in disguise- they just have decimal points).

#Step 1: We need to store the distance to mars in kilometers in a variable named 'distance_to_mars.' This should be input as a float.

distance_to_mars = 54.6
speed_kmph = 1000          # the average speed of a rocket in kilometers per hour



#Step 2: Convert the distance to mars from millions of kilometers to just kilometers (multiply by 1 million). This new variable has been named distance_kim.

distance_km = distance_to_mars * 1000000



#Step 3: Calculate the total travel time in hours by dividing the distance_km by the speed_kmph

travel_time_hours = distance_km / speed_kmph



#Step 4: Convert travel time from hours to days by creating a new variable called 'travel_time_days.'

travel_time_days = travel_time_hours / 24

#Step 5: Check back through your code and make sure that everything that needs to be an integer or a float, is.
