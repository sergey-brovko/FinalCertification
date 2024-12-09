def binary_search_by_id(data, x):
    result = []
    posts = list(data)
    left, right = 0, len(posts) - 1

    while left <= right:
        mid = (left + right) // 2

        if posts[mid].id == x:
            result.append(posts[mid])
            return result
        elif posts[mid].id < x:
            left = mid + 1
        else:
            right = mid - 1

