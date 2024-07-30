def add_time(start, duration):
    
    #Split the start time into hour, minute and period (AM or PM)
    start_time_reformat = start.replace(':', ' ')
    start_time_split = start_time_reformat.split(' ', 3)

    #Split the duration into hour and minute
    duration_split = duration.split(':', 2)
    if int(duration_split[1]) >= 60:
        #return "Error: duration minutes should be less than 60"
        raise ValueError("Error: Duration minutes should be less than 60")
    

    #Add minutes and determine if minutes exceed 60:
    minutes = int(duration_split[1]) + int(start_time_split[1])
    if minutes >= 60:
        minutes_final = minutes - 60
        hour_to_add = 1
    else:
        hour_to_add = 0
        minutes_final = minutes
    
    #Adding hours and determining correct period

    hour = int(start_time_split[0]) + int(duration_split[0]) + hour_to_add
    hour_final = hour % 12
    cycles_split = str(hour/12).split('.', 2)
    cycles_whole = int(cycles_split[0])
    
    if int(start_time_split[0])<12:
        if cycles_whole % 2 == 0:
            period = start_time_split[2]
        if cycles_whole % 2 == 1:
            if start_time_split[2] == "PM":
                period = "AM"
            if start_time_split[2] == "AM":
                period = "PM"
    
    else:
        if cycles_whole % 2 == 1:
            period = start_time_split[2]
        
        if cycles_whole % 2 == 0:
            if start_time_split[2] == "PM":
                period = "AM"
            if start_time_split[2] == "AM":
                period = "PM"

# Next step is to add the days

    #Print final time to check
    print(f"Start Time: {start}\nDuration: {duration}\nCycles remainder: {cycles_whole%2} \nFinal Time: {hour_final}:{minutes_final} {period}" )


#Uncomment when done with final code:

    #new_time = 0

    #return new_time

# Remove below when done with final code:
add_time('12:00 PM', '15:10')
