def pair_sum(arr,num):
	# check if the number entered is much bigger than the elements of the list
	list1 = sorted(arr,reverse=True)
	if ((list1[0] + list1[1]) < num):
		return False
	# Check if the array entered has atleast 2 elements
	if (len(arr) < 2):
		return False
	# Declare two sets : seen for elements not summing up to num
	# output is another set in which we push the elements which sum up to num
	seen = set()
	output = set()
	
	for i in arr:
		target = num - i
		if target not in seen:
			seen.add(i)
		else:
			output.add((min(i,target),max(i,target)))
	return list(output)
# Run tests
print("Testing pair sum function")
print(pair_sum([1,3,2,2],4))
print("Running another function")
print(pair_sum([5,3,4,6,2,7],9))
