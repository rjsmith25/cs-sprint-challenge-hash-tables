from hashtable import HashTable

def intersection(arrays):
    result = []
    cache = {}
    for array in arrays:
        for number in array:
            if number not in cache:
                cache[number] = 1
            else:
                cache[number] += 1

    for key,value in cache.items():
        if value > 1:
            result.append(key)

    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
