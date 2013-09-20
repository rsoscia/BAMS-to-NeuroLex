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
       
       
    """SELECT DISTINCT ?AuthName ?Defin
       WHERE {
          ?a property:Authors ?AuthName .
          ?a property:Definition ?Defin .
       }""",
	)
	
	
#Gives both authors:
#Second author is really the first, etc. as you can see at the following link:
#http://neurolex.org/wiki/Special:ExportRDF/birnlex_1489
print("Author at position 0: %s " %qres.result[0][0])
print("Author at position 0: %s " %qres.result[1][0])
#Gives the definition:
print("Definition: %s " %qres.result[0][1])