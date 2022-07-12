def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # need to use key:value of num: number of appearances in list
    counter = {}

    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    # need to find the most frequently appearing number
    max_val = max(counter.values())

    # printing the key of whatever has the highest frequency

    for (num, freq) in counter.items():
        if freq == max_val:
            return num
