def lessthanfive(arr):
	x=[i for i in arr if i <5] 
	return(x)
arr = []
n =int(input("Enter size"))
for i in range(0,n):
	a=int(input())
	arr.append(a)
print(lessthanfive(arr))

