# This python program is used to list out index number of
# numbers  which equate to a sum. The sum will be part of 
# the list.
import timeit
import sys
list1 = [0,2,3,4,5,6,7,8,9]
sum = int(sys.argv[1])

# check if sum is not part of the list
if(list1.count(sum) == 0):
  exit("value not in the list")
elif sum == min(list1):
  exit("Entered value is the least value")

start = 0
end = len(list1) - 1

index = []
list1.sort()
print(list1)

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
for x in index:
	print(x)
