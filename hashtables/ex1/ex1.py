def get_indices_of_item_weights(weights, length, limit):

    """
    Input: given a list of weights in a python list, with length of the list, and limit for what can be held
    Output: list with indices of weights that add to limit, greater index listed first
    - only two items in this output

    - add each weight as a key, with the complimentary value that could add to the limit
    - check if that value is in the list
    - if so, return a tupe, with the number of greater index in the weights list placed in 0th index of return list
    - edge cases of where there are 2 or less elements in the weights tuple
    """

    # if there are less than 2 elements in weights list
    if length < 2:
        return None
    # if there are exactly two elements in the weights
    if length == 2 and sum(weights) == limit:
        return [1, 0]
    elif length == 2:
        return None

    # if there are more than 2 elements in the weights list
    nums_dict = dict()
    ans = []

    for i, weight in enumerate(weights):
        value = limit - weight
        nums_dict[weight] = (i, value)

    for weight in nums_dict:
        if nums_dict[weight][1] in nums_dict:
            ans.append(nums_dict[weight][0])

    ans.sort(reverse=True)
    return ans
