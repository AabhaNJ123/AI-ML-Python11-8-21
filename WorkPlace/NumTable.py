# Take a number as input and print multiplication table of that number using while loop.
n = int(input("\nEnter number : "))
print("\nTable of ", n)
i = 0
while i <= 10 :
	print(f"{n} X {i} = {i*n}")
	i += 1