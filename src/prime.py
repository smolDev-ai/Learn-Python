# Current BigO == O(n)

x = input("Enter a number: ")

# Actual Final Solution.

def prime(n):
    for m in range(2, int(n**0.5)+1):
        if not n % m:
            return "Not Prime!"
    return "Prime!"


print(prime(int(x)))
