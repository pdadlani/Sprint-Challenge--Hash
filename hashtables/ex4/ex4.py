def has_negatives(a):

    """
    Input: list of integers
    Output: list of integers that have both negative and positive values in the input list

    - iterate through all the negative values in the input list
    - for each negative value, store in a dict where key is the positive value and value is the negative

    - then iterate through each positive element in the input list
    - if the element exists (as a key) in the dict, add the element to results array
    """

    result = []
    nums = dict()

    for num in a:
        if num < 0:
            nums[-num] = num
    
    for num in a:
        if num in nums:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
