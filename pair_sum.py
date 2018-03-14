def pair_sum(arr,num):
        """
        This function returns tuples of elements in a array which sum up to 
        a passed key value.
        """
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
