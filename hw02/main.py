def bsearch(data,target,low,high):
    mid=(int)((high+low)/2)
    print(mid)
    if target==data[mid]:
        return mid
    elif target<data[mid]:
        high=mid-1
        if low==high:
            return none
        else:
            bsearch(data,target,low,high)
    else :
        low=mid+1
        if low==high:
            return none
        else:
            bsearch(data,target,low,high)

print(bsearch([1,2,3,4,6],3,0,4))
