def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    U:
    fill a package to its limit from a list of items with weights

    a package can not weigh more than limit. 
    find two items that sum = limit
    higher value index should be in 0 index and lower in 1
    if pair doesn't exist for inputs, then return none
    solution linear time
    Hash tables are perfect for when you need to map from one thing to another thing, usually to be able to look something up.
    return the index of the item in list, not the weight
    P: each weight in weights is the key
        each weight index is value
        find two items that equal limit
        return tuple sorted by higher value 0 lower value 1
    """
    # Your code here
    cache = {}
    index = 0

    # while index is less than length
    while index < length:
        # check if values in cache
        if (limit - weights[index]) not in cache:
            # so if the value of the limit-weight is not in cache, then it will not pair
            cache[weights[index]] = index
            index += 1
        else:
            return [index, cache[limit-weights[index]]]
    return None
