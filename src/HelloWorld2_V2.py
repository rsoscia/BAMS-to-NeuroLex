import rdflib
from rdflib import plugin


plugin.register(
    'sparql', rdflib.query.Processor,
    'rdfextras.sparql.processor', 'Processor')
plugin.register(
    'sparql', rdflib.query.Result,
    'rdfextras.sparql.query', 'SPARQLQueryResult')

#Get a Graph object
g = rdflib.Graph()
# pull in an RDF document from NeuroLex, parse, and store.
result = g.parse("http://neurolex.org/wiki/Special:ExportRDF/birnlex_1489", format="application/rdf+xml")

#Ask a specific question about that RDF document
qres = g.query(
    #"""SELECT DISTINCT ?b
    #   WHERE {
    #      ?a property:Definition ?b .
    #   }""",
       
       
    """SELECT DISTINCT ?b
       WHERE {
          ?a property:Authors ?b .
       }""",
    
    #initNs=dict(
     #   property=rdflib.Namespace("http://neurolex.org/wiki/Special:URIResolver/Property-3A"),
     #   wiki=rdflib.Namespace("http://neurolex.org/wiki/Special:URIResolver/")))
	
	)
	
	
	
#Lines 38-47 are for the Definition Query:
#print("QRES: %s " %qres.result)

#print statement below is connected to the exported RDF about "birnlex_1489"
#print("Length: %s" % len(g))


#print("Description: %s" % qres.result[0])
#Description: Part of the rhombencephalon that lies in the posterior cranial fossa behind the brain stem, consisting of the cerebellar cortex, deep cerebellar nuclei and cerebellar white matter.
#A portion of the brain that helps regulate posture, balance, and coordination. (NIDA Media Guide Glossary)


#Lines 50- are for the authors query:
#Below print statement prints both authors
#print("qres: %s " %qres.result)

#Below print statement prints the author at positon zero.. but it's backwards for some reason...
#maybe the parser messes with that.
#print("Author: %s " %qres.result)
print("Author at position 0: %s " %qres.result[0])
#the above print statement is printing the author that is second... not sure why.




