# Current BigO == O(n)

x = input("Enter a number: ")

if (int(x) % int(x) == 0 and int(x) % 1 == 0):
    if (int(x) % 2 == 0 or int(x) % 5 == 0):
        if(int(x) == 2 or int(x) == 5):
            print("Prime!")
        else:
            print("Not Prime!")
    else:
        print("Prime!")
