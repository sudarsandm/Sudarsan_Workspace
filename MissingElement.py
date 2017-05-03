# This program is for finding the missing elements between two arrays which has
# all elements same except for one.

def finder(arr1,arr2):
   miss_item = 0
   for item in arr1:
      if (arr2.count(item) == 0):
         miss_item = item
      else:
         continue
      
   if (miss_item == 0):
      return False
   else:
      return miss_item

print(finder([1,4,3,2,5],[1,3,4,5]))
print(finder([7,4,3,2,5],[7,3,2,5]))
