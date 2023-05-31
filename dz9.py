# og list
animals = ["cat", "lion", "parrot", "bird", "toucan", "mouse", "dog", "leoprad", "cow"]
# print og list to see the difference later
print(animals)
# make a function with a later said value
def swap(list):
    # variable that controls while later on
    swapped = True
    # changeable varibales to set range when sorting
    left = 0
    right = len(list)-1
    # start loop
    while swapped:
        # prevent loop from starting, unless swapped = True again
        swapped = False
        # checking elements from left to right in the specified range
        for i in range(left, right):
            # if left element of list has more symbols than the one after
            if len(list[i]) > len(list[i+1]):
                # they swap places
                list[i], list[i+1] = list[i+1], list[i]
                # to start the loop again when the time comes
                swapped = True
        # make range smaller
        right -= 1
        # checking elements from right to left in the specified range, but with step -1 so it counts back instead of forward
        for i in range(right, left, -1):
            # if right element of list has more symbols than the one before
            if len(list[i]) < len(list[i-1]):
                # swap
                list[i], list[i-1] = list[i-1], list[i]
                # make sure the loop starts next time
                swapped = True
        # make range smaller
        left += 1
    # reset ranges for next check
    left = 0
    right = len(list)-1
    # repeat 10 times incase there are more that 1 similar letters
    for i in range(10):
        # checking elements from left to right
        for i in range(left, right):
            # if length of the element on the left = length of the one after
            if len(list[i]) == len(list[i+1]):
                # sort by abc and store in a temporary list to then switch them to the og
                templist = sorted([list[i], list[i+1]])
                # switch the right elements to the og list
                list[i], list[i+1] = templist[0], templist[1]
    # print the result
    print(list)
    
# complete function
swap(animals)