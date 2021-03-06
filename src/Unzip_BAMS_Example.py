#Unzip_BAMS_Example.py

import rdflib
import zipfile
from StringIO import StringIO


zipdata = StringIO()

#open the file using a relative path
r = open("../Data/BAMS1.zip")

#zipdata is a buffer holding the contents of the zip file in memory
zipdata.write(r.read())

#myzipfile opens the contents of the zip file as an object that knows how

#to unzip
myzipfile = zipfile.ZipFile(zipdata)

#grab the contents out of myzipfile by name
foofile = myzipfile.open('bams_ontology_2013-07-10_03-20-00.xml')

print "printing first 10 lines of the zip file"
for i, line in enumerate(foofile):
	if i == 10:
		break
	else:
		print line

#Get a Graph object
g = rdflib.Graph()

#pull in an RDF document from NeuroLex, parse, and store.
result = g.parse(file=myzipfile.open('bams_ontology_2013-07-10_03-20-00.xml'), format="application/rdf+xml")

#number of statements 
print ("graph has %s statements." % len(g))



foofile.close()