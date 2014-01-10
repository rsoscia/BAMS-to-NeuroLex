# ProgressReport.py
# Progress Report For Zaid





#This is an all encompassing program that does everything at once, hopefully placing all
#of the BAMS query results into a single CSV file
#doesn't run properly unless the path is accessed first, interactive python is activated,
#and the code is pasted into terminal..

#Only run the below persist section once:

#Persist Begin
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

#ADDITIONAL CONTENT
#r = open("../Data/bams_ontology_2013-10-16_20-34-52.xml.zip")

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
#ADDITIONAL CONTENT
#foofile = myzipfile.open('bams_ontology_2013-10-16_20-34-52.xml')

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
#ADDITIONAL CONTENT
#result = g.parse(file=myzipfile.open('bams_ontology_2013-10-16_20-34-52.xml'), format="application/rdf+xml")

foofile.close()

# when done!
g.close()

print("Graph stored to disk")

#WORKS PERFECTLY
#Persist End
#########################################################################################

#For Parsing
import rdflib
from rdflib import plugin

#for getting the length of the files
import os

#for working with tempfiles
import os.path as op
import tempfile

#for csv output
import csv

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

#BAMS Thesaurus content has 3797 items in it
#additional BAMS content (graph) has 167178 items in it




# CHOOSE ONE OF THE FOLLOWING QUERIES

#########################################################################################
#BASAL GANGLIA OF TELENCEPHALON QUERY:
qres = g.query(
	 """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
	   SELECT ?subject ?predicate ?object
	   WHERE {
		  ?subject bamsProp:entry "Basal ganglia of telencephalon" .
		  ?subject ?predicate ?object
		}""")
	
	
#########################################################################################
#// Basal Ganglia Query:
#// Good For Testing Purposes
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



# Open/Write CSV file
# (Copy) Experimental -- best working yet
#########################################################################################
with open('Progress_Report.csv', 'wb') as f:
	BAMS_Dict = {"Subject": qres.result[0][0], "Predicate": qres.result[0][1], "Object": qres.result[0][2]}
	w = csv.DictWriter(f, BAMS_Dict.keys())
	w.writeheader()
	w.writerow(BAMS_Dict)
	for r in qres.result:
		c = csv.writer(open("Progress_Report.csv","wb"))
		c.writerows(qres.result) 
#########################################################################################



































# CSV File Generated Containing BAMS Data From Queries
#########################################################################################

for r in qres.result:
        #print str(r[0]), str(r[1]), str(r[2])
        #print str(r[0][0]) #gives the first position in the first tripple "h" for the url
        
        #c = csv.writer(open("BAMS_Thesaurus_Data4Upload.csv","wb"))
        c = csv.writer(open("BAMS_Formatted_Data.csv","wb"))
        
        c.writerows(qres.result) 


# skip a row
# open the file
# allow program to enter loop and continue to open and insert data into the file




# Experimental -- best working yet
#########################################################################################
with open('BAMS_Formatted_Data.csv', 'wb') as f:
	
	BAMS_Dict = {"Subject": qres.result[0][0], "Predicate": qres.result[0][1], "Object": qres.result[0][2]}
	w = csv.DictWriter(f, BAMS_Dict.keys())
	w.writeheader()
	w.writerow(BAMS_Dict)
	for r in qres.result:
		c = csv.writer(open("BAMS_Formatted_Data.csv","wb"))
		c.writerows(qres.result) 
	#w.writerows(qres.result)
#########################################################################################





#########################################################################################
#with open('mycsvfileV1.csv', 'wb') as f:  # Just use 'w' mode in 3.x
with open('BAMS_Formatted_Data.csv', 'wb') as f:  # Just use 'w' mode in 3.x
	
	
	#First Entire Triple, Second Entire Triple, Third Entire Triple.....
	#BAMS_Dict = {"Subject": qres.result[0], "Predicate": qres.result[1], "Object": qres.result[2]}
	
	#Subject Of First Triple, Predicate Of First Triple, Object Of First Triple.....
	BAMS_Dict = {"Subject": qres.result[0][0], "Predicate": qres.result[0][1], "Object": qres.result[0][2]}
	
	w = csv.DictWriter(f, BAMS_Dict.keys())
	w.writeheader()
	w.writerow(BAMS_Dict)
	
	#Check To See If A DictWriter Library Of Some Sort Is Required For Access To These Methods
	
	
	#for row in BAMS_DICT:
    #out_f.write("%s%s" %(delimiter.join([row[name] for name in f]), lineterminator))
	
	
	#Left off with this vvvvvvvvvv
	#DictWriter.writerows(...)