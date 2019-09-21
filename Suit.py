while(1):
	print("Siapa yang menang : ")
	print('a vs b :')
	x = input()
	print('a vs c :')
	y = input()
	print('b vs c :')
	z = input()

	a = 1
	b = 1
	c = 1
	ans = 'valid'
	p = False

	if(x.find('seri')!=-1):
		a = b
		p = True
	elif x.find('a') != -1:
		a = b+1
	else:
		b = a+1

	if(y.find('seri')!=-1):
		c = a
	elif (y.find('a') != -1):
		a = c+1
		if(p):
			b = a
	else:
		c = a+1


		

	if(z.find('seri')!=-1):
		if( c != b):
			ans = 'tidak valid'
		
	elif (z.find('b') != -1):
		if( b == c+1 or b == c-2):
			ans = 'valid'
		else:
			ans = 'tidak valid'
	else:
		if( c == b+1 or c == b-2):
			ans = 'valid'
		else:
			ans = 'tidak valid'

	print(a,b,c)

	if(ans == 'valid'):
		x = ['gunting','batu','kertas','gunting']
		print('a :',x[a-1])
		print('b :',x[b-1])
		print('c :',x[c-1])
	else:
		print(ans)
