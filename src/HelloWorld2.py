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
#result = g.parse("http://neurolex.org/wiki/Special:ExportRDF/birnlex_1489", format="application/rdf+xml")
#result = g.parse("/Users/ryansoscia/BAMS-to-NeuroLex/Data/bams_ontology_2013-07-10_03-20-00.xml", format="application/rdf+xml")

result = g.parse("http://neurolex.org/wiki/Special:ExportRDF/birnlex_1489", format="application/rdf+xml")


#prints the result in a non readable format
#print("result is in the format:", result)
#not sure how to convert it yet
#print("result is in the format:", result)

#print("g.result is:", g[:0])





#Ask a specific question about that RDF document
qres = g.query(
    """SELECT DISTINCT ?definition
       WHERE {
          ?cells property:Definition "birnlex_1489"^^xsd:string ?definition.
    	}""",)
    
    
    
    #initNs=dict(
        #property=rdflib.Namespace("http://neurolex.org/wiki/Special:URIResolver/birnlex_1489"),
        #wiki=rdflib.Namespace("http://neurolex.org/wiki/Special:URIResolver/")))

#possibilities:

for i in qres:
	print("Definition: %s" % qres.result[i])


#sparql.setReturnFormat(JSON)
#results = sparql.query().convert()
#print("RESULTS $s" %results)
	


#results = sparql.query().convert()

#for i in results["results"]["bindings"]:
#	print (i["b"]["definition"])
