def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """

    weekday_names = [
        'Sunday', 
        'Monday', 
        'Tuesday', 
        'Wednesday', 
        'Thursday', 
        'Friday', 
        'Saturday']
    
    if day_of_week < 1 or day_of_week > 7:
        return 'None! Sowwy.'

    if day_of_week == 1:
        print(weekday_names[0])
    if day_of_week == 2:
        print(weekday_names[1])
    if day_of_week == 3:
        print(weekday_names[2])
    if day_of_week == 4:
        print(weekday_names[3])
    if day_of_week == 5:
        print(weekday_names[4])
    if day_of_week == 6:
        print(weekday_names[5])    
    if day_of_week == 7:
        print(weekday_names[6])



print(weekday_name(1))
print(weekday_name(2))
print(weekday_name(8))



    