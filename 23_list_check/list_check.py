def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    lists = [item for item in lst if isinstance(item, list)]

    if len(lists) == len(lst):
        print(True)
    else:
        print(False)


list_check([[1], [2, 3]])
list_check([[1], "nope"])