"""
This is a lambda function for checking if a given number is prime or not.

"""
is_prime = lambda x : all (x%y != 0 for y in range(2,x))

## Testing the above function.
print(is_prime(17))
print(is_prime(21))
print(is_prime(19))
