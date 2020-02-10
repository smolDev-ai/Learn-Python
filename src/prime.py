# Current BigO == O(n)

x = input("Enter a number: ")

# Actual Final Solution.
# Changed implementation to be a function as suggested by TL,
# also changed the for loop implementation to use not rather than 
# to have multiple if/else. This allows me not to have to break the 
# loop to get all correct primes.


def prime(n):
    for m in range(2, int(n**0.5)+1):
        if not n % m:
            return "Not Prime!"
    return "Prime!"


print(prime(int(x)))
