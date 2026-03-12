# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

difference = int(input("Enter you First number: "))
sum = 0

for i in range(9):
    num =int(input("Enter the 9 numbers: "))
    sum = num + sum

print(difference-sum)