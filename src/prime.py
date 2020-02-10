# Current BigO == O(n)

# x = input("Enter a number: ")

# Actual Final Solution.
# Changed implementation to be a function as suggested by TL,
# also changed the for loop implementation to use not rather than
# to have multiple if/else. This allows me not to have to break the
# loop to get all correct primes.


# def prime(num):
#     for iterator in range(2, int(num**0.5)+1):
#         if not num % iterator:
#             return "Not Prime!"
#     return "Prime!"


# print(prime(int(x)))

# Sieve of Eratosthenes implementation
# Pseudo Code:
# algorithm Sieve of Eratosthenes is
#     input: an integer n > 1.
#     output: all prime numbers from 2 through n.

#     let A be an array of Boolean values, indexed by integers 2 to n,
#     initially all set to true.
#     for i = 2, 3, 4, ..., not exceeding √n do
#         if A[i] is true
#             for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
#                 A[j] := false

#     return all i such that A[i] is true.


def sieve(num):
    # create a boolean array
    # all entries must be true
    # list comprehension:
    prime = [True for i in range(num + 1)]
    # sets the first value to 2
    p = 2
    while (p * p <= num):
        # if prime[p] doesn't change then it's a prime.
        if prime[p] is True:
            # update all multiples of p
            for i in range(p * 2, num + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all Primes
    for p in range(num + 1):
        if prime[p]:
            print(f'Primes related to {num}: {p} \n')


print(sieve(233))
