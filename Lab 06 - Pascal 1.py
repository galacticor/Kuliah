def make_new_row(lst):
	if lst == []:
		return [1]
	ret = [1]
	for i in range(1,len(lst)):
		ret.append(lst[i] + lst[i-1])
	ret.append(lst[-1])
	return ret

lst = []
print(make_new_row(lst))
