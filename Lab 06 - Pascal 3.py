def make_new_row(lst):
	if lst == []:
		return [1]
	ret = [1]
	for i in range(1,len(lst)):
		ret.append(lst[i] + lst[i-1])
	ret.append(lst[-1])
	return ret

def oke(height_pascal):
	final = []
	str_final = ['1']
	lst = [1]
	print("\nPrinting the whole list of lists:\n[")
	print(lst)
	for i in range(1,height_pascal):
		lst = make_new_row(lst)[:]
		final.append(lst[:])
		tmp = ''
		for data in lst:
			tmp  = tmp + str(data) + ' '
		tmp = tmp[:-1]
		str_final.append(tmp)
		print(lst)
	print("]")
	print("\nPascal's triangle of height", height_pascal,":")
	for i in range(height_pascal):
		print(' '*(height_pascal-i-1),str_final[i],' '*(height_pascal-i-1))
	

end = False
while not end:
	height_pascal = input("Enter the height of Pascal's triangle in decimal (> 2): ")
	try :
		height_pascal = int(height_pascal)
		if height_pascal <=2 :
			print("Invalid input")
		else:
			end = True
			oke(height_pascal)
	except ValueError:
		print("Invalid input")
