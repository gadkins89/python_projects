"""
5.16 LAB: Output range with increment of 5

Write a program whose input is two integers. Output the first integer and subsequent
increments of 5 as long as the value is less than or equal to the second integer.
Ex: If the input is:
-15
10
the output is:
-15 -10 -5 0 5 10 
Ex: If the second integer is less than the first as in:
20
5
the output is:
Second integer can't be less than the first.
For coding simplicity, output a space after every integer, including the last.
"""

print("This program will count by 5's between two integers of your choice as long as the second integer is larger than the first.\n ")

int_1 = int(input("Please enter a number. "))
int_2 = int(input("Please enter a second number. "))

if int_1 > int_2:
    print("Second integer can't be less than the first. ")

while int_1 <= int_2:
    print(f"{int_1}" + " ", end=" ")
    int_1 += 5
print()
