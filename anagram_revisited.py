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

from nose.tools import assert_equal

class AnagramTest(object):

   def test(self,sol):
      assert_equal(sol('go go go','gggOOO'),True)
      assert_equal(sol('Abc','CBa'),True)
      assert_equal(sol('Abc','CBa'),True)
      assert_equal(sol('hi man','hi   man'),True)
      assert_equal(sol('aabbcc','aabbc'),False)
      assert_equal(sol('123','1 2'),False)
      print("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagram)

    
