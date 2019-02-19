import pickle
import re
import web
import csv


class TA:
	def __init__(self,judul,penulis,pembimbing):
		self.judul = judul
		self.pembimbing = pembimbing
		self.penulis = penulis

class Buku:
	def __init__(self,judul,penulis,penerbit,kode):
		self.judul = judul
		self.penulis = penulis
		self.penerbit = penerbit
		self.kode = kode


allOfTA = dict()
allOfBook = dict()

with open ('TA','rb') as f:
	TAdb = pickle.load(f)

listOfBook = list()
with open ("senayan_biblio_export.csv","rb") as csvfile:
	reader = csv.reader(csvfile, delimiter=',',quotechar='"')
	for row in reader:
		listOfBook.append(row)

counter = 1  
for i in listOfBook:
	allOfBook[counter] = Buku(i[0],i[15],i[4],i[8])
	counter += 1


'''
for i in allOfBook:
	print allOfBook[i].penulis
'''


'''
for i in TAdb:
	judul = i["judul"]
	if judul is not None:
		judul = judul.encode("ascii","ignore")

for i in TAdb:
	if i["pembimbing"] is not None:
		pembimbing = i["pembimbing"]
		judul = i["judul"]
		if re.search("\n",pembimbing):
			a = re.split("\n",pembimbing)
		else:
			a = re.split("\s{3,}",pembimbing)
		b = list()
		for y in a:
			if len(y) > 0:
				b.append(y)
		kodebuku = i["kodebuku"]
		penulis = i["penulis"]
		allOfTA[kodebuku] = TA(judul,penulis,b)


'''



urls = (
	'/','index',
	'/search/(.+)','search',
	'/topik','topik',
	'/domain','domain',
	'/umum','umum',
	'/tokohislam','tokohislam'
	)

class index:
	def GET(self):
		render = web.template.render('templates')
		return render.viewtemplate(allOfBook)

class search:
	def GET(self,squery):
		TAQueryResult = dict()
		for i in allOfBook:
			judulBuku =  allOfBook[i].judul
			if judulBuku is not None:
				squeryUP = squery.upper()
				judulBukuUP = judulBuku.upper()
				if re.search(squeryUP,judulBukuUP):
					TAQueryResult[i] = allOfBook[i]
		render = web.template.render('templates')
		return render.viewtemplate(TAQueryResult)

class topik:
	def GET(self):
		render = web.template.render('templates')
		return render.topictemplate(allOfTA)
class domain:
	def GET(self):
		render = web.template.render('templates')
		return render.domaintemplate(allOfTA)
class umum:
	def GET(self):
		render = web.template.render('templates')
		return render.umumtemplate(allOfTA)
class tokohislam:
	def GET(self):
		render = web.template.render('templates')
		return render.tokohislamtemplate(allOfTA)



if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
