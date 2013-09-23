<<<<<<< HEAD
#Unzip_BAMS_Example.py

#For Parsing
import rdflib

#For Unzipping
=======
>>>>>>> 63cc95a608e916092a79c751cf666257d93273f2
import zipfile
from StringIO import StringIO

zipdata = StringIO()

# open the file using a relative path
r = open("../Data/BAMS1.zip")

# zipdata is a buffer holding the contents of the zip file in memory
zipdata.write(r.read())

#myzipfile opens the contents of the zip file as an object that knows how
<<<<<<< HEAD
#to unzip
=======
# to unzip
>>>>>>> 63cc95a608e916092a79c751cf666257d93273f2
myzipfile = zipfile.ZipFile(zipdata)

#grab the contents out of myzipfile by name
foofile = myzipfile.open('bams_ontology_2013-07-10_03-20-00.xml')

print "printing first 10 lines of the zip file"
for i, line in enumerate(foofile):
	if i == 10:
		break
	else:
		print line

<<<<<<< HEAD
#Get a Graph object
g = rdflib.Graph()


#pull in an RDF document from NeuroLex, parse, and store.

#possible options (haven't tested them all):
	#pass the foofile
		#stored as an ZipExtFile
	#pass the myzipfile.open('bams_ontology_2013-07-10_03-20-00.xml') directly
	#pass zipdata
	#pass zipfile.ZipFile(zipdata)

result = g.parse(file=myzipfile.open('bams_ontology_2013-07-10_03-20-00.xml'), format="application/rdf+xml")
print ("graph has %s statements." % len(g))

foofile.close()
=======
foofile.close()
>>>>>>> 63cc95a608e916092a79c751cf666257d93273f2
