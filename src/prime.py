# Current BigO == O(n)

x = input("Enter a number: ")

# Final Solution

num = int(x)

# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, num // 2):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if i % num == 0:
            print(num, "is not a prime number")
            break
    print(num, "is not a prime number")
