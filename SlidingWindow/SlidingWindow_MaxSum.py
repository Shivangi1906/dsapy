def solve(arr,k):
    windowStart=0
    windowSum=0
    maxSum=0
    for windowEnd in range(len(arr)):
        windowSum+=arr[windowEnd]
        if windowEnd>=k-1:
            maxSum=max(maxSum,windowSum)
            windowSum-=arr[windowStart]
            windowStart+=1
    return maxSum

arr=list(map(int,input().split()))
k=4
print(solve(arr,k))
