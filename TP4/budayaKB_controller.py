#!/usr/bin/env python3
"""

TEMPLATE TP4 DDP1 Semester Gasal 2019/2020

Author: 
Ika Alfina (ika.alfina@cs.ui.ac.id)
Evi Yulianti (evi.yulianti@cs.ui.ac.id)
Meganingrum Arista Jiwanggi (meganingrum@cs.ui.ac.id)

Last update: 23 November 2019

"""
from budayaKB_model import BudayaItem, BudayaCollection
from flask import Flask, request, render_template, redirect, flash
from wtforms import Form, validators, TextField

app = Flask(__name__)
app.secret_key ="tp4"

#inisialisasi objek budayaData
databasefilename = ""
budayaData = BudayaCollection()


#merender tampilan default(index.html)
@app.route('/')
def index():
	return render_template("index.html")

# Bagian ini adalah implementasi fitur Impor Budaya, yaitu:
# - merender tampilan saat menu Impor Budaya diklik	
# - melakukan pemrosesan terhadap isian form setelah tombol "Import Data" diklik
# - menampilkan notifikasi bahwa data telah berhasil diimport 	
@app.route('/imporBudaya', methods=['GET', 'POST'])
def importData():
	if request.method == "GET":
		return render_template("imporBudaya.html")

	elif request.method == "POST":
		f = request.files['file']
		databasefilename=f.filename
		result_impor=budayaData.importFromCSV(f.filename)
		budayaData.exportToCSV(databasefilename) #setiap perubahan data langsung disimpan ke file
		return render_template("imporBudaya.html", result=result_impor, fname=f.filename)

@app.route('/tambahBudaya', methods=['GET', 'POST'])
def tambahData():
	if request.method == "GET":
		return render_template("tambahBudaya.html")

	elif request.method == "POST":
		nama = request.form['nama']
		tipe = request.form['tipe']
		prov = request.form['prov']
		url = request.form['url']
		result_tambah = budayaData.tambah(nama,tipe,prov,url)
		return render_template("tambahBudaya.html",result=result_tambah,name = nama)

@app.route('/ubahBudaya', methods=['GET', 'POST'])
def ubahData():
	if request.method == "GET":
		return render_template("ubahBudaya.html")

	elif request.method == "POST":
		nama = request.form['nama']
		tipe = request.form['tipe']
		prov = request.form['prov']
		url = request.form['url']
		result_ubah = budayaData.ubah(nama.title(),tipe.title(),prov.title(),url)
		return render_template("ubahBudaya.html",result=result_ubah,name = nama)

@app.route('/hapusBudaya', methods=['GET', 'POST'])
def hapusData():
	if request.method == "GET":
		return render_template("hapusBudaya.html")

	elif request.method == "POST":
		nama = request.form['nama']
		result_hapus = budayaData.hapus(nama)
		return render_template("hapusBudaya.html",result=result_hapus,name = nama)

@app.route('/cariBudaya', methods=['GET', 'POST'])
def cariData():
	if request.method == "GET":
		return render_template("cariBudaya.html")

	elif request.method == "POST":
		pilihan = request.form['pilihan']
		masukan = request.form['masukan']
		if pilihan == 'Nama':
			result = budayaData.cariByNama(masukan)
		elif pilihan == 'Tipe':
			result = budayaData.cariByTipe(masukan)
		elif pilihan == 'Prov':
			result = budayaData.cariByProv(masukan)
		return render_template("cariBudaya.html",result=result,pilihan = pilihan,masukan=masukan )

@app.route('/statsBudaya', methods=['GET', 'POST'])
def statData():
	if request.method == "GET":
		return render_template("statBudaya.html")

	elif request.method == "POST":
		pilihan = request.form['pilihan']
		st = ''
		if pilihan == 'All':
			result = budayaData.stat()
		elif pilihan == 'Tipe':
			st = 'Tipe'
			result = budayaData.statByTipe()
		elif pilihan == 'Prov':
			st = 'Asal Provinsi'
			result = budayaData.statByProv()
		return render_template("statBudaya.html",result=result,pilihan = pilihan,st = st)

# run main app
if __name__ == "__main__":
	app.run(debug=True)



