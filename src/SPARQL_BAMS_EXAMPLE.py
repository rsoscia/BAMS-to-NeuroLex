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
#foofile = myzipfile.open('bams_ontology_2013-07-10_03-20-00.xml')

#print "printing first 10 lines of the zip file"
#for i, line in enumerate(foofile):
#	if i == 100:
#		break
#	else:
#		print line

#Get a Graph object
g = rdflib.Graph()

print("loading up the BAMS file in memory...")

#pull in an RDF document from NeuroLex, parse, and store.
result = g.parse(file=myzipfile.open('bams_ontology_2013-07-10_03-20-00.xml'), format="application/rdf+xml")

print("going to get results...")

qres = g.query(
    """SELECT ?x ?y ?z
       WHERE {
          ?x ?y ?z.
    	} LIMIT 10""",)
#"birnlex_1489"^^xsd:string

#####################################################################
#could write qres out to a pickle file -- save as a temp file to disk
#####################################################################

print("printing results")

#Search through everything
#for i in qres:
#	print("Definition: %s" %qres.result[i])
# need to append the rows to fix this error

#print("Definition: %s" %qres.result[0])
#not all results are converted during string formatting

print(qres.result[0])
#####################
#######results#######
#loading up the BAMS file in memory...
#going to get results...
#printing results
#(rdflib.term.URIRef(u'http://brancusi1.usc.edu/RDF/conn_3703'), rdflib.term.URIRef(u'http://brancusi1.usc.edu/RDF/description'), rdflib.term.Literal(u'Case pg302. Soma notes p302: we were unable to confirm that flocculus receives afferents from oculomotor & trochlear nuclei. Terminal notes HRP inj sites in 8 aniamls differed slightly btwn cases but each was confined to the margins of flocculus without spilling into PFLv or brainstem.'))





#foofile.close()