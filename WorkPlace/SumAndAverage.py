# Take input from user and find out sum and average of 0 to that number.

i =0
sum = 0
n = int(input("\nEnter number : "))
while i <= n :
	sum+= i
	i += 1
print(f"\nSum of numbers from 0 to {n} = {sum} ")
print(f"\nAverage of numbers from 0 to {n} = {sum/n}\n")
