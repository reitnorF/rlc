import web
import pickle

#Store all ontology node
global ontologyDatabase
ontologyDatabase = dict()

def loadDatabase():
	global ontologyDatabase
	with open('ontologyStorage','rb') as f:
		ontologyDatabase = pickle.load(f)

def endTransaction():
	global ontologyDatabase
	with open('ontologyStorage','wb') as f:
		pickle.dump(ontologyDatabase,f)

def showAllOntologyNode():
	global ontologyDatabase
	for i in ontologyDatabase:
		print str(i) + "---->" + str(ontologyDatabase[i])
		print ""

def addNewNodeBySourceCode(sourcecode):
	global ontologyDatabase
	data = sourcecode
	nodeOntology = dict()
	parsedNodeSourceCode = data.splitlines()
	nodeOntology["key"] = parsedNodeSourceCode[0]
	for x in range(1,len(parsedNodeSourceCode)):
		nodeOntology[x] = parsedNodeSourceCode[x]
	ontologyDatabase[nodeOntology["key"]] = nodeOntology
	endTransaction()


urls = (
	'/','index',
	'/dataGateway','dataGateway'
	)

class index:
	def GET(self):
		render = web.template.render('pytemplate')
		return render.index(ontologyDatabase)

class dataGateway:
	def POST(self):
		data = web.data()
		addNewNodeBySourceCode(data)
		return data

loadDatabase()





if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
