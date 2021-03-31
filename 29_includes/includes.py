def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    match = []

    if isinstance(collection, set) or isinstance(collection, dict):
        for val in collection:
            if val == sought:
                match.append(val)
        if match != []:
            print(True)
        if match == []:
            print(False)

    if isinstance(collection, dict):
        for val in collection.values():
            if val == sought:
                match.append(val)
        if match == []:
            print(False)
        if match != []:
            print(True)
        

    if isinstance(collection, tuple) or isinstance(collection, str) or isinstance(collection, list):
        if start == None:
            for val in collection:
                if val == sought:
                    match.append(val)
                    if match != []:
                        print(True)
        if start != None:
            for val in collection[start:]:
                if val == sought:
                    match.append(val)
            if match != []:
                print(True)
            if match == []:
                print(False)
    



    
includes([1, 2, 3], 1)
includes([1, 2, 3], 1, 2)
includes("hello", "o")
includes(('Elmo', 5, 'red'), 'red', 1)
includes({1, 2, 3}, 1)
includes({1, 2, 3}, 1, 3)
includes({"apple": "red", "berry": "blue"}, "blue")