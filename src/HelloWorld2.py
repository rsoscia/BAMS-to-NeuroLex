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
    """SELECT DISTINCT ?b
       WHERE {
          ?a property:Definition ?b .
       }""",
    initNs=dict(
        property=rdflib.Namespace("http://neurolex.org/wiki/Special:URIResolver/Property-3A"),
        wiki=rdflib.Namespace("http://neurolex.org/wiki/Special:URIResolver/")))


print("Definition: %s" % qres.result[0])