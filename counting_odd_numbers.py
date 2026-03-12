# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
odd = 0
for i in range (10):
    nums = int(input("enter you numbers: "))
    if nums % 2 == 1:
        odd += 1
print(odd)
