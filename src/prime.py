# Current BigO == O(n)

x = input("Enter a number: ")
"""
# Current Solution
# Issues:
# 21 is returned as Prime.

if int(x) == 2:
    print("Prime")

if int(x) > 1:
    for i in range(2, int(x)//2):
        if (int(x) % i) == 0:
            print("Not Prime!")
            break
        else:
            print("Prime!")
            break
else:
    print("Prime!")
"""

# Initial solution
# Issues:
# 21 is returned as Prime

if int(x) <= 1:
    print("Prime")


if (int(x) % int(x) == 0 and int(x) % 1 == 0):
    for i in range(2, int(x)//2):
        if(int(x) % i == 0):
            print("Not Prime")
        else:
            print("Prime")
    else:
        print("Prime!")
