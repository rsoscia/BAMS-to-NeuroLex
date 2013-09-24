#SPARQL_BAMS_Basal_Ganglia
#This program is used to parse through the BAMS data and figure out everything about "Basal Ganglia"

#For Parsing
import rdflib
from rdflib import plugin

#for getting the length of the files
import os

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
r = open("../Data/BAMS1.zip")

# zipdata is a buffer holding the contents of the zip file in memory
zipdata.write(r.read())

print("~40 seconds for zip to open...")

#myzipfile opens the contents of the zip file as an object that knows how to unzip
myzipfile = zipfile.ZipFile(zipdata)

#grab the contents out of myzipfile by name
foofile = myzipfile.open('bams_ontology_2013-07-10_03-20-00.xml')

#print "printing first 10 lines of the zip file"
#for i, line in enumerate(foofile):
#	if i == len(foofile):
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
     """SELECT DISTINCT ?definition
       WHERE {
          ?cells property:Name "Basal ganglia"^^xsd:string ?definition.
    	}""",)
    #property:Definition
    
    
    
#    """SELECT DISTINCT ?definition
#       WHERE {
#          ?cells bams:name "ganglia"^^xsd:string ?definition.
#    	} LIMIT 10""",)
 
# """SELECT DISTINCT ?definition
#       WHERE {
#          ?cells property:Definition "birnlex_1489"^^xsd:string ?definition.
#    	}""",)

#could write qres out to a pickle file -- save as a temp file to disk

print("printing results")

#Search through everything
#for i in qres:
#	print("Definition: %s" %qres.result[i])

print("Name: %s" %qres.result[0])

print("Name--not necessarily in strign format %s" %qres.result[0])

#myzipfile.close('bams_ontology_2013-07-10_03-20-00.xml')

foofile.close()