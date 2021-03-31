def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    if to_swap in phrase:
        swapped = phrase.replace(to_swap, to_swap.swapcase())
        print(swapped)
        

flip_case('Aaaahhh', 'a')
flip_case('Aaaahhh', 'A')
flip_case('Aaaahhh', 'h')