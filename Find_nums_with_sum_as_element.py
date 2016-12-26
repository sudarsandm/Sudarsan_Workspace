import timeit
list1 = [0,2,3,4,5,6,7,8,9]
sum = int(input("Enter the sum to found:"))
start = 0

if(sum < int(max(list1))):
   end = int(max(list1)/2) + 1
else:
    end = len(list1) - 1

index = []
list1.sort()

while(start <= end):
    base = start + 1
    while(base <= end):
        if((list1[base] + list1[start]) == sum):
            index.append(base)
            index.append(start)
            base += 1
        else:
            base += 1
    start += 1
    

    
    
    
