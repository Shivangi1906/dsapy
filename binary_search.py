def binary_search(mylist,target):
    low=0
    high=len(my list)-1
    while low<=high:
        middle=(low+high)//2
        if target==mylist[middle]:
            return middle
        elif target>mylist[middle]:
            low=middle+1
        else:
            high= middle-1
    return-1

print(binary_search([2,3,4,5],10))

