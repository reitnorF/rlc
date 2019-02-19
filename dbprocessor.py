import csv

listOfBook = list()
with open ("senayan_biblio_export.csv","rb") as csvfile:
	reader = csv.reader(csvfile, delimiter=',',quotechar='"')
	for row in reader:
		listOfBook.append(row)

listOfJudul = list()


for i in listOfBook:
	print i
	#print i[8] + i[0]




'''
judul : 0
penerbit : 4
kode : 8
penulis : [15]
'''

