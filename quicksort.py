def quicksort(sequence):
    x = len(sequence)
    if x <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    items_greater = []
    items_lower = []
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
        
        
        #print (pivot)
    return quicksort(items_lower) + [pivot] + quicksort(items_greater)
    

print(quicksort([1919,2124,31323312,4372]))
