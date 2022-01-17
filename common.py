def common(arr,arr1):
	print(set(arr).intersection(arr1))
arr = []
n =int(input("Enter size"))
for i in range(0,n):
	a=int(input())
	arr.append(a)
arr1 = []
m =int(input("Enter size"))
for i in range(0,m):
	b=int(input())
	arr1.append(b)
common(arr,arr1)
