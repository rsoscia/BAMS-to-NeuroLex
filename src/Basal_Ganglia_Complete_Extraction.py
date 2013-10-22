#RUN A MODIFIED VERSION OF SPARQL_BAMS_Store_Persist_Example.py AFTER ENTERING INTERACTIVE PYTHON

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
#r = open("../Data/bams_thesaurus_2013-10-06_14-58-56.xml.zip")

# adding the additional content (to check to see if the anchor tags need to be removed
# on this file as well
r = open("../Data/bams_ontology_2013-10-16_20-34-52.xml.zip")


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
#foofile = myzipfile.open('bams_thesaurus_2013-10-06_14-58-56.xml')

# additional BAMS content (rather than the thesaurus)
foofile = myzipfile.open('bams_ontology_2013-10-16_20-34-52.xml')

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
#result = g.parse(file=myzipfile.open('bams_thesaurus_2013-10-06_14-58-56.xml'), format="application/rdf+xml")

result = g.parse(file=myzipfile.open('bams_ontology_2013-10-16_20-34-52.xml', format="application/rdf+xml")

foofile.close()

# when done!
g.close()

print("Graph stored to disk")


##WORKS PERFECTLY
##Don't think it works perfectly... needs the persist example from All_Encompassing.py

#########################################################################################
#########################################################################################
#########################################################################################

#RUN THIS CUTOFF VERSION OF SPARQL_BAMS_Store_Query_Example.py IN ORDER TO RUN SPECIALIZED QUERIES


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


print("The graph has " + str(len(g)) + " items in it")

##THE ADDITIONAL BAMS CONTENT HAS A GRAPH CONTAINING 3797 ITEMS IN IT



























#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

BELOW IS CODE FOR QUERIES:

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#This is a document containing the complete results from the BAMS Thesaurus (fixed) basal ganglia data extraction
#The queries are below and rely on two other sets of code: One is SPARQL_BAMS_Store_Persist_Example.py and the other
#is SPARQL_BAMS_Store_Query_Example.py


#BASAL GANGLIA OF TELENCEPHALON QUERY:
	qres = g.query(
		 """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
		   SELECT ?subject ?predicate ?object
		   WHERE {
			  ?subject bamsProp:entry "Basal ganglia of telencephalon" .
			  ?subject ?predicate ?object
			}""")
	
	for r in qres.result:
		print str(r[0]), str(r[1]), str(r[2])

#QUERY RESULTS FROM THE ADDITIONAL BAMS CONTENT:
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/ranson-sw-1920/">Ranson, 1920</a>
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/definition For macrodissected adult humans it includes the caudate and lentiform (putamen and globus pallidus) nuclei, amygdala, and claustrum (p. 252) and is thus not synonymous with <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>. More recently it was used in Ranson's sense by for example Clark (1951, p. 968).
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/entry Basal ganglia of telencephalon
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/slug basal-ganglia-of-telencephalon
	
	
	##RESULTS (FROM BAMS THESAURUS QUERIES --- RESULTS BELOW ARE JUST FOR COMPARISON):
		http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/workspace 0
		http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
		http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/ranson-sw-1920/">Ranson, 1920</a>
		http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/definition For macrodissected adult humans it includes the caudate and lentiform (putamen and globus pallidus) nuclei, amygdala, and claustrum (p. 252) and is thus not synonymous with <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>. More recently it was used in Ranson's sense by for example Clark (1951, p. 968).
		http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/entry Basal ganglia of telencephalon
		http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/slug basal-ganglia-of-telencephalon

#BASAL GANGLIA QUERY:
	qres = g.query(
		 """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
		   SELECT ?subject ?predicate ?object
		   WHERE {
			  ?subject bamsProp:entry "Basal ganglia" .
			  ?subject ?predicate ?object
			}""")
	
	for r in qres.result:
		print str(r[0]), str(r[1]), str(r[2])

#QUERY RESULTS FROM THE ADDITIONAL BAMS CONTENT:
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


	##RESULTS (FROM BAMS THESAURUS QUERIES --- RESULTS BELOW ARE JUST FOR COMPARISON)::
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
	
#BASAL NUCLEI QUERY:
	qres = g.query(
		 """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
		   SELECT ?subject ?predicate ?object
		   WHERE {
			  ?subject bamsProp:entry "Basal nuclei" .
			  ?subject ?predicate ?object
			}""")
	
	for r in qres.result:
		print str(r[0]), str(r[1]), str(r[2])

#QUERY RESULTS FROM THE ADDITIONAL BAMS CONTENT:
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/clark-weleg-1951/">Clark, 1951</a>
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/definition Synonym for basal ganglia (Strong & Elwyn, 1943) in macrodissected adult humans, and thus not synonymous with <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; p. 968. Others employing this usage include Warwick & Williams (1973, p. 976; and Williams & Warwick, 1980, p. 1032), International Anatomical Nomenclature Committee (1983, p. A72).
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/entry Basal nuclei
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/slug basal-nuclei
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/warwick-r-williams-pl-eds-1973/">Warwick & Williams, 1973</a>
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/definition Synonym for <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; see Warwick & Williams (1973, p. 805; and Williams & Warwick, 1980, p. 864) and Swanson (1998, p. 200).
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/entry Basal nuclei
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/slug basal-nuclei-2


	##RESULTS:
		http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/workspace 0
		http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
		http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/clark-weleg-1951/">Clark, 1951</a>
		http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/definition Synonym for basal ganglia (Strong & Elwyn, 1943) in macrodissected adult humans, and thus not synonymous with <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; p. 968. Others employing this usage include Warwick & Williams (1973, p. 976; and Williams & Warwick, 1980, p. 1032), International Anatomical Nomenclature Committee (1983, p. A72).
		http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/entry Basal nuclei
		http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/slug basal-nuclei
		http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/workspace 0
		http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
		http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/warwick-r-williams-pl-eds-1973/">Warwick & Williams, 1973</a>
		http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/definition Synonym for <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; see Warwick & Williams (1973, p. 805; and Williams & Warwick, 1980, p. 864) and Swanson (1998, p. 200).
		http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/entry Basal nuclei
		http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/slug basal-nuclei-2
		

#RESULTS FROM COMPARISON OF ADDITIONAL DATA TO THE FIXED BAMS THESAURUS DATA:
#THEY ARE IDENTICAL (MEANING PRODUCE THE SAME OUTPUTS FORM THE SAME BASAL GANGLIA QUERIES)



#BEGINNING TO ADD THE CSV CODE:
import csv

for r in qres.result:
	#print str(r[0]), str(r[1]), str(r[2])
	c = csv.writer(open("temp.csv","wb"))
	
	# gives us the triple info in each cell (notice it's not in string format) it's pretty ugly
	#c.writerow(qres.result)
	# regardless of the format, i'm going to index this first
	# figure out how to place at the next 
	
	# need to access each individual part of the triple
	# making row plural allows for this type of functionality
	
	#subject = (qres.result)
	#predicate = str(r[1])
	#object = str(r[2])
	
	#c.writerows(subject)
	
	c.writerows(qres.result)
	
	print("The graph has " + str(len(g)) + " items in it")
	print("The graph has " + str(len(r)) + " items in it")
	
	
	
	
	#c.writerows(str(r[0]))
	#c.writerows(r[0])
	#c.writerows(r)
	
	
	#the best way to do this 
	
	
	#c.writerow(r)
	#c.writecol(qres.result)



