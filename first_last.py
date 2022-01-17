def first_last(a_list):
    return [a_list[0], a_list[len(a_list)-1]]
arr = []
n =int(input("Enter size"))
for i in range(0,n):
	a=int(input())
	arr.append(a)
print(first_last(arr))


