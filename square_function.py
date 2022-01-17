def squares(dict_1):
	for i in range(1,21):
		key=i
		dict_1[key]=i**2
	print(dict_1)	
if __name__ == '__main__':
	dict_1 ={}
	squares(dict_1)