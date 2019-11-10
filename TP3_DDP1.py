import csv

semua = {}

def impor(query):
	query = query.replace('IMPOR ','').strip()
	file = open(query,'r')
	count = 0;
	query = query.split()
	for baris in file:
		semua[query[0]] = query[1:]
		count += 1
	print("Terimpor {} baris".format(count))

def ekspor(query):
	query = query.replace('EKSPOR ','').strip()

def cari_nama(query):
	query = query.replace('CARINAMA ','').strip()
	tmp = semua[query]
	print(tmp[0],tmp[1],tmp[2],tmp[3], sep = ',')

def cari_tipe(query):
	count = 0
	for data in semua:
		if semua[data][1] == tipe:
			count += 1
			tmp = semua[data]
			print(tmp[0],tmp[1],tmp[2],tmp[3], sep = ',')
	print("*Ditemukan")

def cari_prov(query):


def main():
	while(True):
		query = input().strip()
		if 'IMPOR' in query:
			impor()
		elif 'EKSPOR' in query:
			ekspor()
		elif 'CARINAMA' in query:
			carinama()
		elif 'EKSPOR' in query:
			ekspor()
		elif 'EKSPOR' in query:
			ekspor()
		elif 'EKSPOR' in query:
			ekspor()
