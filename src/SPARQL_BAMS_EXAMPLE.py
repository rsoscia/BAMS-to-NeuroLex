#SPARQL_BAMS_EXAMPLE.py

#For Parsing
import rdflib

#For Unzipping
import zipfile
from StringIO import StringIO
from rdflib import plugin

plugin.register(
    'sparql', rdflib.query.Processor,
    'rdfextras.sparql.processor', 'Processor')
plugin.register(
    'sparql', rdflib.query.Result,
    'rdfextras.sparql.query', 'SPARQLQueryResult')

zipdata = StringIO()

# open the file using a relative path
r = open("../Data/BAMS1.zip")

# zipdata is a buffer holding the contents of the zip file in memory
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

qres = g.query(
    """SELECT DISTINCT ?Defn
       WHERE {
          ?cells property:Name"nervous-system-2"^^xsd:string ?Defn.
    	}""",)
#"birnlex_1489"^^xsd:string

#Search through everything
for i in qres:
	print("Definition: %s" % qres.result[i])


foofile.close()