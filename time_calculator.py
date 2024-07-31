def add_time(start, duration):
    
    # Split the start time into hour, minute and period (AM or PM)
    start_time_reformat = start.replace(':', ' ')
    start_time_split = start_time_reformat.split(' ', 4)

    # Split the duration into hour and minute
    duration_split = duration.split(':', 2)
    if int(duration_split[1]) >= 60:
        #return "Error: duration minutes should be less than 60"
        raise ValueError("Error: Duration minutes should be less than 60")
    
    # Add minutes and determine if minutes exceed 60:
    minutes = int(duration_split[1]) + int(start_time_split[1])
    if minutes >= 60:
        minutes_final = minutes - 60
        hour_to_add = 1
    else:
        hour_to_add = 0
        minutes_final = minutes

    if minutes_final == 0 or minutes_final < 10:
        minutes_final = str("0")+ str(minutes_final)
    
    # Converting the hours into military time
    if start_time_split[2] == "PM" and int(start_time_split[0]) < 12:
        start_military_hour = 12 + int(start_time_split[0])
    else:
        start_military_hour = int(start_time_split[0])

    # Adding the hours 
    hour_military = start_military_hour + int(duration_split[0]) + hour_to_add
    
    # Return to 12-hour format
    hour_final = hour_military % 12
    if hour_final == 0:
        hour_final = 12
    
    # Determining the period (AM or PM)
    hour_period = hour_military % 24
    if hour_period <= 12:
        period = "AM"
    if hour_period > 12:
        period = "PM"
    if hour_period == 0:
        period = "AM"


#Uncomment when done with final code:

    #new_time = 0

    #return new_time

# Remove below when done with final code:
add_time('12:00 PM', '15:10')
