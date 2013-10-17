#SPARQL_BAMS_Store_Query_Example.py

#Accessing Python Interactive Mode:
#python -i SPARQL_BAMS_Store_Query_Example.py
#This program demonstrates a basic query pulling data out of a persisted SPARQL store

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

qres = g.query(
     """SELECT ?subject ?predicate ?object
       WHERE {
          ?subject ?predicate ?object.
    	} LIMIT 5""")

print("printing results")

#Search through everything
#for i in qres:
#	print("Definition: %s" %qres.result[i])

#print("Name: %s" %qres.result[0])
#TypeError: not all arguments converted during string formatting

print("The graph has " + str(len(g)) + " items in it")

print("Name--not necessarily in string format: ")
print(qres.result[0])




# when done!
#g.close()

##################################################################
##################################################################
#Results from running this program on the BAMS Thesaurus:
##################################################################
#loading up the BAMS file in memory...
#going to get results...
#printing results
#The graph has 22176 items in it
#Name--not necessarily in string format: 
#(rdflib.term.BNode('Ndf48c09cc76f48c2bc02ca3b687a8d06'), 
#rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'), 
#rdflib.term.URIRef(u'file:///anchor'))
##################################################################


##################################################################
##################################################################
##################################################################
##################################################################
#Version 1
#Modified BAMS Query for fixed RDF:
qres = g.query(
     """PREFIX bams: <http://brancusi1.usc.edu/thesaurus/definition/>
       SELECT ?predicate ?object
       WHERE {
          bams:corpora-quadrigemina/ ?predicate ?object.
    	} LIMIT 5""")

for r in qres.result:
    #print str(r[0]), str(r[1])
    
    #added on the object
    print("added on the object")
    print str(r[0]), str(r[1]), str(r[2])


##############################################################################################
##############################################################################################
#Version 2:
#Modified BAMS Query for fixed RDF:
#Instead of this prefix:
#http://brancusi1.usc.edu/thesaurus/
#Using this prefix:
#http://brancusi1.usc.edu/RDF/thesaurus


PREFIX bams: <http://brancusi1.usc.edu/RDF/thesaurus/definition/>



qres = g.query(
     """PREFIX bams: <http://brancusi1.usc.edu/RDF/thesaurus/definition/>
       SELECT ?predicate ?object
       WHERE {
          bams:Basal-ganglia/ ?predicate ?object.
    	} LIMIT 5""")

for r in qres.result:
    #print str(r[0]), str(r[1])
    
    #added on the object
    
    print str(r[0]), str(r[1]), str(r[2])
    
#############################################################################################
#Version 2:
#Modified BAMS Query for fixed RDF:
#Instead of this prefix:
#http://brancusi1.usc.edu/thesaurus/
#Using this prefix:
#http://brancusi1.usc.edu/RDF/thesaurus
http://brancusi1.usc.edu/RDF/thesaurusReference
##################################################

#Not sure if that's even the right description of the modification i'm about to make
#Found the node though for the basal glanglia triple:
#N8b46643d8653451da69a6a73576819d0

#Now inserting it into a query:

qres = g.query(
     """SELECT ?predicate ?object
       WHERE {
          _:N8b46643d8653451da69a6a73576819d0 ?predicate ?object .
    	} LIMIT 5""")

for r in qres.result:
    print str(r[0]), str(r[1])
    
#The above query returned the following:
	#http://www.w3.org/1999/02/22-rdf-syntax-ns#type file:///anchor
	#http://www.w3.org/1999/xlinkhref http://brancusi1.usc.edu/thesaurus/definition/tectum/
	#http://www.w3.org/1999/xlinktype simple
	#http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	#http://brancusi1.usc.edu/RDF/definition N8b830f1c7f6c4002b3384eadd2196373
#############################################################################################
#############################################################################################
#Changing the limit to something >5
#N8b46643d8653451da69a6a73576819d0

qres = g.query(
     """SELECT ?predicate ?object
       WHERE {
          _:N8b46643d8653451da69a6a73576819d0 ?predicate ?object .
    	} LIMIT 50""")

for r in qres.result:
    print str(r[0]), str(r[1])

#############################################################################################
#############################################################################################


#Trying with a new ID
Na88e23a883694760abef4476981f4573

qres = g.query(
     """SELECT ?predicate ?object
       WHERE {
          _:Na88e23a883694760abef4476981f4573 ?predicate ?object .
    	} LIMIT 5""")

for r in qres.result:
    print str(r[0]), str(r[1])
    
#############################################################################################
#############################################################################################
#New Node:
#N8b46643d8653451da69a6a73576819d0

qres = g.query(
     """SELECT ?predicate ?object
       WHERE {
          _:N8b46643d8653451da69a6a73576819d0 ?predicate ?object .
    	} LIMIT 5""")

for r in qres.result:
    print str(r[0]), str(r[1])
    
qres = g.query(
     """SELECT ?predicate ?object
       WHERE {
          ?predicate _:N8b46643d8653451da69a6a73576819d0 ?object .
    	} LIMIT 5""")

for r in qres.result:
    print str(r[0]), str(r[1])
    
qres = g.query(
     """SELECT ?predicate ?object
       WHERE {
          ?predicate ?object _:N8b46643d8653451da69a6a73576819d0 .
    	} LIMIT 5""")

for r in qres.result:
    print str(r[0]), str(r[1])



