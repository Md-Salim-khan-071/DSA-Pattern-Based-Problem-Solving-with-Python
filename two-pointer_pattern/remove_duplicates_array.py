def remove_duplicate(array):
    if len(array)==0:
        return 0
    
    i = 0
    j = 1
    unique = 1   # if arrray is empty it  will already tackled before so unique will always be 1 

    while(j <=  len(array)-1):
        if(array[j] != array[j-1]):
            array[i+1]=array[j]
            i = i+1
            unique = unique+1
            j = j+1 
        else:
            j = j+1 
    
    return unique

array = [2,2,2,3,3,4,5,7,9,9,11]
print(remove_duplicate(array))
