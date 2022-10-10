def binarysearch(lst,l,h,key):
    if l<=h:
        mid=(l+h)//2
        if lst[mid]==key:
            return mid
        elif lst[mid]<key:
            return binarysearch(lst,mid+1,h,key)
        else:
            return binarysearch(lst,mid-1,h,key)
        return-1
lst=[]
n=int(input("Enter the size "))
for i in range(n):
    e=int(input("enter element:"))
    lst.append(e)
    lst=sorted(lst)
print(lst)
l=0
h=len(lst)-1
key=int(input("enter elements to be searched:"))
res=binarysearch(lst,l,h,key)
if res==-1:
    print("enter element is not found")
else:
    print("element found at:",res)