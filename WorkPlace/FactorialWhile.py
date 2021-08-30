# Writr a program to find factorial using while loop.
n = int(input("\nEnter number : "))
fact = 1
i = 1
while i <= n :
	fact *= i 
	i += 1
print(f"\n Factorial of {n} is : ", fact)