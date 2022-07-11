def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    char = to_swap.lower()

    flip_str = ""

    for letter in phrase:
        if letter.lower() == char:
            letter = letter.swapcase()
        flip_str += letter

    return flip_str
