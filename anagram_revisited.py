# This program defines multiple solutions for Anagram problem and also tests 
# these solution's using nose.tools.
# Author Sudarsan Devarajulu <sudarsandm@gmail.com>
#
# The first approach is a simple approach which doesn't use dictionaries
def is_anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # Edge case checking
    if len(s1) != len(s2):
        return False

    for letter in s1:
        if s1.count(letter) != s2.count(letter):
            return False
    return True

# The second approach involves a dictionary.
def is_anagram1(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # Edge case checking
    if len(s1) != len(s2):
        return False

    # Populate a dictionary with index as character in s1 and value as its
    # number of repetitions
    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    # De-populate the same dictionary if character in s1 is found in s2.
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    # if any index in count has a non-zero value. If it is then the strings are
    # not anagrams.
    for key in count:
        if count[key] != 0:
            print("{} and {}".format(key, count[key]))
            return False

    return True
        

# Run Tests
print("Testing is_anagram function")
print(is_anagram('go go go','gggoOO'))
print(is_anagram('121','122'))
print("Testing is_anagram1 function")
print(is_anagram1('g   o       d','D  o  G'))
print(is_anagram('12112','122111'))
print(is_anagram1('taylor','Tailor'))
