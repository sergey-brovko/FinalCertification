def binary_search_by_id(posts, x):
    left, right = 0, len(posts) - 1

    while left <= right:
        mid = (left + right) // 2

        if posts[mid].id == x:
            return mid
        elif posts[mid].id < x:
            left = mid + 1
        else:
            right = mid - 1


    return -1