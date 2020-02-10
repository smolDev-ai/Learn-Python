# Current BigO == O(n)

x = input("Enter a number: ")

# Actual Final Solution.
# Changed implementation to be a function as suggested by TL,
# also changed the for loop implementation to use not rather than
# to have multiple if/else. This allows me not to have to break the
# loop to get all correct primes.


def prime(num):
    for iterator in range(2, int(num**0.5)+1):
        if not num % iterator:
            return "Not Prime!"
    return "Prime!"


print(prime(int(x)))
