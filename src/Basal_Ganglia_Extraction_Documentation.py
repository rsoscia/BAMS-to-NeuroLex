//Documentation of SPARQL Queries targeting specific information in the BAMS thesaurus:
//Using the fixed RDF

	cd BAMS-to-NeuroLex/src/
		

//Ran The Persist Example in terminal:

	python SPARQL_BAMS_Store_Persist_Example.py

		#SPARQL_BAMS_Store_Persist_Example.py
		#This program is used to open up BAMS data, persist it to a store for speed up of querying
		
		
		#Needed after IPython installation:
		#import sys
		#print(sys.path)
		#shows that the path was changed after downloading anaconda and IPython Notebook
		#sys.path += ['', 'C:\Python27\Lib\idlelib', 'C:\Python27\lib\site-packages\pip-1.1-py2.7.egg', 'C:\Python27\lib\site-packages\gensim-0.8.6-py2.7.egg', 'C:\WINDOWS\system32\python27.zip', 'C:\Python27\DLLs', 'C:\Python27\lib', 'C:\Python27\lib\plat-win', 'C:\Python27\lib\lib-tk', 'C:\Python27', 'C:\Python27\lib\site-packages', 'C:\Python27\lib\site-packages\PIL'] 
		
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
		r = open("../Data/bams_thesaurus_2013-10-06_14-58-56.xml.zip")
		
		
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
		foofile = myzipfile.open('bams_thesaurus_2013-10-06_14-58-56.xml')
		
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
		result = g.parse(file=myzipfile.open('bams_thesaurus_2013-10-06_14-58-56.xml'), format="application/rdf+xml")
		
		foofile.close()
		
		# when done!
		g.close()
		
		print("Graph stored to disk")
		
//RESULTS:
	~40 seconds for zip to open...
	loading up the BAMS file in memory...
	Graph stored to disk


//Getting into interactive mode:
	python -i
	
//Now that the graph is stored to disk, let's play with some queries:
//If actually using the below code, tab it to the left twice.

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

for r in qres.result:
	print str(r[0]), str(r[1]), str(r[2])


#RESULTS:
	>>> print("The graph has " + str(len(g)) + " items in it")
	The graph has 3797 items in it
	
	>>> print(qres.result[0])
	(rdflib.term.URIRef(u'http://brancusi1.usc.edu/thesaurus/definition/neural-subnetwork/'), 
	rdflib.term.URIRef(u'http://brancusi1.usc.edu/RDF/workspace'), 
	rdflib.term.Literal(u'0'))
	
	>>> for r in qres.result:
	...     print str(r[0]), str(r[1]), str(r[2])
	... 
	http://brancusi1.usc.edu/thesaurus/definition/neural-subnetwork/ 
	http://brancusi1.usc.edu/RDF/workspace 
	0
	
	http://brancusi1.usc.edu/thesaurus/definition/neural-subnetwork/ 
	http://www.w3.org/1999/02/22-rdf-syntax-ns#type 
	http://brancusi1.usc.edu/RDF/thesaurus
	
	http://brancusi1.usc.edu/thesaurus/definition/neural-subnetwork/ 
	http://brancusi1.usc.edu/RDF/definition
	An arbitrary subset of a complete <a href="/thesaurus/definition/neural-network/"><span class="synonim_bold">neural network</span></a>, often distinguished on functional grounds. A closely related term is <a href="/thesaurus/definition/neural-subsystem/"><span class="synonim_bold">neural subsystem</span></a>.
	
	http://brancusi1.usc.edu/thesaurus/definition/neural-subnetwork/ 
	http://brancusi1.usc.edu/RDF/entry 
	Neural subnetwork
	
	http://brancusi1.usc.edu/thesaurus/definition/neural-subnetwork/ 
	http://brancusi1.usc.edu/RDF/preferred 
	True
	




//RAN ANOTHER ONE OF STEPHEN'S EXAMPLE QUERIES:
	qres = g.query(
		 """SELECT ?predicate ?object
		   WHERE {
			  <http://brancusi1.usc.edu/thesaurus/definition/corpora-quadrigemina/> ?predicate ?object.
			} LIMIT 5""")
	
	for r in qres.result:
		print str(r[0]), str(r[1])

//RESULTS:
	http://brancusi1.usc.edu/RDF/workspace 0
	http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/winslow-1733/">Winslow, 1733</a>
	http://brancusi1.usc.edu/RDF/definition Synonym for macrodissected adult human <a href="/thesaurus/definition/tectum/"><span class="synonim_bold">tectum (Schwalbe, 1881)</span></a>; Sect. X, p. 37. Quadrigeminal body in English.
	http://brancusi1.usc.edu/RDF/entry Corpora quadrigemina

//Modifying the above example to search for the definition of basal-ganglia:
qres = g.query(
	 """SELECT ?predicate ?object
	   WHERE {
		  <http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/> ?predicate ?object.
		} LIMIT 5""")

for r in qres.result:
	print str(r[0]), str(r[1])

//RESULTS:
	http://brancusi1.usc.edu/RDF/workspace 0
	http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/ferrier-d-1876/">Ferrier, 1876</a>
	http://brancusi1.usc.edu/RDF/definition In modern terms includes for macrodissected adult monkeys and humans the <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a> and <a href="/thesaurus/definition/interbrain/"><span class="synonim_bold">interbrain (Baer, 1837)</span></a> considered together; pp. 8, 236.
	http://brancusi1.usc.edu/RDF/entry Basal ganglia

//This is good!!!


Block of code, messing around with it:
###############################################################################################################################
//Runing the above query with the prefix notation:
	
	qres = g.query(
		 """PREFIX bams: <http://brancusi1.usc.edu/thesaurus/definition/>
		 SELECT ?predicate ?object
		   WHERE {
			  <http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/> ?predicate ?object.
			} LIMIT 5""")
	
	for r in qres.result:
		print str(r[0]), str(r[1])


//Results:
	http://brancusi1.usc.edu/RDF/workspace 0
	http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/ferrier-d-1876/">Ferrier, 1876</a>
	http://brancusi1.usc.edu/RDF/definition In modern terms includes for macrodissected adult monkeys and humans the <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a> and <a href="/thesaurus/definition/interbrain/"><span class="synonim_bold">interbrain (Baer, 1837)</span></a> considered together; pp. 8, 236.
	http://brancusi1.usc.edu/RDF/entry Basal ganglia


//I admit, the above prefix is a little messed up. Below is an attempt to fix it:
qres = g.query(
	 """PREFIX bams: <http://brancusi1.usc.edu/thesaurus/definition/>
	 SELECT ?predicate ?object
	   WHERE {
		  bams:"basal-ganglia" ?predicate ?object.
		} LIMIT 5""")

for r in qres.result:
	print str(r[0]), str(r[1])

//Didn't get it to work... don't necessarily need it to work moving on.
###############################################################################################################################



Block of code (same example twice--checking for syntax issues within query)
###############################################################################################################################
// Running an example with this as the predicate:<http://brancusi1.usc.edu/RDF/definition>:
	qres = g.query(
		 """SELECT ?predicate ?object
		   WHERE {
			  ?predicate <http://brancusi1.usc.edu/RDF/definition> ?object.
			} LIMIT 5""")
	
	for r in qres.result:
		print str(r[0]), str(r[1])

//Results (possibly a syntax issue):
	http://brancusi1.usc.edu/thesaurus/definition/neural-subnetwork/ An arbitrary subset of a complete <a href="/thesaurus/definition/neural-network/"><span class="synonim_bold">neural network</span></a>, often distinguished on functional grounds. A closely related term is <a href="/thesaurus/definition/neural-subsystem/"><span class="synonim_bold">neural subsystem</span></a>.
	http://brancusi1.usc.edu/thesaurus/definition/neural-subsystem/ A subset of the complete<a href="/thesaurus/definition/nervous-system-2/"><span class="synonim_bold"> nervous system (Monro, 1783) </span></a>defined on functional grounds; for example, the visual system or the somatic motor system. A closely related term is <a href="/thesaurus/definition/neural-subnetwork/"><span class="synonim_bold">neural subnetwork</span></a>, but formally a <a href="/thesaurus/definition/neural-subsystem/"><span class="synonim_bold">neural subsystem</span></a> would include objects other than <a href="/thesaurus/definition/neuron/"><span class="synonim_bold">neurons (Waldeyer, 1891)</span></a>.
	http://brancusi1.usc.edu/thesaurus/definition/neural-tube/
	Traceback (most recent call last):
	  File "<stdin>", line 2, in <module>
	  File "/Library/Python/2.7/site-packages/rdflib/term.py", line 1250, in __str__
		return self.encode()
	UnicodeEncodeError: 'ascii' codec can't encode character u'\xe4' in position 1195: ordinal not in range(128)

//Seeing if the syntax is corrected using this example:
qres = g.query(
	 """SELECT ?subject ?object
	   WHERE {
		  ?subject <http://brancusi1.usc.edu/RDF/definition> ?object.
		} LIMIT 5""")

for r in qres.result:
	print str(r[0]), str(r[1])

//Results:
	http://brancusi1.usc.edu/thesaurus/definition/neural-subnetwork/ An arbitrary subset of a complete <a href="/thesaurus/definition/neural-network/"><span class="synonim_bold">neural network</span></a>, often distinguished on functional grounds. A closely related term is <a href="/thesaurus/definition/neural-subsystem/"><span class="synonim_bold">neural subsystem</span></a>.
	http://brancusi1.usc.edu/thesaurus/definition/neural-subsystem/ A subset of the complete<a href="/thesaurus/definition/nervous-system-2/"><span class="synonim_bold"> nervous system (Monro, 1783) </span></a>defined on functional grounds; for example, the visual system or the somatic motor system. A closely related term is <a href="/thesaurus/definition/neural-subnetwork/"><span class="synonim_bold">neural subnetwork</span></a>, but formally a <a href="/thesaurus/definition/neural-subsystem/"><span class="synonim_bold">neural subsystem</span></a> would include objects other than <a href="/thesaurus/definition/neuron/"><span class="synonim_bold">neurons (Waldeyer, 1891)</span></a>.
	http://brancusi1.usc.edu/thesaurus/definition/neural-tube/
	Traceback (most recent call last):
	  File "<stdin>", line 2, in <module>
	  File "/Library/Python/2.7/site-packages/rdflib/term.py", line 1250, in __str__
		return self.encode()
	UnicodeEncodeError: 'ascii' codec can't encode character u'\xe4' in position 1195: ordinal not in range(128)

//Same exact results... doesn't seem like a syntax issue.
//I'm wondering why the rest of the definitions were not displayed... I checked the link and it's live.
//The problem is probably caused by some terms in the definition that are unable to be formatted as strings.
//To test this hypothesis, i'm running the exact same query but only printing r[0], the results should includ 5 unique URI's
###############################################################################################################################

//Running a modified query:
qres = g.query(
	 """SELECT ?subject ?object
	   WHERE {
		  ?subject <http://brancusi1.usc.edu/RDF/definition> ?object.
		} LIMIT 5""")

for r in qres.result:
	print str(r[0])
//Results:
	http://brancusi1.usc.edu/thesaurus/definition/neural-subnetwork/
	http://brancusi1.usc.edu/thesaurus/definition/neural-subsystem/
	http://brancusi1.usc.edu/thesaurus/definition/neural-tube/
	http://brancusi1.usc.edu/thesaurus/definition/neurite/
	http://brancusi1.usc.edu/thesaurus/definition/neuron/
//Success! that was definitely the problem.
//From here i'm checking out the rest of Stephen's notes to see how much more complexity is needed to obtain all relevant info
//regarding a specific subject... then i'll apply all of the methods to basal ganglia and it's counterparts.




//These are the items that are "upstream" of the blank node, where the blank node is the 'object'. Let's look at if this blank node is the subject of any triples:
//replacing the "blank node" with "basal ganglia" and conducting the query:

qres = g.query(
	 """SELECT ?subject ?predicate
	   WHERE {
		  ?subject ?predicate _:Basal ganglia.
		} LIMIT 5""")

for r in qres.result:
	print str(r[0])

//Result:
	//NOTHING -- WRONG SYNTAX.

//Skipped looking at what is upstream and downsteam of Basal Ganglia... moving on



//The below query is used to make sure there aren't any blank nodes returned, if there are then the RDF isn't fixed yet:
	
	qres = g.query(
		 """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
		   SELECT ?subject ?object
		   WHERE {
			  ?subject bamsProp:definition ?object.
			} LIMIT 50""")
	
	for r in qres.result:
		print str(r[0]), str(r[1])

//Results:
	http://brancusi1.usc.edu/thesaurus/definition/neural-subnetwork/ An arbitrary subset of a complete <a href="/thesaurus/definition/neural-network/"><span class="synonim_bold">neural network</span></a>, often distinguished on functional grounds. A closely related term is <a href="/thesaurus/definition/neural-subsystem/"><span class="synonim_bold">neural subsystem</span></a>.
	http://brancusi1.usc.edu/thesaurus/definition/neural-subsystem/ A subset of the complete<a href="/thesaurus/definition/nervous-system-2/"><span class="synonim_bold"> nervous system (Monro, 1783) </span></a>defined on functional grounds; for example, the visual system or the somatic motor system. A closely related term is <a href="/thesaurus/definition/neural-subnetwork/"><span class="synonim_bold">neural subnetwork</span></a>, but formally a <a href="/thesaurus/definition/neural-subsystem/"><span class="synonim_bold">neural subsystem</span></a> would include objects other than <a href="/thesaurus/definition/neuron/"><span class="synonim_bold">neurons (Waldeyer, 1891)</span></a>.
	http://brancusi1.usc.edu/thesaurus/definition/neural-tube/
	Traceback (most recent call last):
	  File "<stdin>", line 2, in <module>
	  File "/Library/Python/2.7/site-packages/rdflib/term.py", line 1250, in __str__
		return self.encode()
	UnicodeEncodeError: 'ascii' codec can't encode character u'\xe4' in position 1195: ordinal not in range(128)
// although all 5 terms and definitions should have been printed, just like before there is something in the 3rd term's definition
// that is unable to be converted into a string... so ultimately this is good for purposes of proving the RDF is fine.


###############################################################################################################################
###############################################################################################################################
//Finally getting into some Basal Ganglia specific queries:
	
	qres = g.query(
		 """SELECT ?predicate ?object
		   WHERE {
			  <http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/> ?predicate ?object.
			} LIMIT 5""")
	
	for r in qres.result:
		print str(r[0]), str(r[1])
Results:
	http://brancusi1.usc.edu/RDF/workspace 0
	http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/ferrier-d-1876/">Ferrier, 1876</a>
	http://brancusi1.usc.edu/RDF/definition In modern terms includes for macrodissected adult monkeys and humans the <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a> and <a href="/thesaurus/definition/interbrain/"><span class="synonim_bold">interbrain (Baer, 1837)</span></a> considered together; pp. 8, 236.
	http://brancusi1.usc.edu/RDF/entry Basal ganglia


//Now taking the limit off the above query:
	qres = g.query(
		 """SELECT ?predicate ?object
		   WHERE {
			  <http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/> ?predicate ?object.
			}""")
	
	for r in qres.result:
		print str(r[0]), str(r[1])
Results:
	http://brancusi1.usc.edu/RDF/workspace 0
	http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/ferrier-d-1876/">Ferrier, 1876</a>
	http://brancusi1.usc.edu/RDF/definition In modern terms includes for macrodissected adult monkeys and humans the <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a> and <a href="/thesaurus/definition/interbrain/"><span class="synonim_bold">interbrain (Baer, 1837)</span></a> considered together; pp. 8, 236.
	http://brancusi1.usc.edu/RDF/entry Basal ganglia
	http://brancusi1.usc.edu/RDF/slug basal-ganglia
//Good, this produces one more result than the limited query.
// the last thing returned from the query "basal-ganglia" is the node id (i think)



//Running another one of Stephen's example queries:
qres = g.query(
     """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
       SELECT ?subject ?predicate
       WHERE {
          ?subject bamsProp:entry "Basal ganglia".
    	}""")

for r in qres.result:
    print str(r[0]), str(r[1])
Results:
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/ None
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/ None
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/ None
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/ None

//shows the different node id's for the various types of basal ganglia, should be pretty useful.
//although there are only 4 above, the BAMS thesaurus website shows 5
//the additional basal ganglia has the node id "basal-ganglia-of-telencephalon" .. not sure if this is even the same thing,
//but it does have the basal ganglia prefix


//Retrieving basal ganglia information:
//starting off with basal-ganglia-2:

	qres = g.query(
		 """SELECT ?predicate ?object
		   WHERE {
			  <http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/> ?predicate ?object.
			}""")
	
	for r in qres.result:
		print str(r[0]), str(r[1])

Results:
	http://brancusi1.usc.edu/RDF/workspace 0
	http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/strong-os-elwyn-a-1943/">Strong & Elwyn, 1943</a>
	http://brancusi1.usc.edu/RDF/definition Synonym for basal ganglia of telencephalon (Ranson, 1920) in macrodissected adult humans, and thus not synonymous with <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; p. 319.
	http://brancusi1.usc.edu/RDF/entry Basal ganglia
	http://brancusi1.usc.edu/RDF/slug basal-ganglia-2
//the important things to note are the following:
	// slug = node id
	// entry = name
	// definition = definition of node id



######################################################
//making the URI the predicate rather than the subject:
qres = g.query(
	 """SELECT ?predicate ?object
	   WHERE {
		  ?predicate <http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/> ?object.
		}""")

for r in qres.result:
	print str(r[0]), str(r[1])
//Results:
//literally does nothing

//making the URI the object rather than the predicate
qres = g.query(
	 """SELECT ?predicate ?object
	   WHERE {
		  ?predicate ?object <http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/>.
		}""")

for r in qres.result:
	print str(r[0]), str(r[1])

Results:
//literally does nothing too-- syntax is definitely incorrect 
######################################################
//Going to try something different instead
qres = g.query(
     """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
       SELECT ?subject ?predicate ?object
       WHERE {
          bamsProp:entry "Basal ganglia" ?object .
          ?subject ?predicate ?object
    	}""")

for r in qres.result:
    print str(r[0]), str(r[1]), str(r[2])


###############################################################################################################################
###############################################################################################################################
//Rather than conducting 4 different queries on the different basal ganglia nodes, i'm doing it all at once:
qres = g.query(
     """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
       SELECT ?subject ?predicate ?object
       WHERE {
          ?subject bamsProp:entry "Basal ganglia" .
          ?subject ?predicate ?object
    	}""")

for r in qres.result:
    print str(r[0]), str(r[1]), str(r[2])
//Results:
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/carpenter-mb-1976/">Carpenter, 1976</a>
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/ http://brancusi1.usc.edu/RDF/definition For macrodissected adult humans it includes the caudate and lenticular nuclei and the amygdala, and is thus not synonymous with <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; p. 496.
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/ http://brancusi1.usc.edu/RDF/entry Basal ganglia
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/ http://brancusi1.usc.edu/RDF/slug basal-ganglia-4
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/ferrier-d-1876/">Ferrier, 1876</a>
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/ http://brancusi1.usc.edu/RDF/definition In modern terms includes for macrodissected adult monkeys and humans the <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a> and <a href="/thesaurus/definition/interbrain/"><span class="synonim_bold">interbrain (Baer, 1837)</span></a> considered together; pp. 8, 236.
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/ http://brancusi1.usc.edu/RDF/entry Basal ganglia
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/ http://brancusi1.usc.edu/RDF/slug basal-ganglia
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/strong-os-elwyn-a-1943/">Strong & Elwyn, 1943</a>
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/ http://brancusi1.usc.edu/RDF/definition Synonym for basal ganglia of telencephalon (Ranson, 1920) in macrodissected adult humans, and thus not synonymous with <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; p. 319.
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/ http://brancusi1.usc.edu/RDF/entry Basal ganglia
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/ http://brancusi1.usc.edu/RDF/slug basal-ganglia-2
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/warwick-r-williams-pl-eds-1973/">Warwick & Williams, 1973</a>
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/ http://brancusi1.usc.edu/RDF/definition Synonym for <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; see Warwick & Williams (1973, p. 805; and Williams & Warwick, 1980, p. 864). Its use is discouraged because reference to <a href="/thesaurus/definition/ganglia/"><span class="synonim_bold">ganglia (Galen, c173)</span></a> in the <a href="/thesaurus/definition/cerebrospinal-axis/"><span class="synonim_bold">cerebrospinal axis (Meckel, 1817)</span></a> is archaic; and because "basal ganglia" today usually refers to a functional system that includes components in the <a href="/thesaurus/definition/forebrain-2/"><span class="synonim_bold">forebrain (Goette, 1873)</span></a> and <a href="/thesaurus/definition/midbrain/"><span class="synonim_bold">midbrain (Baer, 1837)</span></a>, rather than to a <a href="/thesaurus/definition/topographic-division/"><span class="synonim_bold">topographic division</span></a> of the <a href="/thesaurus/definition/endbrain/"><span class="synonim_bold">endbrain (Kuhlenbeck, 1927)</span></a>; see Anthoney (1994, pp. 106-109), DeLong & Wichmann (2007), and Federative Committee on Anatomical Terminology (1998, *A14.1.09.501).
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/ http://brancusi1.usc.edu/RDF/entry Basal ganglia
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/ http://brancusi1.usc.edu/RDF/slug basal-ganglia-3
 
//I wonder if this is all the info i need..
//Conducting separate query below in case the the info from node id: "basal-ganglia-of-telencephalon" is needed:
qres = g.query(
     """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
       SELECT ?subject ?predicate ?object
       WHERE {
          ?subject bamsProp:entry "Basal ganglia of" .
          ?subject ?predicate ?object
    	}""")

for r in qres.result:
    print str(r[0]), str(r[1]), str(r[2])
//doesn't work
//However, still going to isolate each part of the triple's results for clarity:

//Running:
	for r in qres.result:
    	print str(r[0])
//Results:
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/

//Running:
	for r in qres.result:
		print str(r[1])
//Results:
	http://brancusi1.usc.edu/RDF/workspace
	http://www.w3.org/1999/02/22-rdf-syntax-ns#type
	http://brancusi1.usc.edu/RDF/reference
	http://brancusi1.usc.edu/RDF/definition
	http://brancusi1.usc.edu/RDF/entry
	http://brancusi1.usc.edu/RDF/slug
	http://brancusi1.usc.edu/RDF/workspace
	http://www.w3.org/1999/02/22-rdf-syntax-ns#type
	http://brancusi1.usc.edu/RDF/reference
	http://brancusi1.usc.edu/RDF/definition
	http://brancusi1.usc.edu/RDF/entry
	http://brancusi1.usc.edu/RDF/slug
	http://brancusi1.usc.edu/RDF/workspace
	http://www.w3.org/1999/02/22-rdf-syntax-ns#type
	http://brancusi1.usc.edu/RDF/reference
	http://brancusi1.usc.edu/RDF/definition
	http://brancusi1.usc.edu/RDF/entry
	http://brancusi1.usc.edu/RDF/slug
	http://brancusi1.usc.edu/RDF/workspace
	http://www.w3.org/1999/02/22-rdf-syntax-ns#type
	http://brancusi1.usc.edu/RDF/reference
	http://brancusi1.usc.edu/RDF/definition
	http://brancusi1.usc.edu/RDF/entry
	http://brancusi1.usc.edu/RDF/slug

//Running:
	for r in qres.result:
		print str(r[2])	
	
//Results:
	0
	http://brancusi1.usc.edu/RDF/thesaurus
	<a target="_blank" href="/thesaurus/reference/carpenter-mb-1976/">Carpenter, 1976</a>
	For macrodissected adult humans it includes the caudate and lenticular nuclei and the amygdala, and is thus not synonymous with <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; p. 496.
	Basal ganglia
	basal-ganglia-4
	0
	http://brancusi1.usc.edu/RDF/thesaurus
	<a target="_blank" href="/thesaurus/reference/ferrier-d-1876/">Ferrier, 1876</a>
	In modern terms includes for macrodissected adult monkeys and humans the <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a> and <a href="/thesaurus/definition/interbrain/"><span class="synonim_bold">interbrain (Baer, 1837)</span></a> considered together; pp. 8, 236.
	Basal ganglia
	basal-ganglia
	0
	http://brancusi1.usc.edu/RDF/thesaurus
	<a target="_blank" href="/thesaurus/reference/strong-os-elwyn-a-1943/">Strong & Elwyn, 1943</a>
	Synonym for basal ganglia of telencephalon (Ranson, 1920) in macrodissected adult humans, and thus not synonymous with <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; p. 319.
	Basal ganglia
	basal-ganglia-2
	0
	http://brancusi1.usc.edu/RDF/thesaurus
	<a target="_blank" href="/thesaurus/reference/warwick-r-williams-pl-eds-1973/">Warwick & Williams, 1973</a>
	Synonym for <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; see Warwick & Williams (1973, p. 805; and Williams & Warwick, 1980, p. 864). Its use is discouraged because reference to <a href="/thesaurus/definition/ganglia/"><span class="synonim_bold">ganglia (Galen, c173)</span></a> in the <a href="/thesaurus/definition/cerebrospinal-axis/"><span class="synonim_bold">cerebrospinal axis (Meckel, 1817)</span></a> is archaic; and because "basal ganglia" today usually refers to a functional system that includes components in the <a href="/thesaurus/definition/forebrain-2/"><span class="synonim_bold">forebrain (Goette, 1873)</span></a> and <a href="/thesaurus/definition/midbrain/"><span class="synonim_bold">midbrain (Baer, 1837)</span></a>, rather than to a <a href="/thesaurus/definition/topographic-division/"><span class="synonim_bold">topographic division</span></a> of the <a href="/thesaurus/definition/endbrain/"><span class="synonim_bold">endbrain (Kuhlenbeck, 1927)</span></a>; see Anthoney (1994, pp. 106-109), DeLong & Wichmann (2007), and Federative Committee on Anatomical Terminology (1998, *A14.1.09.501).
	Basal ganglia
	basal-ganglia-3


//Ran the following to make sure that r[2] contained the last of the content:
	for r in qres.result:
		print str(r[-1])
//Results:
	//same as r[2]
	//success.
	

	





###############################################################################################################################
###############################################################################################################################
###############################################################################################################################
###############################################################################################################################

//Checking other queries:
	qres = g.query(
		 """SELECT ?subject ?predicate 
		   WHERE {
			  ?subject ?predicate ?text .
			  FILTER regex(?text, "^basal", "i")
			}""")
	
	for r in qres.result:
		print str(r[0]), str(r[1])
//Results:
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/ http://brancusi1.usc.edu/RDF/entry
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/ http://brancusi1.usc.edu/RDF/slug
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/ http://brancusi1.usc.edu/RDF/entry
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/ http://brancusi1.usc.edu/RDF/slug
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/ http://brancusi1.usc.edu/RDF/entry
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/ http://brancusi1.usc.edu/RDF/slug
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/ http://brancusi1.usc.edu/RDF/entry
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/ http://brancusi1.usc.edu/RDF/slug
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/entry
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/slug
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/entry
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/slug
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/entry
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/slug