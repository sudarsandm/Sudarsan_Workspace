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
