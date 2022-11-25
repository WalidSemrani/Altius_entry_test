# ------------- Walid Semrani Assignment --------- #

def minimum_distance(a):
    # Create a HashMap to
    # store (key, values) pair.
    hmap = dict()
    minimum_distance = 10 ** 9

    # Initialize previousIndex and currentIndex as 0
    previousIndex = 0
    currentIndex = 0

    # Traverse the array an find the minimum distance
    # between the same elements with map
    for i in range(len(a)):

        if a[i] in hmap:
            currentIndex = i

            # Fetch the previous index from map.
            previousIndex = hmap[a[i]]

            # Find the minimum distance.
            minimum_distance = min((currentIndex - previousIndex), minimum_distance)

        # Update the map.
        hmap[a[i]] = i
        # print(hmap[a[i]],end=" ")

    # return minimum distance,
    # if no such elements found, return -1
    if minimum_distance == 10 ** 9:
        return -1
    return minimum_distance


# Driver code
if __name__ == '__main__':
    # Test Case 1:
    f = open("assignment02-2.txt", "r")
    print("\n")
    cases_len = int(f.readline())
    cases = [int(j) for j in f.readline().split()]
    # print(cases_len)
    # print(cases)
    print(-1) if cases_len == 0 else print(minimum_distance(cases))
    # cases = [int(x) for x in f]
    # print(cases)
