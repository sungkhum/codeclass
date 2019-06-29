#
# Recursive Merge Sort
# Nathan Wells
#

def mergeSort(list):
    """This recursively splits a list down
    to seperate lists with only one number each
    to prepare the list to be sorted in assending
    order by our helper function.
    """
    if len(list) > 1:
        half = len(list) // 2
        listA = mergeSort(list[:half])
        listB = mergeSort(list[half:])
        newList = mergeHelper(listA, listB)
        return newList
    else:
        return list

def mergeHelper(listA, listB):
    """This is a helper function for mergeSort that 
    sorts and combines two lists recursively.
    """
    if listA == []:
        return listB
    elif listB == []:
        return listA
    elif listA[0] <= listB[0]:
        return [listA[0]] + mergeHelper(listA[1:], listB)
    else:
        return [listB[0]] + mergeHelper(listA, listB[1:])
            


print(mergeSort([1,11,4,5,6,7,3,10,5]))

