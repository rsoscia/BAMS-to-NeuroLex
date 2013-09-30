# Below are some sample queries used to explore the BAMS data.
# September 29, 2013
# these queries are separated by ######## and can be copy and pasted into the terminal after running 
# SPARQL_BAMS_Store_Persist_Example.py (regularly) && 
# SPARQL_BAMS_Store_Query_Example.py (in python interactive mode)


##########################################################################################

print("going to get results...")
qres = g.query(
     """SELECT ?subject ?predicate ?object
       WHERE {
          ?subject ?predicate ?object.
    	} LIMIT 5""")
print("printing results")

#Search through everything
#for i in qres:
	#print("Definition: %s" %qres.result[i])
#print("Name: %s" %qres.result[0])
#TypeError: not all arguments converted during string formatting

print("The graph has " + str(len(g)) + " items in it")
	#Returns the following:
	#The graph has 22176 items in it
print("Name--not necessarily in string format: ")
	#Returns the following:
	#Name--not necessarily in string format:
	
print(qres.result[0])
	#Returns the following:
	#(rdflib.term.BNode('Ndf48c09cc76f48c2bc02ca3b687a8d06'), 
	#rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'), 
	#rdflib.term.URIRef(u'file:///anchor'))
print(qres.result[1])
	#Returns the following:
	#(rdflib.term.BNode('Ndf48c09cc76f48c2bc02ca3b687a8d06'), 
	#rdflib.term.URIRef(u'http://www.w3.org/1999/xlinktype'), 
	#rdflib.term.Literal(u'simple'))
print(qres.result[2])
	#Returns the following:
	#(rdflib.term.BNode('Ndf48c09cc76f48c2bc02ca3b687a8d06'), 
	#rdflib.term.URIRef(u'http://www.w3.org/1999/xlinkhref'), 
	#rdflib.term.Literal(u'http://brancusi1.usc.edu/thesaurus/definition/tectum/'))






#Conclusion about printing:
	
#Picks out the a triple (based on it's index w/in the data) from the data
	#Zero specifies the triple held at index = 0
print(qres.result[0])
	#Returns the following:
	#(rdflib.term.BNode('Ndf48c09cc76f48c2bc02ca3b687a8d06'), 
	#rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'), 
	#rdflib.term.URIRef(u'file:///anchor'))

#Array 2 picks the specified node from the specified triple (called from the first array)
	#0 specifies the first node in the triple specified before
print(qres.result[0][0])
	#Returns the following:
	#Ndf48c09cc76f48c2bc02ca3b687a8d06
	
#Array 3 specifies which element from the first node in the first triple you'd like to see
	#zero in the third array picks out the element at position 0 in the first node of the first triple (i.e. "N")	
print(qres.result[0][0][0])
	#Returns the following:
	#N
	
#To test my assertion above, I put 1 as the value in the third array, and as i predicted.. the second element
# in the first triple's first node is extracted.
print(qres.result[0][0][1])
	#Returns the following:
	#d




# Building off of this knowledge to conduct more intelligent queries:



# New Query 1.0
#Desired Outcome:
#Actual Outcome:
qres = g.query(
     prefix bams: <http://brancusi1.usc.edu/RDF/>
     """SELECT ?subject ?predicate ?object
       WHERE {
          ?subject ?predicate ?object.
    	} LIMIT 5""")
print(qres.result[0])
	#Returns the following:
	#(rdflib.term.BNode('N35f13b7fbc4e4b80a47e4bf277acd530'), 
	#rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'), 
	#rdflib.term.URIRef(u'file:///anchor'))
	
#Returned when there was no prefix "bams" inside the query
	#Returns the following:
	#(rdflib.term.BNode('Ndf48c09cc76f48c2bc02ca3b687a8d06'), 
	#rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'), 
	#rdflib.term.URIRef(u'file:///anchor'))
	




#Insert this string somewhere:
	#?x ?y "Basal ganglia"^^xsd:string .
##########################################################################################
# New Query 1.0 (with modification):


#prefix xsd: <http://www.w3.org/2001/XMLSchema#>
prefix BAMS: <http://brancusi1.usc.edu/RDF/>
qres = g.query(
     """SELECT ?subject ?predicate ?object
       WHERE {
          ?subject ?predicate ?object.
    	} LIMIT 5""")
print("printing results")
print(qres.result[0])
	#Returned the following:
		#(rdflib.term.BNode('N35f13b7fbc4e4b80a47e4bf277acd530'), 
		#rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'), 
		#rdflib.term.URIRef(u'file:///anchor'))
print(qres.result[1])
	#Returned the following:
		#(rdflib.term.BNode('N35f13b7fbc4e4b80a47e4bf277acd530'), 
		#rdflib.term.URIRef(u'http://www.w3.org/1999/xlinktype'), 
		#rdflib.term.Literal(u'simple'))
print(qres.result[2])
	#Returned the following:
		#(rdflib.term.BNode('N35f13b7fbc4e4b80a47e4bf277acd530'), 
		#rdflib.term.URIRef(u'http://www.w3.org/1999/xlinkhref'), 
		#rdflib.term.Literal(u'http://brancusi1.usc.edu/thesaurus/definition/bilateral-symmetry/'))
print(qres.result[3])
	#Returned the following:
		#(rdflib.term.BNode('Ne30bfc8d40c54a339e2e5fc857c4f4a4'), 
		#rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'), 
		#rdflib.term.URIRef(u'file:///anchor'))

print(qres.result[4])
	#Returned the following:
		#(rdflib.term.BNode('Ne30bfc8d40c54a339e2e5fc857c4f4a4'), 
		#rdflib.term.URIRef(u'http://www.w3.org/1999/xlinktype'), 
		#rdflib.term.Literal(u'simple'))
print(qres.result[5])
	#The following results were returned because the query has a limit of 5, thus 0-4 satisfy the 5 indexes within its specified limits
	#Returned the following:
		#Traceback (most recent call last):
  		#File "<stdin>", line 1, in <module>
		#IndexError: list index out of range

###########################################
###########################################
###########################################
Extension of above queries:
prefix BAMS: <http://brancusi1.usc.edu/RDF/>
qres = g.query(
     """SELECT ?subject ?predicate ?object
       WHERE {
          ?subject ?predicate ?object.
    	} LIMIT 5""")
print("printing results")
print(qres.result[0])
	

##########################################
EXAMPLE STEPHEN AND I WENT OVER:
prefix xsd: <http://www.w3.org/2001/XMLSchema#>
prefix property: <http://neurolex.org/wiki/Property-3A>
	select DISTINCT ?x ?axonl where 
	{
	?x property:Id "nifext_128"^^xsd:string . 
	?x property:AxonLength ?axonl 
	}
###########################################
USING THE ABOVE QUERY TO MODIFY THE BELOW QUERY
###########################################
prefix BAMS: <http://brancusi1.usc.edu/RDF/>
qres = g.query(
     """SELECT ?subject ?predicate ?object
       WHERE {
          ?subject ?predicate ?object.
    	} LIMIT 5""")
print("printing results")
print(qres.result[0])
#############################################
#############################################
RESULT QUERY(essentially trying to figure out how to get the prefix(s) working):

prefix xsd: <http://www.w3.org/2001/XMLSchema#>
prefix BAMS: <http://brancusi1.usc.edu/RDF/>
qres = g.query(
     """SELECT DISTINCT ?x ?def
       WHERE {
          ?x BAMS:Definition "Basal ganglia"^^xsd:string .
          ?x BAMS:Definition ?def.
    	} LIMIT 5""")
print("printing results")
print(qres.result[0])
	#Returns the following:
	#(rdflib.term.BNode('N35f13b7fbc4e4b80a47e4bf277acd530'), 
	#rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'), 
	#rdflib.term.URIRef(u'file:///anchor'))
print(qres.result[1])
	#Returns the following:
	#(rdflib.term.BNode('N35f13b7fbc4e4b80a47e4bf277acd530'), 
	#rdflib.term.URIRef(u'http://www.w3.org/1999/xlinktype'), 
	#rdflib.term.Literal(u'simple'))
print(qres.result[2])
	#Returns the following:
	#(rdflib.term.BNode('N35f13b7fbc4e4b80a47e4bf277acd530'), 
	#rdflib.term.URIRef(u'http://www.w3.org/1999/xlinkhref'), 
	#rdflib.term.Literal(u'http://brancusi1.usc.edu/thesaurus/definition/bilateral-symmetry/'))
print(qres.result[3])
	#Returns the following:
	#(rdflib.term.BNode('Ne30bfc8d40c54a339e2e5fc857c4f4a4'), 
	#rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'), 
	#rdflib.term.URIRef(u'file:///anchor'))
print(qres.result[4])
	#Returns the following:
	#(rdflib.term.BNode('Ne30bfc8d40c54a339e2e5fc857c4f4a4'), 
	#rdflib.term.URIRef(u'http://www.w3.org/1999/xlinktype'), 
	#rdflib.term.Literal(u'simple'))

print(qres.result[5])
	#Returns the following:
	#Traceback (most recent call last):
  	#File "<stdin>", line 1, in <module>
	#IndexError: list index out of range
print(qres.result[0][0])
	#Returns the following:
	#N35f13b7fbc4e4b80a47e4bf277acd530
print(qres.result[0][1])
	#Returns the following:
	#http://www.w3.org/1999/02/22-rdf-syntax-ns#type
print(qres.result[0][2])
	#Returns the following:
	#file:///anchor
print(qres.result[0][3])
	#Returns the following:
	#Traceback (most recent call last):
  	#File "<stdin>", line 1, in <module>
	#IndexError: tuple index out of range
print(qres.result[0][4])
	#Returns the following:
	#Traceback (most recent call last):
  	#File "<stdin>", line 1, in <module>
	#IndexError: tuple index out of range
print(qres.result[0][5])
	#Returns the following:
	#Traceback (most recent call last):
  	#File "<stdin>", line 1, in <module>
	#IndexError: tuple index out of range
print(qres.result[1][1])
	#Returns the following:
	#http://www.w3.org/1999/xlinktype
print(qres.result[2][1])
	#Returns the following:
	#http://www.w3.org/1999/xlinkhref
print(qres.result[3][1])
	#Returns the following:
	#http://www.w3.org/1999/02/22-rdf-syntax-ns#type
print(qres.result[4][1])
	#Returns the following:
	#http://www.w3.org/1999/xlinktype
#print(qres.result[5][1])
	#Traceback (most recent call last):
 	#File "<stdin>", line 1, in <module>
	#IndexError: list index out of range
#############################################
#Modifying the limit size, then printing the first 20 triples
prefix xsd: <http://www.w3.org/2001/XMLSchema#>
prefix BAMS: <http://brancusi1.usc.edu/RDF/>
qres = g.query(
     """SELECT DISTINCT ?x ?def
       WHERE {
          ?x BAMS:Definition "Basal ganglia"^^xsd:string .
          ?x BAMS:Definition ?def.
    	} LIMIT 20""")
print("printing results")
print(qres.result[0])
print(qres.result[1])
print(qres.result[2])
print(qres.result[3])
print(qres.result[4])
print(qres.result[5])
print(qres.result[6])
print(qres.result[7])
print(qres.result[8])
print(qres.result[9])
print(qres.result[10])
print(qres.result[11])
print(qres.result[12])
print(qres.result[13])
print(qres.result[14])
print(qres.result[15])
print(qres.result[16])
print(qres.result[17])
print(qres.result[18])
print(qres.result[19])
print(qres.result[20])

Says the index is out of range when we get to printing the results at index = 4,
Maybe this means there are only 5 types of basal ganglia defined by the BAMS thesaurus...
Going to website to double check.. pretty sure i saw this before though.

http://brancusi1.usc.edu/thesaurus/list/by_initial/B/

the above link supports my observation, because there were 5 terms with the strings "basal ganglia" in the front





#Ask a specific question about that RDF document
qres = g.query(
	prefix bams: <http://brancusi1.usc.edu/RDF/>
	
    """SELECT DISTINCT ?b
       WHERE {
          ?a bams:Definition ?b .
       }""",
    #initNs=dict(
    #    property=rdflib.Namespace("http://neurolex.org/wiki/Special:URIResolver/Property-3A"),
    #    wiki=rdflib.Namespace("http://neurolex.org/wiki/Special:URIResolver/")))


#print("Definition: %s" % qres.result[0])
print(qres.result[0])	