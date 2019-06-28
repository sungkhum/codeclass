def count(pred, l):
    """ Accepts a predicate (pred) and a list (l).
    Returns the number of items in l where pred(l) matches (returns true).
    Recoursion
    """
    temp_number = 0
    if l == []:
        return 0
    
    while len(l) > 0:
        if pred(l[0]) == True:
            temp_number = temp_number + 1
            #print(l[0], 'it is true')
            l = l[1:]
            
            
        else:
            #print(l[0], 'it is not true')
            l = l[1:]
            
    output = temp_number
    output = output + count(pred, l)
    return output



def count(pred, l):
    """ Accepts a predicate (pred) and a list (l).
    Returns the number of items in l where pred(l) matches (returns true).
    List Comprehention
    """
    nl = [i for i in range(0,len(l)) if pred(l[i])]

    return len(nl)


#print(count(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))


def count(pred, l):
    if l == []:
        return 0
    # step
    if pred(l[0]):
        return 1 + count(pred, l[1:])
    else:
        return count(pred, l[1:])

#print(count(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
assert count(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == 2
assert count(lambda x: x % 3 != 0, [1, 2, 3, 4, 5]) == 4

#print(len(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))))
#print(sum(list(map(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))))

def blsort(L):
    """ Accept a binary list L and should return a list 
    with the same elements as L, but in ascending order.
    """
    nl = []
    for i in L:
        if L[i] == 1:
            nl.append(L[i])
        else:
            nl.insert(0, L[i])
    return nl

#print(blsort([0, 1, 1, 0, 1, 0]))


def anythingSort(L):
    """ Accept a list L and should return a list 
    with the same elements as L, but in ascending order.
    """
    return internalSort(L, 0, len(L) - 1)


def merge(A, first, middle, last):
    L = A[first:middle+1]
    R = A[middle+1:last+1]
    L.append(99999999999)
    R.append(99999999999)
    i = j = 0
    for k in range (first, last + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

def internalSort(A, first, last):
    if first < last:
        middle = (first + last) // 2
        internalSort(A, first, middle)
        internalSort(A, middle + 1, last)
        merge(A, first, middle, last)
    return A




print(anythingSort([4, 2, 5, 6, 1]))
