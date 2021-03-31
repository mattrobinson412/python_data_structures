def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str1 = str(num1)
    str2 = str(num2)

    if len(str1) == len(str2):
        print(True)
    else:
        print(False)


same_frequency(551122, 221515)
same_frequency(321142, 3212215)
same_frequency(1212, 2211)