def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase_eval = phrase.lower()
    nu_phrase = phrase_eval.replace(" ", "")
    phrase_reverse = nu_phrase[::-1]

    if phrase_reverse == nu_phrase:
        print(f"{phrase} is a palindrome!")
    else:
        print(f"{phrase} is not a palindrome...") 

is_palindrome('tacocat')
is_palindrome('noon')
is_palindrome('robert')
is_palindrome('taco cat')
is_palindrome('Noon')

    

