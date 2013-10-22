#This is an all encompassing program that does everything at once, hopefully placing all
#of the BAMS query results into a single CSV file
#doesn't run properly unless the path is accessed first, interactive python is activated,
#and the code is pasted into terminal..

#For Parsing
import rdflib
from rdflib import plugin

#for getting the length of the files
import os

#for working with tempfiles
import os.path as op
import tempfile

#For Unzipping
import zipfile
from StringIO import StringIO

plugin.register(
    'sparql', rdflib.query.Processor,
    'rdfextras.sparql.processor', 'Processor')
plugin.register(
    'sparql', rdflib.query.Result,
    'rdfextras.sparql.query', 'SPARQLQueryResult')

zipdata = StringIO()

# open the file using a relative path
#r = open("../Data/BAMS1.zip")

# adding the BAMS Thesaurus instead of the more limited set of data:
#r = open("../Data/bams_thesaurus_2013-09-24_17-12-40.xml.zip")
# Fixed RDF
#r = open("../Data/bams_thesaurus_2013-10-06_14-58-56.xml.zip")
#ADDITIONAL CONTENT
r = open("../Data/bams_ontology_2013-10-16_20-34-52.xml.zip")

# zipdata is a buffer holding the contents of the zip file in memory
zipdata.write(r.read())

print("~40 seconds for zip to open...")

#myzipfile opens the contents of the zip file as an object that knows how to unzip
myzipfile = zipfile.ZipFile(zipdata)

#grab the contents out of myzipfile by name
#foofile = myzipfile.open('bams_ontology_2013-07-10_03-20-00.xml')

#changing the foofile to be the file we upen above^^^^^ in r = open()....etc.
#foofile = myzipfile.open('bams_thesaurus_2013-09-24_17-12-40.xml')
# Fixed RDF
#foofile = myzipfile.open('bams_thesaurus_2013-10-06_14-58-56.xml')
#ADDITIONAL CONTENT
foofile = myzipfile.open('bams_ontology_2013-10-16_20-34-52.xml')

print("loading up the BAMS file in memory...")

#Get a Graph object using a Sleepycat persistent store
g = rdflib.Graph('Sleepycat',identifier='BAMS')

# first time create the store
#  put the store in a temp directory so it doesn't get confused with stuff we should commit
tempStore = op.join( tempfile.gettempdir(), 'myRDF_BAMS_Store')
g.open(tempStore, create = True)

#pull in the BAMS RDF document, parse, and store.
#result = g.parse(file=myzipfile.open('bams_ontology_2013-07-10_03-20-00.xml'), format="application/rdf+xml")

#do the same thing but with the BAMS thesaurus file
#result = g.parse(file=myzipfile.open('bams_thesaurus_2013-09-24_17-12-40.xml'), format="application/rdf+xml")
# Fixed RDF
#result = g.parse(file=myzipfile.open('bams_thesaurus_2013-10-06_14-58-56.xml'), format="application/rdf+xml")
#ADDITIONAL CONTENT
result = g.parse(file=myzipfile.open('bams_ontology_2013-10-16_20-34-52.xml'), format="application/rdf+xml")

foofile.close()

# when done!
g.close()

print("Graph stored to disk")

#WORKS PERFECTLY
#########################################################################################

#For Parsing
import rdflib
from rdflib import plugin

#for getting the length of the files
import os

#for working with tempfiles
import os.path as op
import tempfile

plugin.register(
    'sparql', rdflib.query.Processor,
    'rdfextras.sparql.processor', 'Processor')
plugin.register(
    'sparql', rdflib.query.Result,
    'rdfextras.sparql.query', 'SPARQLQueryResult')

#Get a Graph object
g = rdflib.Graph('Sleepycat',identifier='BAMS')

print("loading up the BAMS file in memory...")

# assumes myRDF_BAMS_Store has been created
tempStore = op.join( tempfile.gettempdir(), 'myRDF_BAMS_Store')
g.open(tempStore)

print("going to get results...")


print("The graph has " + str(len(g)) + " items in it")

#additional BAMS content (graph) has 167178 items in it

#BASAL GANGLIA OF TELENCEPHALON QUERY:
qres = g.query(
	 """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
	   SELECT ?subject ?predicate ?object
	   WHERE {
		  ?subject bamsProp:entry "Basal ganglia of telencephalon" .
		  ?subject ?predicate ?object
		}""")

for r in qres.result:
	print str(r[0]), str(r[1]), str(r[2])


#BASAL GANGLIA QUERY:
qres = g.query(
	 """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
	   SELECT ?subject ?predicate ?object
	   WHERE {
		  ?subject bamsProp:entry "Basal ganglia" .
		  ?subject ?predicate ?object
		}""")

for r in qres.result:
	print str(r[0]), str(r[1]), str(r[2])


#BASAL NUCLEI QUERY:
qres = g.query(
	 """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
	   SELECT ?subject ?predicate ?object
	   WHERE {
		  ?subject bamsProp:entry "Basal nuclei" .
		  ?subject ?predicate ?object
		}""")

for r in qres.result:
	print str(r[0]), str(r[1]), str(r[2])


import csv

for r in qres.result:
	#print str(r[0]), str(r[1]), str(r[2])
	c = csv.writer(open("temp.csv","wb"))
	
	# gives us the triple info in each cell (notice it's not in string format) it's pretty ugly
	#c.writerow(qres.result)
	# regardless of the format, i'm going to index this first
	# figure out how to place at the next 
	
	# need to access each individual part of the triple
	# making row plural allows for this type of functionality
	
	c.writerows(qres.result)
	

