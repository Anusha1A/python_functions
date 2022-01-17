def remove_duplicates(my_list):
	temp_list = []
	for i in my_list:
    		if i not in temp_list:
        			temp_list.append(i)
	my_list = temp_list
	print("List After removing duplicates ", my_list)
my_list = []
n=int(input())
for i in range(n):
	a=int(input())
	my_list.append(a)
print("List Before ", my_list)
remove_duplicates(my_list)