semua = {}

def impor(query):
	query = query.replace('IMPOR ','').strip()
	file = open(query,'r')
	count = 0;
	for baris in file:
		baris = baris[1:-2]
		tmp = baris.split(',')
		semua[tmp[0]] = tmp[:]
		count += 1
	print("Terimpor {} baris".format(count))
	print(semua)

def ekspor(query):
	query = query.replace('EKSPOR ','').strip()
	######

def cari_nama(query):
	query = query.replace('CARINAMA ','').strip()
	tmp = semua[query]
	print("{}, {}, {}, {}".format(tmp[0],tmp[1],tmp[2],tmp[3]))

def cari_tipe(query):
	query = query.replace('CARITIPE ','').strip()
	count = 0
	for data in semua:
		if semua[data][1] == query:
			count += 1
			tmp = semua[data]
			print("{}, {}, {}, {}".format(tmp[0],tmp[1],tmp[2],tmp[3]))
	print("*Ditemukan {} {}*".format(count,query))

def cari_prov(query):
	query = query.replace('CARIPROV ','').strip()
	count = 0
	for data in semua:
		if semua[data][2] == query:
			count += 1
			tmp = semua[data]
			print("{}, {}, {}, {}".format(tmp[0],tmp[1],tmp[2],tmp[3]))
	print("*Ditemukan {} warisan budaya*".format(count,query))

def tambah(query):
	query = query.replace('TAMBAH ','').strip()
	query = query[1:]
	query = query.split(',,,')
	if query[0] in semua:
		print('Data telah ada')
	else:
		semua[query[0]] = query[:]

def update(query):
	query = query.replace('UPDATE ','')
	query = query[1:]
	query = query.split(',,,')
	semua[query[0]] = query[:]

def hapus(query):
 	query = query.replace('HAPUS ','').strip()
 	query = query[1:]
 	try:
 		del semua[query]
 		print("{} dihapus".format(query))
 	except:
 		print("{} memang tidak ada".format(query))

def stat():
 	print("Terdapat {} warisan budaya".format(len(semua)))

def stat_tipe():
 	for data in semua:
 		semua[data]



def main(): 
	while(True):
		query = input().strip()
		if 'IMPOR' in query:
			impor(query)
		elif 'EKSPOR' in query:
			ekspor(query)
		elif 'CARINAMA' in query:
			cari_nama(query)
		elif 'CARITIPE' in query:
			cari_tipe(query)
		elif 'CARIPROV' in query:
			cari_prov(query)
		elif 'TAMBAH' in query:
			tambah(query)
		elif 'UPDATE' in query:
			update(query)
		elif 'HAPUS' in query:
			hapus(query)

if __name__ == "__main__":
        main()
