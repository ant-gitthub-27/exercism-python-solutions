def find(search_list, value):
    check = 0
    search_list.sort()

    start = 0
    end = len(search_list) - 1
    mid = (start + end)//2

    while start <= end:
        if value == search_list[mid]:
            return mid
            check = 1
        elif value > search_list[mid]:
            start = mid + 1
            mid = (start + end)//2
        else:
            end = mid - 1
            mid = (start + end)//2

    if not check:
        raise ValueError("value not in array")