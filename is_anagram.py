"""
This is a function to check if the entered pair of strings are anagram or not.

"""
def is_anagram(s1,s2):
	s1 = s1.replace(' ','').lower()
	s2 = s2.replace(' ','').lower()
	
	if(len(s1) != len(s2)):
		return False
	for x in s1:
		if (s1.count(x) != s2.count(x)):
			return False
	else:
		return True
		
print("Test code runs here...\n")
print(is_anagram('S  i  Ri','I r    iS'))