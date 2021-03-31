def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    titlemaker = phrase.title()
    print(titlemaker)


titleize('this is awesome')
titleize('oNLy cAPITALIZe fIRSt')
