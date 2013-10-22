#SPARQL_BAMS_Store_Persist_Example.py
#This program is used to open up BAMS data, persist it to a store for speed up of querying
#This document is currently working with the Fixed RDF BAMS Thesaurus Data

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