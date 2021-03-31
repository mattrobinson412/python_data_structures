def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """

    if a > b:
        return f"{a} is greater!"
    if a < b: 
        return f"{b} is greater!"
    if a == b:
        return f"{a} and {b} are equal!"
    

print(number_compare(2, 2))
print(number_compare(4, 2))
print(number_compare(-2, 2))