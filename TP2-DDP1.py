import string
import numpy as np
import matplotlib.pyplot as plt

teks = []
lst_kata = []
lst_freq = []
stopwords = []
lst_final = []

# Input stopwords yaitu kata-kata yang tidak boleh ada atau diabaikan
def input_stopwords():
	File = open("stopWords.txt", "r")
	stopwords = []
	for words in File:
		stopwords.append(words.strip())
	File.close()
	return stopwords

# Input kata-kata dalam file text
def input_data(file):
	teks = ''
	for baris in file:
		teks = teks + ' ' + baris.strip()
	teks = teks.split()
	return teks

# Buang tanda baca atau punctuation yang seharusnya diabaikan
def buang_tanda(teks):
	ret_teks = []
	kata_baru = ''
	for kata in teks:
		kata_baru = kata
		for char in string.punctuation:
			kata_baru = kata_baru.replace(char,"")
		ret_teks.append(kata_baru.lower())
	return ret_teks

# Menghitung frequensi kemunculan kata untuk setiap kata di dalam teks
def hitung_freq(teks):
	for kata in teks:
		if len(kata) > 0 and kata not in stopwords:
			idx = -1
			for i in range(len(lst_kata)):
				if kata == lst_kata[i]:
					idx = i
					break
			if idx == -1:
				lst_kata.append(kata)
				lst_freq.append(1)
			else:
				lst_freq[idx] += 1

# Fungsi untuk mencetak tabel max 36 list of words
def print1():
        lebar_freq = max(len(str(data[0])) for data in lst_final) + 1
        lebar_kata = max(len(data[1]) for data in lst_final) + 16
        print()
        print(f"{len(lst_final)} words in frequency order as (count:word) pairs")
        print()
        for i in range(len(lst_final)):
                count = lst_final[i][0]
                word = lst_final[i][1]
                print(f"{count}".rjust(lebar_freq), f"{word}".ljust(lebar_kata), sep=":", end="")
                if i%2 == 1:
                        print()
        if (len(lst_final)%2 == 1):
                print()
    
print("Create word frequency table and bar chart from a text file")
print("----------------------------------------------------------")
file_name = input("Please enter the file name: ")
#   JokoWidodoSpeechAPEC2014.txt
#   CommencementSpeechByGates2014.txt


File = open(file_name,'r')
stopwords = input_stopwords()
teks = input_data(File)
teks = buang_tanda(teks)
hitung_freq(teks)
File.close()

# Masukkan ke dalam tuple agar bisa disort
for i in range(len(lst_kata)):
    lst_final.append((lst_freq[i],lst_kata[i]))

# Sort secara terbalik berdasarkan index 1 atau frequensi
lst_final.sort(reverse = True)
if len(lst_final)>36:
    lst_final = lst_final[:36]
print1()
# Sort secara terbalik berdasarkan index 2 atau abjad
lst_final.sort(key = lambda x : x[1],reverse = True)

lst_kata = []
lst_freq = []
# Copy dari list of tuple ke dalam list untuk dicetak dalam matplotlib
for i in range(len(lst_final)):
	lst_kata.append(lst_final[i][1])
	lst_freq.append(lst_final[i][0])

lebar = 0.75
# bikin list arrange
banyakBar = np.arange(len(lst_kata))
# set bar untuk horizontal
plt.barh(banyakBar, lst_freq,lebar)
# atur label y axis 
plt.yticks(banyakBar, lst_kata)
# atur nama label x
plt.xlabel('Frequency')
# atur judul
plt.title('Top 36 Words in Alphabetical Order')
# show the figure
plt.show()
input ("Please type Enter to exit ...")
