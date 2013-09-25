#Document of Queries i ran on the BAMS data to determine it's format:

#select DISTINCT ?prop where 
#	{?x ?prop ?y} 

#example form neurolex.org

#select DISTINCT ?name ?id where 
#   {?x property:Id "birnlex_779"^^xsd:string .     # the id corresponds to the Granular layer of cerebellar cortex
#   ?cells property:Located_in ?x.                  # find anything using the Located_in property (typically only cells)
#   ?cells property:Label ?name.                    # get the name of the triples matched above from the label
#   ?cells property:Id ?id} 

#Based off the above example, going to make a query like this for the BAMS data:
select DISTINCT ?name ?id where 
   {?x property:Id "birnlex_779"^^xsd:string .     # the id corresponds to the Granular layer of cerebellar cortex
   ?cells property:Located_in ?x.                  # find anything using the Located_in property (typically only cells)
   ?cells property:Label ?name.                    # get the name of the triples matched above from the label
   ?cells property:Id ?id} 

	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/
	prefix bams: <http://brancusi1.usc.edu/RDF/>
	basal-ganglia-4
	 
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/
	
	prefix bams: <http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/>
	#Things inside this prefix:
		#term
		#definition
			
qres = g.query(
    #prefix bams: <http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/>   	
	#prefix bams: <http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/>  
	prefix bams: http://brancusi1.usc.edu/thesaurus/definition/
"""SELECT ?subject ?predicate ?object
       WHERE {
          ?cells bams:Definition "
    	} LIMIT 5""")
    	
print("printing results")
##################################
qres = g.query(
    """SELECT DISTINCT ?definition
       WHERE {
          ?cells property:Definition "basal-ganglia-4"^^xsd:string ?definition.
    	}""",)
##################################
prefix bams: <http://brancusi1.usc.edu/RDF/>

SELECT ?x ?y ?def
WHERE {
  ?x ?y "Basal ganglia"^^xsd:string .
  ?x bams:Definition ?def
} LIMIT 5
##################################




####################################################################
####################################################################
####################################################################
#Original Query#####################################################
####################################################################
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
####################################################################
#Output from Original Query:########################################
####################################################################
(rdflib.term.URIRef(u'http://brancusi1.usc.edu/RDF/conn_42771'), 
rdflib.term.URIRef(u'http://brancusi1.usc.edu/RDF/description'), 
rdflib.term.Literal(u'Collator note: NIc does not receive projections from this region, because all of the atlas levels were inspected and no label was found.'))
####################################################################
#My Thoughts:
#The query produces this weird result because it's only spitting out the one at position 0:
#Try other positions...
####################################################################
####################################################################



####################################################################
####################################################################
####################################################################
#Original Query (modified_V1)#######################################
#Modifications:
	#Added Prefix
	#Edited the query and formatted it to the example Stephen and I went over
####################################################################


qres = g.query(
	prefix bams: <http://brancusi1.usc.edu/RDF/>  
	#should be accessing "bams" rather than "prefix"... doesn't work though
     """SELECT ?subject ?predicate ?def
       WHERE {
          ?subject ?predicate "Basal ganglia"^^xsd:string .
          ?subject ?predicate prefix:Definition ?def.
    	} LIMIT 5""")

print("printing results")

#Search through everything
#for i in qres:
#	print("Definition: %s" %qres.result[i])

#print("Name: %s" %qres.result[0])
#TypeError: not all arguments converted during string formatting

print("The graph has " + str(len(g)) + " items in it")
#The graph has 670161 items in it

print("Name--not necessarily in string format: ")

print(qres.result[0][0])
#http://brancusi1.usc.edu/RDF/conn_42771
print(qres.result[1][0])
#http://brancusi1.usc.edu/RDF/conn_42771
print(qres.result[2][0])
#http://brancusi1.usc.edu/RDF/conn_42771
print(qres.result[0][1])
#http://brancusi1.usc.edu/RDF/description
print(qres.result[1][1])
#http://brancusi1.usc.edu/RDF/reference
print(qres.result[2][1])
#http://www.w3.org/1999/02/22-rdf-syntax-ns#type
print(qres.result[0][2])
#Collator note: NIc does not receive projections from this region, because all of the atlas levels were inspected and no label was found.
print(qres.result[1][2])
#N27d18a5dcbdc41c89054a6eb0e287c22
print(qres.result[2][2])
#http://brancusi1.usc.edu/RDF/connection

print(qres.result[0][0])
#http://brancusi1.usc.edu/RDF/conn_42771
print(qres.result[0][1])
#http://brancusi1.usc.edu/RDF/description
print(qres.result[0][2])
#Collator note: NIc does not receive projections from this region, because all of the atlas levels were inspected and no label was found.
print(qres.result[1][0])
#http://brancusi1.usc.edu/RDF/conn_42771
print(qres.result[1][1])
#http://brancusi1.usc.edu/RDF/reference
print(qres.result[1][2])
#N27d18a5dcbdc41c89054a6eb0e287c22
print(qres.result[2][0])
#http://brancusi1.usc.edu/RDF/conn_42771
print(qres.result[2][1])
#http://www.w3.org/1999/02/22-rdf-syntax-ns#type
print(qres.result[2][2])
#http://brancusi1.usc.edu/RDF/connection


#print(qres.result[0])
####################################################################
#Output from Original Query (modified_V1):########################################
####################################################################
(rdflib.term.URIRef(u'http://brancusi1.usc.edu/RDF/conn_42771'), 
rdflib.term.URIRef(u'http://brancusi1.usc.edu/RDF/description'), 
rdflib.term.Literal(u'Collator note: NIc does not receive projections from this region, because all of the atlas levels were inspected and no label was found.'))
####################################################################
####################################################################
####################################################################




####################################################################
####################################################################
####################################################################
#Query 1############################################################
####################################################################
prefix bams: http://brancusi1.usc.edu/thesaurus/definition/

qres = g.query(
    """SELECT DISTINCT ?definition
       WHERE {
          ?cells bams:term "basal-ganglia-4"^^xsd:string ?definition.
    	} LIMIT 5""",)
print("printing results")
print(qres.result[0])
####################################################################
####################################################################
####################################################################

##################################

#Search through everything
#for i in qres:
#	print("Definition: %s" %qres.result[i])

#print("Name: %s" %qres.result[0])
#TypeError: not all arguments converted during string formatting

print("The graph has " + str(len(g)) + " items in it")

print("Name--not necessarily in string format: ")
print(qres.result[0])

	
#########################################################
#########################################################
#Approach:

#Determining the format of the BAMS data held inside the RDF
#Picking out everything related to "Basal Ganglia" inside the RDF

#Tasks:
#Make sure the rdf is the right zipfile first off
	#Defined in (SPARQL_BAMS_Store_Persist_Example.py)
	#Run first program (SPARQL_BAMS_Store_Persist_Example.py)
		#Literally type: (python SPARQL_BAMS_Store_Persist_Example.py)
	#Run second program (SPARQL_BAMS_Store_Query_Example.py)
		#Literally type: (python -i SPARQL_BAMS_Store_Query_Example.py)
	#Conduct a series of test queries that will lead me to better understand the format of the data
	#Use this obtained knowledge to extract all of related "Basal Ganglia" data
#########################################################
#Notes:

#Possible strings to use in the query (plucked from inspecting the basal ganglia elements on the BAMS FMC Thesaurus
	#basal-ganglia-4
	#basal-ganglia
	#basal-ganglia-2
#This last one might be too specific and not needed, but worth noting..
	#basal-ganglia-of-telencephalon	
#########################################################	
	
	
qres = g.query(
     prefix bams: <http://brancusi1.usc.edu/RDF/>    	

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
