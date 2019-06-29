#
# Recursive Merge Sort
# Nathan Wells
#

def mergeSort(list):
	"""This recursively splits a list down
	to seperate lists with only one number each
	to prepare the list to be sorted in assending
	order by our merge function.
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
	sorts and combines two lists
	"""
	mergedList = []
	if listA == [] and listB == []:
		return mergedList
	else:
		if listA == [] and listB != []:
			mergedList.extend(listB[0:])
			return mergedList
		elif listA != [] and listB == []:
			mergedList.extend(listA[0:])
			return mergedList
		elif listA[0] <= listB[0]:
			mergedList.append(listA[0])
			mergedList.extend(mergeHelper(listA[1:], listB))
			return mergedList
		else:
			mergedList.append(listB[0])
			mergedList.extend(mergeHelper(listA, listB[1:]))
			
	return mergedList


print(mergeSort([1,11,4,5,6,7,3,10,5]))

