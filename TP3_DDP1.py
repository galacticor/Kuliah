semua = {}

def impor(query):
	query = query.replace('IMPOR ','').strip()
	try:
		file = open(query,'r')
		count = 0;
		for baris in file:
			tmp = baris.strip().split(',')
			semua[tmp[0]] = tmp[:]
			count += 1
		print("Terimpor {} baris".format(count))
	except:
		print('{} File tidak ada'.format(query))
	
def ekspor(query):
	query = query.replace('EKSPOR','').strip()
	try:
		file = open(query,'w+')
		count = 0
		for data in semua:
			tmp = semua[data]
			file.write("{},{},{},{}".format(tmp[0],tmp[1],tmp[2],tmp[3]))
			file.write('\n')
			count += 1
		file.close()
		print('Terekspor {} baris'.format(count))
	except:
		print('File tidak ada'.format(query))

def cari_nama(query):
	query = query.replace('CARINAMA','').strip()
	if query == '*':
		for data in semua:
			tmp = semua[data]
			print("{}, {}, {}, {}".format(tmp[0],tmp[1],tmp[2],tmp[3]))	
	elif query in semua:
		tmp = semua[query]
		print("{}, {}, {}, {}".format(tmp[0],tmp[1],tmp[2],tmp[3]))
	else: print("{} tidak ditemukan".format(query))

def cari_tipe(query):
	query = query.replace('CARITIPE ','').strip()
	count = 0
	for data in semua:
		if semua[data][1] == query:
			count += 1
			tmp = semua[data]
			print("{}, {}, {}, {}".format(tmp[0],tmp[1],tmp[2],tmp[3]))
	if count!=0 : print("*Ditemukan {} {}*".format(count,query))
	else: print("{} tidak ditemukan".format(query))

def cari_prov(query):
	query = query.replace('CARIPROV ','').strip()
	count = 0
	for data in semua:
		if semua[data][2] == query:
			count += 1
			tmp = semua[data]
			print("{}, {}, {}, {}".format(tmp[0],tmp[1],tmp[2],tmp[3]))
	if count!=0 : print("*Ditemukan {} {}*".format(count,query))
	else: print("{} tidak ditemukan".format(query))

def tambah(query):
	query = query.replace('TAMBAH ','').strip()
	query = query.split(';;;')
	if len(query) < 4:
		print('Masukkan format TAMBAH yang benar')
	elif query[0] in semua:
		print('{} telah ada'.format(query[0]))
	else:
		semua[query[0]] = query[:]
		print ('{} ditambahkan'.format(query[0]))

def update(query):
	query = query.replace('UPDATE ','')
	query = query.split(';;;')
	if len(query) < 4:
		print('Masukkan format UPDATE yang benar')
	elif query[0] not in semua:
		print('{} belum ada'.format(query[0]))
	else:
		semua[query[0]] = query[:]
		print ('{} diupdate'.format(query[0]))

def hapus(query):
 	query = query.replace('HAPUS ','').strip()
 	try:
 		del semua[query]
 		print("{} telah dihapus".format(query))
 	except:
 		print("{} memang tidak ada".format(query))

def stat():
 	print("Terdapat {} warisan budaya".format(len(semua)))

def stat_tipe():
	dict_tipe = {}
	tipe = []
	for data in semua:
		if semua[data][1] not in dict_tipe:
			dict_tipe[semua[data][1]] = 0
		dict_tipe[semua[data][1]] += 1
	for k,v in dict_tipe.items():
		tipe.append((k,v))
	tipe.sort(key = lambda x: x[1], reverse = True)
	print(tipe)

def stat_prov():
	dict_prov = {}
	prov = []
	for data in semua:
		if semua[data][2] not in dict_prov:
			dict_prov[semua[data][2]] = 0
		dict_prov[semua[data][2]] += 1
	for k,v in dict_prov.items():
		prov.append((k,v))
	prov.sort(key = lambda x: x[1], reverse = True)
	print(prov)

def main():
	while(True):
		print("#"*5)
		query = input("Masukkan perintah : ").strip()
		if 'IMPOR' in query: impor(query)
		elif 'EKSPOR' in query: ekspor(query)
		elif 'CARINAMA' in query: cari_nama(query)
		elif 'CARITIPE' in query: cari_tipe(query)
		elif 'CARIPROV' in query: cari_prov(query)
		elif 'TAMBAH' in query: tambah(query)
		elif 'UPDATE' in query: update(query)
		elif 'HAPUS' in query: hapus(query)
		elif 'STATTIPE' in query: stat_tipe()
		elif 'STATPROV' in query: stat_prov()
		elif 'STAT' == query: stat()
		elif 'cetak' in query: print (semua)
		elif 'KELUAR' in query: 
			print('~Sampai jumpa, jangan lupa mencintai warisan budaya Indonesia!~')
			break
		else:
			print('Masukkan perintah yang benar ')

if __name__ == "__main__":
	print("#"*5)
	print("BudayaKB Lite v1.0")
	print("~Kalau bukan kita yang melestarikan budaya, siapa lagi?~")
	main()
