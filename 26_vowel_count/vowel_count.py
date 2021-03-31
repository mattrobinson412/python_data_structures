def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phraze = phrase.lower()
    vowels = 'aeiou'
    vowel_chart = {}

    for vowel in vowels:
        vc = phraze.count(vowel)
        if vc >= 1:
            vowel_chart.update( {vowel: vc} )
    
    print(vowel_chart)


vowel_count('rithm school')
vowel_count('HOW ARE YOU? i am great!')