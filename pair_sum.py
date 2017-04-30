def pair_sum(list1,num):
	list2 = sorted(list1,reverse=True)
	if (num > (list2[0] + list2[1])):
		return False
	list2 = []
	for i in list1:
		for j,k in enumerate(list1):
			if (i == j):
				continue
			elif ((list1[i] + k) != num):
				continue
			else:
				tup_i = (list1[i],k)
				list2.append(tup_i)
	list2 = list(set(list2))
	for i in list2:
		print(i)

# Run tests
print("Testing pair sum function")
pair_sum([1,3,2,2],4)
print("Running another function")
pair_sum([5,3,4,6,2,7],9)
