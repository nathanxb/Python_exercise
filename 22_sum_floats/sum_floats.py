def sum_floats(nums):
    """Return sum of floating point numbers in nums.

        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9

        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!

    total = 0

    for num in nums:
        if isinstance(num, float):
            total = total + num

    return total

    # -----One Line Version-----
    # return sum([num for num in nums if isinstance(num, float)])

    # this one line utilizes the built in sum function of Python
