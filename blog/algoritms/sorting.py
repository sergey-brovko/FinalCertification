def bubble_sort_by_title(posts):
    array = list(posts)
    for i in range(1, len(array)):
        flag = False
        for j in range(0, len(array) - i):
            if array[j].title > array[j+1].title:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True
        if not flag:
            break
    return array

