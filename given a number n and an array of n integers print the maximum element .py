def largest(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
        return max
arr=[2,10]
n=len(arr)
ans=largest(arr,n)
print("largest in given array is",ans)
