def factorial(n): 
	if (n==1 or n==0):
		return 1
	else:
		n*factorial(n - 1)
	return 0
num =int(input())
print("Factorial of",num,"is", factorial(num))