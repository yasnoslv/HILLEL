list  = [1, 8, 3, 1, 0]

def is_sorted(value):
    if value == sorted(value):
        return True
    else:
        return False

def my_sort(lst):
    if not is_sorted(lst):     
        lastelement = len(lst)-1
        swapped = True
        while swapped == True:
            swapped = False
            for i in range(lastelement):
                if lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                    swapped = True
            lastelement -= 1
    else:
        lst.reverse()
    return lst

print(my_sort(list))


# testing
assert is_sorted([]) == True
assert is_sorted([42]) == True
assert is_sorted([3, 14, 15, 92]) == True
assert is_sorted([1, 1, 1]) == True
assert is_sorted([1, 1, 2, 2, 3, 3, 3]) == True
assert is_sorted([2, 1]) == False
assert is_sorted([1, 2, 1]) == False

assert my_sort([]) == []
assert my_sort([1]) == [1]
assert my_sort([1, 2]) == [2, 1]
assert my_sort([3, 5, 2, 1, 4]) == [1, 2, 3, 4, 5]
assert my_sort([6, 7, 8, 4, 2, 1, 3, 5]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert my_sort([6, 7, 8, 9]) == [9, 8, 7, 6]
assert my_sort([0, 0, 0, 0]) == [0, 0, 0, 0]
assert my_sort([2, 0, 2]) == [0, 2, 2]