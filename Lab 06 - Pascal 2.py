def make_new_row(lst):
	if lst == []:
		return [1]
	ret = [1]
	for i in range(1,len(lst)):
		ret.append(lst[i] + lst[i-1])
	ret.append(lst[-1])
	return ret

end = False
while not end:
	height_pascal = input("Enter the height of Pascal's triangle in decimal (> 2): ")
	try :
		height_pascal = int(height_pascal)
		if height_pascal <=2 :
			print("Invalid input")
		else:
			end = True
			lst = [1]
			print(lst)
			for i in range(1,height_pascal):
				lst = make_new_row(lst)[:]
				print(lst)
	except ValueError:
		print("Invalid input")
