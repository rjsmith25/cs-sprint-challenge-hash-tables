from hashtable import HashTable


def get_indices_of_item_weights(weights, length, limit):
    hashtable = HashTable(length)

    for i in range(length):
        hashtable.put(str(weights[i]), i)

    for i, w in enumerate(weights):
        difference = limit - w
        exist = hashtable.get(str(difference))
        if exist:
            if weights[max(i, exist)] + weights[min(i, exist)] == limit:
                return (max(i, exist), min(i, exist))

    return None
