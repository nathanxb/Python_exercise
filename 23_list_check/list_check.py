def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    all_lists = True

    for item in lst:
        all_lists = isinstance(item, list)

    return all_lists

    # Alternate answer: use all() with a generator comprehension,
    #
    # return all(isinstance(item, list) for item in lst)
