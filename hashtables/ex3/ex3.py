def intersection(arrays):

    """
    create a results list and nums dictionary

    iterate through all elements in the array,
    count each elements appearance and store in dict

    check if count for an element is equal to number of array within arrays
    - if so, append that element to results list

    terrible run time of O(n**2). Not proud.
    """

    result = []
    nums = dict()

    for array in arrays:
        for element in array:
            if element in nums:
                nums[element] += 1
            else:
                nums[element] = 1

    for key,val in nums.items():
        if val == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
