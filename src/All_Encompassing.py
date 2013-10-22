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
#r = open("../Data/bams_thesaurus_2013-10-06_14-58-56.xml.zip")
#ADDITIONAL CONTENT
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
#ADDITIONAL CONTENT
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
#ADDITIONAL CONTENT
result = g.parse(file=myzipfile.open('bams_ontology_2013-10-16_20-34-52.xml'), format="application/rdf+xml")

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

#additional BAMS content (graph) has 167178 items in it

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


#Test Query:

#qres = g.query(
#     """SELECT ?subject ?predicate 
#       WHERE {
#        ?subject ?predicate ?text .
#        FILTER regex(?text, "^basal", "i")
#      }""")
#  
#for r in qres.result:
#    print str(r[0]), str(r[1])

qres = g.query(
     """SELECT ?subject ?predicate 
       WHERE {
        ?subject ?predicate ?text .
        FILTER regex(?text, "^basal", "i")
      }""")
  
for r in qres.result:
    print str(r[0]), str(r[1])
#WORKS


qres = g.query(
     """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
       SELECT ?subject ?predicate ?object
       WHERE {
          ?subject bamsProp:term "Basal ganglia" .
          ?subject ?predicate ?object
      }""")

for r in qres.result:
    print str(r[0]), str(r[1]), str(r[2])
#DOESN'T WORK

qres = g.query(
     """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
       SELECT ?subject ?predicate ?object
       WHERE {
          ?subject bamsProp:entry "Basal ganglia" .
          ?subject ?predicate ?object
      }""")

for r in qres.result:
    print str(r[0]), str(r[1]), str(r[2])
#DOESN'T WORK






#Query:
	qres = g.query(
		 """SELECT ?subject ?predicate ?text
		   WHERE {
			?subject ?predicate ?text .
			FILTER regex(?text, "^basal", "i")
		  } LIMIT 10""")
	  
	for r in qres.result:
		print str(r[0]), str(r[1])
#works but is not very useful
#Results:
	http://brancusi1.usc.edu/brain_parts/BASAL-AMYGDALOID-NUCLEUS/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/Basal-nucleus-of-the-dorsal-horn-2/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/BASAL-PART-OF-PONS-2/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/basal-nucleus/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/BASAL-PART-OF-PONS/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/BASAL-GANGLIA/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/Basal-nucleus-of-the-dorsal-horn/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/Basal-nucleus-of-the-spinal-cord/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/Basal-nucleus-of-the-spinal-cord-general/ http://brancusi1.usc.edu/RDF/name

##SAME QUERY WITHOUT LIMIT:
	qres = g.query(
		 """SELECT ?subject ?predicate ?text
		   WHERE {
			?subject ?predicate ?text .
			FILTER regex(?text, "^basal", "i")
		  }""")
	  
	for r in qres.result:
		print str(r[0]), str(r[1])

#RESULTS:
	http://brancusi1.usc.edu/brain_parts/BASAL-AMYGDALOID-NUCLEUS/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/Basal-nucleus-of-the-dorsal-horn-2/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/BASAL-PART-OF-PONS-2/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/basal-nucleus/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/BASAL-PART-OF-PONS/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/BASAL-GANGLIA/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/Basal-nucleus-of-the-dorsal-horn/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/Basal-nucleus-of-the-spinal-cord/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/Basal-nucleus-of-the-spinal-cord-general/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/Basal-Nuclei/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/BASAL-AMYGDALOID-NUCLEUS-2/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/BASAL-GANGLIA-2/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/basal-nucleus-3/ http://brancusi1.usc.edu/RDF/name
	N35e0f2dd73d84d0c8dcb3334b284c38d http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/Basal-forebrain/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/Basal-forebrain/ http://brancusi1.usc.edu/RDF/abbreviation
	N302065ddff7141549b427bb769c3022b http://brancusi1.usc.edu/RDF/name
	Nf506bc08a91e4818962a826969fe8172 http://brancusi1.usc.edu/RDF/name
	N9289aa5a064c48f5a242d602414a10f1 http://brancusi1.usc.edu/RDF/name
	Nb6a2af56bb0d4cda9edccaeecc8376e4 http://brancusi1.usc.edu/RDF/name
	Na6a6dc5b86b542e4929d47114f6eac5f http://brancusi1.usc.edu/RDF/name
	N0da72ac281934c8d88838953987fff76 http://brancusi1.usc.edu/RDF/name
	N0c534989ca564785973c6dc0739e78b6 http://brancusi1.usc.edu/RDF/name
	Nffbada52fe87489bbe844e4a93b4716c http://brancusi1.usc.edu/RDF/name
	Nf54dc08a3e44402aa8e4f50131f1685f http://brancusi1.usc.edu/RDF/name
	N32121f94720547a4962c80f6147deda1 http://brancusi1.usc.edu/RDF/name
	N0d3a6c07653c429a9b8e633396876ac1 http://brancusi1.usc.edu/RDF/name
	Nbbff2a068df84b6e87ddef97dd14ef3d http://brancusi1.usc.edu/RDF/name
	N98da41a65c8344a3ac29d46531894bc5 http://brancusi1.usc.edu/RDF/name
	N34a62f7ac79840f3bee6fd1f7dfbf865 http://brancusi1.usc.edu/RDF/name
	N6ff4c6d44a704fe6b308c65afc175c61 http://brancusi1.usc.edu/RDF/name
	N27e76961005b42b4bbe766a1456bf174 http://brancusi1.usc.edu/RDF/name
	N87a432ccb78a483d9f4686aa43a66f10 http://brancusi1.usc.edu/RDF/name
	N007d87b14b864e99a811539b1c92cc2f http://brancusi1.usc.edu/RDF/name
	Naddb806600d6460ebadd9dba870b113d http://brancusi1.usc.edu/RDF/name
	N5d7380b925bb4678a3f74ae5fb0fd5fa http://brancusi1.usc.edu/RDF/name
	N71f3313140fc4e06a4b40120a274b6cd http://brancusi1.usc.edu/RDF/name
	N11650af875d2415ebbca2ecf3097871b http://brancusi1.usc.edu/RDF/name
	Na82968e2e81d4873909f63e11d617c84 http://brancusi1.usc.edu/RDF/name
	N7f725ee50861492e91f737e24f1ec626 http://brancusi1.usc.edu/RDF/name
	N7aa05fa20a7246778b555b8514061f59 http://brancusi1.usc.edu/RDF/name
	Nb0b1017346df4fb796d199f04170888d http://brancusi1.usc.edu/RDF/name
	Nafcf51fd67674d65a0bd90214bc0e27c http://brancusi1.usc.edu/RDF/name
	N35370bb394f3435b87ab1eb1f6a52050 http://brancusi1.usc.edu/RDF/name
	N4cb32a6a50db402d92d944d29c08fe81 http://brancusi1.usc.edu/RDF/name
	N7980bd42e52d47a092243ec22188b7fe http://brancusi1.usc.edu/RDF/name
	Nc5e884b0dfd74e5694046ce392a138b0 http://brancusi1.usc.edu/RDF/name
	N9fecdb3feac84266a5f5ea9d6104136c http://brancusi1.usc.edu/RDF/name
	Nb94e7434c4794252a2ba1b3e46606c93 http://brancusi1.usc.edu/RDF/name
	Nbd36616daecf47b5884755817fab6cb8 http://brancusi1.usc.edu/RDF/name
	Nec66ee43b7b549b383243c1682658f4c http://brancusi1.usc.edu/RDF/name
	N15d39c7921e84b4c81619f8f769b19bd http://brancusi1.usc.edu/RDF/name
	N8cf046f332ad46ffb005875214f7b1d5 http://brancusi1.usc.edu/RDF/name
	N1fc1b317e4f04a86b72e6e82f01c9f44 http://brancusi1.usc.edu/RDF/name
	N4981e26c63404632883bf10762405725 http://brancusi1.usc.edu/RDF/name
	N16e9fdb3042141c28f751784e67e98cb http://brancusi1.usc.edu/RDF/name
	N0e5d1a8f6e7f46b39f4c8072bba4078f http://brancusi1.usc.edu/RDF/name
	N99ea586e35b345baa6b69ccbdd15c80e http://brancusi1.usc.edu/RDF/name
	Nf9a4c5c8840545529a0e4c2b16bd3b11 http://brancusi1.usc.edu/RDF/name
	Nd7938acdfea14d759c8dfbf31f321e93 http://brancusi1.usc.edu/RDF/name
	N8a4fc40eadd4404d9f68c4a64ce63e39 http://brancusi1.usc.edu/RDF/name
	N0e1bd453f25e4625ae55f2133dd4a004 http://brancusi1.usc.edu/RDF/name
	N4bff831afea543c9aaca9ec0eb28161b http://brancusi1.usc.edu/RDF/name
	Ne48b3498521f4c23b780f6a8a38994dd http://brancusi1.usc.edu/RDF/name
	N32f85bfa33ed470d836c04450414ae56 http://brancusi1.usc.edu/RDF/name
	Nc3890065610a414a87b5024340b50e9d http://brancusi1.usc.edu/RDF/name
	Na26618dda70e4123a877ddf951cb8824 http://brancusi1.usc.edu/RDF/name
	Ne4d6872c24744e8ba21e2b9ef4a38c9e http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/basal-nucleus-2/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/basal-nucleus-diffuse-part/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/Basal-nuclear-complex/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/basal-nucleus-compact-part/ http://brancusi1.usc.edu/RDF/name
	N3e06a8740c4743bcbeb4a2dcca8ce499 http://brancusi1.usc.edu/RDF/name
	N2f71200453f34b47a7728b65d82955de http://brancusi1.usc.edu/RDF/chapter
	http://brancusi1.usc.edu/brain_parts/basal-operculum/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/basal-nucleus-of-Meynert/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/basal-ventromedial-nucleus-of-the-thalamus/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/basal-nucleus-Meynert/ http://brancusi1.usc.edu/RDF/name
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia/ http://brancusi1.usc.edu/RDF/name

#Query including the actual name(s):
	qres = g.query(
		 """SELECT ?subject ?predicate ?text
		   WHERE {
			?subject ?predicate ?text .
			FILTER regex(?text, "^basal", "i") .
			?subject ?predicate ?text
		  }""")
	  
	for r in qres.result:
		print str(r[0]), str(r[1]), str(r[2])
#Results:
	http://brancusi1.usc.edu/brain_parts/BASAL-AMYGDALOID-NUCLEUS/ http://brancusi1.usc.edu/RDF/name BASAL AMYGDALOID NUCLEUS
	http://brancusi1.usc.edu/brain_parts/Basal-nucleus-of-the-dorsal-horn-2/ http://brancusi1.usc.edu/RDF/name Basal nucleus of the dorsal horn
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/ http://brancusi1.usc.edu/RDF/name Basal ganglia
	http://brancusi1.usc.edu/brain_parts/BASAL-PART-OF-PONS-2/ http://brancusi1.usc.edu/RDF/name BASAL PART OF PONS
	http://brancusi1.usc.edu/brain_parts/basal-nucleus/ http://brancusi1.usc.edu/RDF/name basal nucleus
	http://brancusi1.usc.edu/brain_parts/BASAL-PART-OF-PONS/ http://brancusi1.usc.edu/RDF/name BASAL PART OF PONS
	http://brancusi1.usc.edu/brain_parts/BASAL-GANGLIA/ http://brancusi1.usc.edu/RDF/name BASAL GANGLIA
	http://brancusi1.usc.edu/brain_parts/Basal-nucleus-of-the-dorsal-horn/ http://brancusi1.usc.edu/RDF/name Basal nucleus of the dorsal horn
	http://brancusi1.usc.edu/brain_parts/Basal-nucleus-of-the-spinal-cord/ http://brancusi1.usc.edu/RDF/name Basal nucleus of the spinal cord
	http://brancusi1.usc.edu/brain_parts/Basal-nucleus-of-the-spinal-cord-general/ http://brancusi1.usc.edu/RDF/name Basal nucleus of the spinal cord, general
	http://brancusi1.usc.edu/brain_parts/Basal-Nuclei/ http://brancusi1.usc.edu/RDF/name Basal Nuclei
	http://brancusi1.usc.edu/brain_parts/BASAL-AMYGDALOID-NUCLEUS-2/ http://brancusi1.usc.edu/RDF/name BASAL AMYGDALOID NUCLEUS
	http://brancusi1.usc.edu/brain_parts/BASAL-GANGLIA-2/ http://brancusi1.usc.edu/RDF/name BASAL GANGLIA
	http://brancusi1.usc.edu/brain_parts/basal-nucleus-3/ http://brancusi1.usc.edu/RDF/name basal nucleus
	N35e0f2dd73d84d0c8dcb3334b284c38d http://brancusi1.usc.edu/RDF/name BASAL PART OF PONS : pontine nuclei
	http://brancusi1.usc.edu/brain_parts/Basal-forebrain/ http://brancusi1.usc.edu/RDF/name Basal forebrain
	http://brancusi1.usc.edu/brain_parts/Basal-forebrain/ http://brancusi1.usc.edu/RDF/abbreviation Basal forebrain
	N302065ddff7141549b427bb769c3022b http://brancusi1.usc.edu/RDF/name BASAL GANGLIA : claustral amygdaloid area
	Nf506bc08a91e4818962a826969fe8172 http://brancusi1.usc.edu/RDF/name BASAL PART OF PONS : longitudinal pontine fibers
	N9289aa5a064c48f5a242d602414a10f1 http://brancusi1.usc.edu/RDF/name Basal ganglia : Striatum
	Nb6a2af56bb0d4cda9edccaeecc8376e4 http://brancusi1.usc.edu/RDF/name BASAL GANGLIA : STRIATUM
	Na6a6dc5b86b542e4929d47114f6eac5f http://brancusi1.usc.edu/RDF/name Basal ganglia : Fundus striati
	N0da72ac281934c8d88838953987fff76 http://brancusi1.usc.edu/RDF/name Basal ganglia : Lateral striatal stripe
	N0c534989ca564785973c6dc0739e78b6 http://brancusi1.usc.edu/RDF/name basal nucleus, diffuse part : nucleus of the ansa peduncularis
	Nffbada52fe87489bbe844e4a93b4716c http://brancusi1.usc.edu/RDF/name BASAL PART OF PONS : longitudinal pontine fibers
	Nf54dc08a3e44402aa8e4f50131f1685f http://brancusi1.usc.edu/RDF/name BASAL GANGLIA : STRIATUM
	N32121f94720547a4962c80f6147deda1 http://brancusi1.usc.edu/RDF/name Basal forebrain : Nucleus accumbens
	N0d3a6c07653c429a9b8e633396876ac1 http://brancusi1.usc.edu/RDF/name Basal nucleus of the dorsal horn : Lateral spinal nucleus
	Nbbff2a068df84b6e87ddef97dd14ef3d http://brancusi1.usc.edu/RDF/name BASAL AMYGDALOID NUCLEUS : lateral part of basal amygdaloid nucleus
	N98da41a65c8344a3ac29d46531894bc5 http://brancusi1.usc.edu/RDF/name basal nucleus of Meynert : basal nucleus, compact part
	N34a62f7ac79840f3bee6fd1f7dfbf865 http://brancusi1.usc.edu/RDF/name Basal nuclear complex : basal nucleus of Meynert
	N6ff4c6d44a704fe6b308c65afc175c61 http://brancusi1.usc.edu/RDF/name Basal Nuclei : Striatum
	N27e76961005b42b4bbe766a1456bf174 http://brancusi1.usc.edu/RDF/name BASAL PART OF PONS : pontine nuclei
	N87a432ccb78a483d9f4686aa43a66f10 http://brancusi1.usc.edu/RDF/name Basal nucleus of the dorsal horn : Lateral cervical nucleus
	N007d87b14b864e99a811539b1c92cc2f http://brancusi1.usc.edu/RDF/name BASAL PART OF PONS : transverse pontine fibers
	Naddb806600d6460ebadd9dba870b113d http://brancusi1.usc.edu/RDF/name Basal nucleus of the spinal cord, general : Basal nucleus of the spinal cord
	N5d7380b925bb4678a3f74ae5fb0fd5fa http://brancusi1.usc.edu/RDF/name BASAL GANGLIA : external capsule
	N71f3313140fc4e06a4b40120a274b6cd http://brancusi1.usc.edu/RDF/name BASAL AMYGDALOID NUCLEUS : lateral part of basal amygdaloid nucleus
	N11650af875d2415ebbca2ecf3097871b http://brancusi1.usc.edu/RDF/name Basal ganglia : Pallidum
	Na82968e2e81d4873909f63e11d617c84 http://brancusi1.usc.edu/RDF/name Basal nucleus of the dorsal horn : Lateral spinal nucleus
	N7f725ee50861492e91f737e24f1ec626 http://brancusi1.usc.edu/RDF/name Basal ganglia : basal nucleus
	N7aa05fa20a7246778b555b8514061f59 http://brancusi1.usc.edu/RDF/name Basal forebrain : Substantia innominata
	Nb0b1017346df4fb796d199f04170888d http://brancusi1.usc.edu/RDF/name Basal Nuclei : Pallidum
	Nafcf51fd67674d65a0bd90214bc0e27c http://brancusi1.usc.edu/RDF/name Basal ganglia : Pallidum
	N35370bb394f3435b87ab1eb1f6a52050 http://brancusi1.usc.edu/RDF/name BASAL PART OF PONS : transverse pontine fibers
	N4cb32a6a50db402d92d944d29c08fe81 http://brancusi1.usc.edu/RDF/name BASAL AMYGDALOID NUCLEUS : medial part of basal amygdaloid nucleus
	N7980bd42e52d47a092243ec22188b7fe http://brancusi1.usc.edu/RDF/name BASAL GANGLIA : extreme capsule
	Nc5e884b0dfd74e5694046ce392a138b0 http://brancusi1.usc.edu/RDF/name Basal ganglia : Interstitial nucleus of the posterior limb of the anterior commissure
	N9fecdb3feac84266a5f5ea9d6104136c http://brancusi1.usc.edu/RDF/name BASAL GANGLIA : GLOBUS PALLIDUS
	Nb94e7434c4794252a2ba1b3e46606c93 http://brancusi1.usc.edu/RDF/name BASAL GANGLIA : claustral amygdaloid area
	Nbd36616daecf47b5884755817fab6cb8 http://brancusi1.usc.edu/RDF/name Basal forebrain : Bed nuclei of the stria terminalis
	Nec66ee43b7b549b383243c1682658f4c http://brancusi1.usc.edu/RDF/name BASAL GANGLIA : AMYGDALA
	N15d39c7921e84b4c81619f8f769b19bd http://brancusi1.usc.edu/RDF/name basal nucleus, diffuse part : Nucleus ansae lenticularis
	N8cf046f332ad46ffb005875214f7b1d5 http://brancusi1.usc.edu/RDF/name BASAL GANGLIA : external capsule
	N1fc1b317e4f04a86b72e6e82f01c9f44 http://brancusi1.usc.edu/RDF/name Basal nucleus of the spinal cord, general : Lateral spinal nucleus
	N4981e26c63404632883bf10762405725 http://brancusi1.usc.edu/RDF/name basal nucleus of Meynert : basal nucleus, diffuse part
	N16e9fdb3042141c28f751784e67e98cb http://brancusi1.usc.edu/RDF/name BASAL PART OF PONS : middle cerebellar peduncle
	N0e5d1a8f6e7f46b39f4c8072bba4078f http://brancusi1.usc.edu/RDF/name Basal forebrain : Putamen
	N99ea586e35b345baa6b69ccbdd15c80e http://brancusi1.usc.edu/RDF/name BASAL GANGLIA : claustrum
	Nf9a4c5c8840545529a0e4c2b16bd3b11 http://brancusi1.usc.edu/RDF/name BASAL GANGLIA : claustrum
	Nd7938acdfea14d759c8dfbf31f321e93 http://brancusi1.usc.edu/RDF/name BASAL GANGLIA : GLOBUS PALLIDUS
	N8a4fc40eadd4404d9f68c4a64ce63e39 http://brancusi1.usc.edu/RDF/name BASAL PART OF PONS : middle cerebellar peduncle
	N0e1bd453f25e4625ae55f2133dd4a004 http://brancusi1.usc.edu/RDF/name BASAL AMYGDALOID NUCLEUS : medial part of basal amygdaloid nucleus
	N4bff831afea543c9aaca9ec0eb28161b http://brancusi1.usc.edu/RDF/name Basal nucleus of the spinal cord, general : Lateral cervical nucleus
	Ne48b3498521f4c23b780f6a8a38994dd http://brancusi1.usc.edu/RDF/name BASAL GANGLIA : AMYGDALA
	N32f85bfa33ed470d836c04450414ae56 http://brancusi1.usc.edu/RDF/name Basal ganglia : bed nucleus of the accessory olfactory tract
	Nc3890065610a414a87b5024340b50e9d http://brancusi1.usc.edu/RDF/name BASAL GANGLIA : extreme capsule
	Na26618dda70e4123a877ddf951cb8824 http://brancusi1.usc.edu/RDF/name Basal nucleus of the dorsal horn : Lateral cervical nucleus
	Ne4d6872c24744e8ba21e2b9ef4a38c9e http://brancusi1.usc.edu/RDF/name Basal ganglia : Striatum
	http://brancusi1.usc.edu/brain_parts/basal-nucleus-2/ http://brancusi1.usc.edu/RDF/name basal nucleus
	http://brancusi1.usc.edu/brain_parts/basal-nucleus-diffuse-part/ http://brancusi1.usc.edu/RDF/name basal nucleus, diffuse part
	http://brancusi1.usc.edu/brain_parts/Basal-nuclear-complex/ http://brancusi1.usc.edu/RDF/name Basal nuclear complex
	http://brancusi1.usc.edu/brain_parts/basal-nucleus-compact-part/ http://brancusi1.usc.edu/RDF/name basal nucleus, compact part
	N3e06a8740c4743bcbeb4a2dcca8ce499 http://brancusi1.usc.edu/RDF/name Basal nucleus of the dorsal horn - equivalent class - Basal nucleus of the spinal cord
	N2f71200453f34b47a7728b65d82955de http://brancusi1.usc.edu/RDF/chapter Basal ganglia
	http://brancusi1.usc.edu/brain_parts/basal-operculum/ http://brancusi1.usc.edu/RDF/name basal operculum
	http://brancusi1.usc.edu/brain_parts/basal-nucleus-of-Meynert/ http://brancusi1.usc.edu/RDF/name basal nucleus of Meynert
	http://brancusi1.usc.edu/brain_parts/basal-ventromedial-nucleus-of-the-thalamus/ http://brancusi1.usc.edu/RDF/name basal ventromedial nucleus of the thalamus
	http://brancusi1.usc.edu/brain_parts/basal-nucleus-Meynert/ http://brancusi1.usc.edu/RDF/name basal nucleus (Meynert)
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia/ http://brancusi1.usc.edu/RDF/name Basal ganglia

#Query:
	qres = g.query(
		 """SELECT ?subject ?predicate ?object
		   WHERE {
			?subject ?predicate ?object .
		  } LIMIT 100""")
	  
	for r in qres.result:
		print str(r[0]), str(r[1]), str(r[2])

#RESULTS:
	http://brancusi1.usc.edu/brain_parts/pineal-gland-3/ http://brancusi1.usc.edu/RDF/description No description provided. The nomenclature was adapted from the atlas.
	http://brancusi1.usc.edu/brain_parts/pineal-gland-3/ http://brancusi1.usc.edu/RDF/grossConstituent http://brancusi1.usc.edu/RDF/grayMatter
	http://brancusi1.usc.edu/brain_parts/pineal-gland-3/ http://brancusi1.usc.edu/RDF/name pineal gland
	http://brancusi1.usc.edu/brain_parts/pineal-gland-3/ http://brancusi1.usc.edu/RDF/nomenclature http://brancusi1.usc.edu/rdf/nomenclature/PaxinosFranklin-2001/
	http://brancusi1.usc.edu/brain_parts/pineal-gland-3/ http://brancusi1.usc.edu/RDF/reference Nccb8a6aab6fb4eedaa16704b7cc865d1
	http://brancusi1.usc.edu/brain_parts/pineal-gland-3/ http://brancusi1.usc.edu/RDF/species http://brancusi1.usc.edu/RDF/mouse
	http://brancusi1.usc.edu/brain_parts/pineal-gland-3/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/brain_parts/pineal-gland-3/ http://brancusi1.usc.edu/RDF/collatorArgument The hierarchy of this region was constructed 
	using the parcellation scheme in this atlas.
	http://brancusi1.usc.edu/brain_parts/pineal-gland-3/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/brainPart
	http://brancusi1.usc.edu/brain_parts/pineal-gland-3/ http://brancusi1.usc.edu/RDF/collatorInvolvement http://brancusi1.usc.edu/RDF/expertiseAndCollationNomenclatureCitedReferences
	http://brancusi1.usc.edu/brain_parts/pineal-gland-3/ http://brancusi1.usc.edu/RDF/abbreviation Pi
	http://brancusi1.usc.edu/brain_parts/pineal-gland-3/ http://brancusi1.usc.edu/RDF/collationDate 2003-02-27
	http://brancusi1.usc.edu/brain_parts/pineal-gland-3/ http://brancusi1.usc.edu/RDF/collator 510
	http://brancusi1.usc.edu/brain_parts/ventromedial-hypothalamic-nucleus-central-part-3/ http://brancusi1.usc.edu/RDF/description No description provided. The nomenclature was adapted from the atlas.
	http://brancusi1.usc.edu/brain_parts/ventromedial-hypothalamic-nucleus-central-part-3/ http://brancusi1.usc.edu/RDF/grossConstituent http://brancusi1.usc.edu/RDF/grayMatter
	http://brancusi1.usc.edu/brain_parts/ventromedial-hypothalamic-nucleus-central-part-3/ http://brancusi1.usc.edu/RDF/name ventromedial hypothalamic nucleus central part
	http://brancusi1.usc.edu/brain_parts/ventromedial-hypothalamic-nucleus-central-part-3/ http://brancusi1.usc.edu/RDF/nomenclature http://brancusi1.usc.edu/rdf/nomenclature/PaxinosFranklin-2001/
	http://brancusi1.usc.edu/brain_parts/ventromedial-hypothalamic-nucleus-central-part-3/ http://brancusi1.usc.edu/RDF/reference Nccb8a6aab6fb4eedaa16704b7cc865d1
	http://brancusi1.usc.edu/brain_parts/ventromedial-hypothalamic-nucleus-central-part-3/ http://brancusi1.usc.edu/RDF/species http://brancusi1.usc.edu/RDF/mouse
	http://brancusi1.usc.edu/brain_parts/ventromedial-hypothalamic-nucleus-central-part-3/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/brain_parts/ventromedial-hypothalamic-nucleus-central-part-3/ http://brancusi1.usc.edu/RDF/collatorArgument The hierarchy of this region was constructed using the rat atlas Paxinos and Watson 1998 and Simerly 1995. 
	See also Swanson 1992.
	http://brancusi1.usc.edu/brain_parts/ventromedial-hypothalamic-nucleus-central-part-3/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/brainPart
	http://brancusi1.usc.edu/brain_parts/ventromedial-hypothalamic-nucleus-central-part-3/ http://brancusi1.usc.edu/RDF/collatorInvolvement http://brancusi1.usc.edu/RDF/expertiseAndCollationNomenclatureCitedReferences
	http://brancusi1.usc.edu/brain_parts/ventromedial-hypothalamic-nucleus-central-part-3/ http://brancusi1.usc.edu/RDF/abbreviation VMHC
	http://brancusi1.usc.edu/brain_parts/ventromedial-hypothalamic-nucleus-central-part-3/ http://brancusi1.usc.edu/RDF/collationDate 2003-02-27
	http://brancusi1.usc.edu/brain_parts/ventromedial-hypothalamic-nucleus-central-part-3/ http://brancusi1.usc.edu/RDF/collator 510
	http://brancusi1.usc.edu/brain_parts/optic-nerve-layer-of-the-superior-colliculus-2/ http://brancusi1.usc.edu/RDF/description No description provided. The nomenclature was adapted from the atlas.
	http://brancusi1.usc.edu/brain_parts/optic-nerve-layer-of-the-superior-colliculus-2/ http://brancusi1.usc.edu/RDF/grossConstituent http://brancusi1.usc.edu/RDF/grayMatter
	http://brancusi1.usc.edu/brain_parts/optic-nerve-layer-of-the-superior-colliculus-2/ http://brancusi1.usc.edu/RDF/name optic nerve layer of the superior colliculus
	http://brancusi1.usc.edu/brain_parts/optic-nerve-layer-of-the-superior-colliculus-2/ http://brancusi1.usc.edu/RDF/nomenclature http://brancusi1.usc.edu/rdf/nomenclature/PaxinosFranklin-2001/
	http://brancusi1.usc.edu/brain_parts/optic-nerve-layer-of-the-superior-colliculus-2/ http://brancusi1.usc.edu/RDF/reference Nccb8a6aab6fb4eedaa16704b7cc865d1
	http://brancusi1.usc.edu/brain_parts/optic-nerve-layer-of-the-superior-colliculus-2/ http://brancusi1.usc.edu/RDF/species http://brancusi1.usc.edu/RDF/mouse
	http://brancusi1.usc.edu/brain_parts/optic-nerve-layer-of-the-superior-colliculus-2/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/brain_parts/optic-nerve-layer-of-the-superior-colliculus-2/ http://brancusi1.usc.edu/RDF/collatorArgument The hierarchy of this region was constructed 
	using the parcellation scheme in this atlas and the information collated from Bowden 2002.
	http://brancusi1.usc.edu/brain_parts/optic-nerve-layer-of-the-superior-colliculus-2/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/brainPart
	http://brancusi1.usc.edu/brain_parts/optic-nerve-layer-of-the-superior-colliculus-2/ http://brancusi1.usc.edu/RDF/collatorInvolvement http://brancusi1.usc.edu/RDF/expertiseAndCollationNomenclatureCitedReferences
	http://brancusi1.usc.edu/brain_parts/optic-nerve-layer-of-the-superior-colliculus-2/ http://brancusi1.usc.edu/RDF/abbreviation Op
	http://brancusi1.usc.edu/brain_parts/optic-nerve-layer-of-the-superior-colliculus-2/ http://brancusi1.usc.edu/RDF/collationDate 2003-02-27
	http://brancusi1.usc.edu/brain_parts/optic-nerve-layer-of-the-superior-colliculus-2/ http://brancusi1.usc.edu/RDF/collator 510
	http://brancusi1.usc.edu/brain_parts/spinal-trigeminal-nucleus-oral-part-2/ http://brancusi1.usc.edu/RDF/description No description provided. The nomenclature was adapted from the atlas.
	http://brancusi1.usc.edu/brain_parts/spinal-trigeminal-nucleus-oral-part-2/ http://brancusi1.usc.edu/RDF/grossConstituent http://brancusi1.usc.edu/RDF/grayMatter
	http://brancusi1.usc.edu/brain_parts/spinal-trigeminal-nucleus-oral-part-2/ http://brancusi1.usc.edu/RDF/name spinal trigeminal nucleus oral part
	http://brancusi1.usc.edu/brain_parts/spinal-trigeminal-nucleus-oral-part-2/ http://brancusi1.usc.edu/RDF/nomenclature http://brancusi1.usc.edu/rdf/nomenclature/PaxinosFranklin-2001/
	http://brancusi1.usc.edu/brain_parts/spinal-trigeminal-nucleus-oral-part-2/ http://brancusi1.usc.edu/RDF/reference Nccb8a6aab6fb4eedaa16704b7cc865d1
	http://brancusi1.usc.edu/brain_parts/spinal-trigeminal-nucleus-oral-part-2/ http://brancusi1.usc.edu/RDF/species http://brancusi1.usc.edu/RDF/mouse
	http://brancusi1.usc.edu/brain_parts/spinal-trigeminal-nucleus-oral-part-2/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/brain_parts/spinal-trigeminal-nucleus-oral-part-2/ http://brancusi1.usc.edu/RDF/collatorArgument The hierarchy of this region was constructed 
	using the parcellation scheme in this atlas.
	http://brancusi1.usc.edu/brain_parts/spinal-trigeminal-nucleus-oral-part-2/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/brainPart
	http://brancusi1.usc.edu/brain_parts/spinal-trigeminal-nucleus-oral-part-2/ http://brancusi1.usc.edu/RDF/collatorInvolvement http://brancusi1.usc.edu/RDF/expertiseAndCollationNomenclatureCitedReferences
	http://brancusi1.usc.edu/brain_parts/spinal-trigeminal-nucleus-oral-part-2/ http://brancusi1.usc.edu/RDF/abbreviation Sp5O
	http://brancusi1.usc.edu/brain_parts/spinal-trigeminal-nucleus-oral-part-2/ http://brancusi1.usc.edu/RDF/collationDate 2003-02-27
	http://brancusi1.usc.edu/brain_parts/spinal-trigeminal-nucleus-oral-part-2/ http://brancusi1.usc.edu/RDF/collator 510
	http://brancusi1.usc.edu/brain_parts/medial-amygdaloid-nucleus-anterior-dorsal/ http://brancusi1.usc.edu/RDF/description No description provided. The nomenclature was adapted from the atlas.
	http://brancusi1.usc.edu/brain_parts/medial-amygdaloid-nucleus-anterior-dorsal/ http://brancusi1.usc.edu/RDF/grossConstituent http://brancusi1.usc.edu/RDF/grayMatter
	http://brancusi1.usc.edu/brain_parts/medial-amygdaloid-nucleus-anterior-dorsal/ http://brancusi1.usc.edu/RDF/name medial amygdaloid nucleus anterior dorsal
	http://brancusi1.usc.edu/brain_parts/medial-amygdaloid-nucleus-anterior-dorsal/ http://brancusi1.usc.edu/RDF/nomenclature http://brancusi1.usc.edu/rdf/nomenclature/PaxinosFranklin-2001/
	http://brancusi1.usc.edu/brain_parts/medial-amygdaloid-nucleus-anterior-dorsal/ http://brancusi1.usc.edu/RDF/reference Nccb8a6aab6fb4eedaa16704b7cc865d1
	http://brancusi1.usc.edu/brain_parts/medial-amygdaloid-nucleus-anterior-dorsal/ http://brancusi1.usc.edu/RDF/species http://brancusi1.usc.edu/RDF/mouse
	http://brancusi1.usc.edu/brain_parts/medial-amygdaloid-nucleus-anterior-dorsal/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/brain_parts/medial-amygdaloid-nucleus-anterior-dorsal/ http://brancusi1.usc.edu/RDF/collatorArgument The hierarchy of this region was constructed using the rat brain atlas Paxinos and Watson 1986, 
	and Alheid et al. 1995. See also Swanson 1992
	http://brancusi1.usc.edu/brain_parts/medial-amygdaloid-nucleus-anterior-dorsal/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/brainPart
	http://brancusi1.usc.edu/brain_parts/medial-amygdaloid-nucleus-anterior-dorsal/ http://brancusi1.usc.edu/RDF/collatorInvolvement http://brancusi1.usc.edu/RDF/expertiseAndCollationNomenclatureCitedReferences
	http://brancusi1.usc.edu/brain_parts/medial-amygdaloid-nucleus-anterior-dorsal/ http://brancusi1.usc.edu/RDF/abbreviation MeAD
	http://brancusi1.usc.edu/brain_parts/medial-amygdaloid-nucleus-anterior-dorsal/ http://brancusi1.usc.edu/RDF/collationDate 2003-02-27
	http://brancusi1.usc.edu/brain_parts/medial-amygdaloid-nucleus-anterior-dorsal/ http://brancusi1.usc.edu/RDF/collator 510
	http://brancusi1.usc.edu/brain_parts/central-amygdaloid-nucleus-medial-division-anteroventral-part/ http://brancusi1.usc.edu/RDF/description No description provided. The nomenclature was adapted from the atlas.
	http://brancusi1.usc.edu/brain_parts/central-amygdaloid-nucleus-medial-division-anteroventral-part/ http://brancusi1.usc.edu/RDF/grossConstituent http://brancusi1.usc.edu/RDF/grayMatter
	http://brancusi1.usc.edu/brain_parts/central-amygdaloid-nucleus-medial-division-anteroventral-part/ http://brancusi1.usc.edu/RDF/name central amygdaloid nucleus medial division anteroventral part
	http://brancusi1.usc.edu/brain_parts/central-amygdaloid-nucleus-medial-division-anteroventral-part/ http://brancusi1.usc.edu/RDF/nomenclature http://brancusi1.usc.edu/rdf/nomenclature/PaxinosFranklin-2001/
	http://brancusi1.usc.edu/brain_parts/central-amygdaloid-nucleus-medial-division-anteroventral-part/ http://brancusi1.usc.edu/RDF/reference Nccb8a6aab6fb4eedaa16704b7cc865d1
	http://brancusi1.usc.edu/brain_parts/central-amygdaloid-nucleus-medial-division-anteroventral-part/ http://brancusi1.usc.edu/RDF/species http://brancusi1.usc.edu/RDF/mouse
	http://brancusi1.usc.edu/brain_parts/central-amygdaloid-nucleus-medial-division-anteroventral-part/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/brain_parts/central-amygdaloid-nucleus-medial-division-anteroventral-part/ http://brancusi1.usc.edu/RDF/collatorArgument The hierarchy of this region was constructed using the rat brain atlas Paxinos and Watson 1986, 
	and Alheid et al. 1995. See also Swanson 1992
	http://brancusi1.usc.edu/brain_parts/central-amygdaloid-nucleus-medial-division-anteroventral-part/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/brainPart
	http://brancusi1.usc.edu/brain_parts/central-amygdaloid-nucleus-medial-division-anteroventral-part/ http://brancusi1.usc.edu/RDF/collatorInvolvement http://brancusi1.usc.edu/RDF/expertiseAndCollationNomenclatureCitedReferences
	http://brancusi1.usc.edu/brain_parts/central-amygdaloid-nucleus-medial-division-anteroventral-part/ http://brancusi1.usc.edu/RDF/abbreviation CeMAV
	http://brancusi1.usc.edu/brain_parts/central-amygdaloid-nucleus-medial-division-anteroventral-part/ http://brancusi1.usc.edu/RDF/collationDate 2003-02-27
	http://brancusi1.usc.edu/brain_parts/central-amygdaloid-nucleus-medial-division-anteroventral-part/ http://brancusi1.usc.edu/RDF/collator 510
	http://brancusi1.usc.edu/brain_parts/ventromedial-preoptic-nucleus-2/ http://brancusi1.usc.edu/RDF/description No description provided. The nomenclature was adapted from the atlas.
	http://brancusi1.usc.edu/brain_parts/ventromedial-preoptic-nucleus-2/ http://brancusi1.usc.edu/RDF/grossConstituent http://brancusi1.usc.edu/RDF/grayMatter
	http://brancusi1.usc.edu/brain_parts/ventromedial-preoptic-nucleus-2/ http://brancusi1.usc.edu/RDF/name ventromedial preoptic nucleus
	http://brancusi1.usc.edu/brain_parts/ventromedial-preoptic-nucleus-2/ http://brancusi1.usc.edu/RDF/nomenclature http://brancusi1.usc.edu/rdf/nomenclature/PaxinosFranklin-2001/
	http://brancusi1.usc.edu/brain_parts/ventromedial-preoptic-nucleus-2/ http://brancusi1.usc.edu/RDF/reference Nccb8a6aab6fb4eedaa16704b7cc865d1
	http://brancusi1.usc.edu/brain_parts/ventromedial-preoptic-nucleus-2/ http://brancusi1.usc.edu/RDF/species http://brancusi1.usc.edu/RDF/mouse
	http://brancusi1.usc.edu/brain_parts/ventromedial-preoptic-nucleus-2/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/brain_parts/ventromedial-preoptic-nucleus-2/ http://brancusi1.usc.edu/RDF/collatorArgument The hierarchy of this region was constructed using the rat atlas Paxinos and Watson 1998 and Simerly 1995. 
	See also Swanson 1992.
	http://brancusi1.usc.edu/brain_parts/ventromedial-preoptic-nucleus-2/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/brainPart
	http://brancusi1.usc.edu/brain_parts/ventromedial-preoptic-nucleus-2/ http://brancusi1.usc.edu/RDF/collatorInvolvement http://brancusi1.usc.edu/RDF/expertiseAndCollationNomenclatureCitedReferences
	http://brancusi1.usc.edu/brain_parts/ventromedial-preoptic-nucleus-2/ http://brancusi1.usc.edu/RDF/abbreviation VMPO
	http://brancusi1.usc.edu/brain_parts/ventromedial-preoptic-nucleus-2/ http://brancusi1.usc.edu/RDF/collationDate 2003-02-27
	http://brancusi1.usc.edu/brain_parts/ventromedial-preoptic-nucleus-2/ http://brancusi1.usc.edu/RDF/collator 510
	http://brancusi1.usc.edu/brain_parts/lateral-septal-nucleus-5/ http://brancusi1.usc.edu/RDF/description No description provided. The nomenclature was adapted from the atlas.
	http://brancusi1.usc.edu/brain_parts/lateral-septal-nucleus-5/ http://brancusi1.usc.edu/RDF/grossConstituent http://brancusi1.usc.edu/RDF/grayMatter
	http://brancusi1.usc.edu/brain_parts/lateral-septal-nucleus-5/ http://brancusi1.usc.edu/RDF/name lateral septal nucleus
	http://brancusi1.usc.edu/brain_parts/lateral-septal-nucleus-5/ http://brancusi1.usc.edu/RDF/nomenclature http://brancusi1.usc.edu/rdf/nomenclature/PaxinosFranklin-2001/
	http://brancusi1.usc.edu/brain_parts/lateral-septal-nucleus-5/ http://brancusi1.usc.edu/RDF/reference Nccb8a6aab6fb4eedaa16704b7cc865d1
	http://brancusi1.usc.edu/brain_parts/lateral-septal-nucleus-5/ http://brancusi1.usc.edu/RDF/species http://brancusi1.usc.edu/RDF/mouse
	http://brancusi1.usc.edu/brain_parts/lateral-septal-nucleus-5/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/brain_parts/lateral-septal-nucleus-5/ http://brancusi1.usc.edu/RDF/collatorArgument The hierarchy of this region was constructed 
	using Jakab and Leranth 1995. See also Swanson 1992
	http://brancusi1.usc.edu/brain_parts/lateral-septal-nucleus-5/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/brainPart






#This actually works

##CONSTRUCTING THE QUERIES TO GET THE RIGHT INFO:
######################################################################################################
######################################################################################################
#BASAL GANGLIA QUERY (note:everything is tabbed right one):
	qres = g.query(
		 """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
		   SELECT ?subject ?predicate ?object
		   WHERE {
			  ?subject bamsProp:name "Basal ganglia" .
			  ?subject ?predicate ?object
			}""")
	
	for r in qres.result:
		print str(r[0]), str(r[1]), str(r[2])

#RESULTS:
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/ http://brancusi1.usc.edu/RDF/description No description provided. Collator note: Abbreviation of this brain part was inserted by the collator.See the human brain nomenclature Bowden 2000.
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/ http://brancusi1.usc.edu/RDF/grossConstituent http://brancusi1.usc.edu/RDF/grayMatter
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/ http://brancusi1.usc.edu/RDF/name Basal ganglia
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/ http://brancusi1.usc.edu/RDF/nomenclature http://brancusi1.usc.edu/rdf/nomenclature/Hof-et-al-2000/
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/ http://brancusi1.usc.edu/RDF/reference N539fbbc6f7ee43bea86cfe4614cd1ce5
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/ http://brancusi1.usc.edu/RDF/species http://brancusi1.usc.edu/RDF/mouse
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/brainPart
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/ http://brancusi1.usc.edu/RDF/abbreviation BG
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/ http://brancusi1.usc.edu/RDF/collationDate 2003-11-28
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/ http://brancusi1.usc.edu/RDF/collator 516
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia/ http://brancusi1.usc.edu/RDF/description Collator note: this region does not appear in the list of structures, nor in the the list of abbreviations, but is used as a superstructure in the section of delineation criteria of the mouse regions.
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia/ http://brancusi1.usc.edu/RDF/grossConstituent http://brancusi1.usc.edu/RDF/grayMatter
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia/ http://brancusi1.usc.edu/RDF/name Basal ganglia
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia/ http://brancusi1.usc.edu/RDF/nomenclature http://brancusi1.usc.edu/rdf/nomenclature/PaxinosFranklin-2001/
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia/ http://brancusi1.usc.edu/RDF/reference Nccb8a6aab6fb4eedaa16704b7cc865d1
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia/ http://brancusi1.usc.edu/RDF/species http://brancusi1.usc.edu/RDF/mouse
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia/ http://brancusi1.usc.edu/RDF/collatorArgument The hierarchy was constructed from the associated atlas.
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/brainPart
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia/ http://brancusi1.usc.edu/RDF/collatorInvolvement http://brancusi1.usc.edu/RDF/expertiseAndCollationNomenclatureCitedReferences
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia/ http://brancusi1.usc.edu/RDF/abbreviation BG
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia/ http://brancusi1.usc.edu/RDF/collationDate 2003-04-16
	http://brancusi1.usc.edu/brain_parts/Basal-ganglia/ http://brancusi1.usc.edu/RDF/collator 510
######################################################################################################
######################################################################################################


######################################################################################################
######################################################################################################
#(MODIFIED) BASAL GANGLIA QUERY (note:everything is tabbed right one):
	qres = g.query(
		 """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
		   SELECT ?subject ?predicate ?object
		   WHERE {
			  ?object bamsProp:name "Basal ganglia" .
			  ?subject ?predicate ?object
			}""")
	
	for r in qres.result:
		print str(r[0]), str(r[1]), str(r[2])

#RESULTS:
	N9289aa5a064c48f5a242d602414a10f1 http://brancusi1.usc.edu/RDF/class1 http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/
	Na6a6dc5b86b542e4929d47114f6eac5f http://brancusi1.usc.edu/RDF/class1 http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/
	N0da72ac281934c8d88838953987fff76 http://brancusi1.usc.edu/RDF/class1 http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/
	N11650af875d2415ebbca2ecf3097871b http://brancusi1.usc.edu/RDF/class1 http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/
	N81e4e6e8891e42338caa6e5742060071 http://brancusi1.usc.edu/RDF/class2 http://brancusi1.usc.edu/brain_parts/Basal-ganglia-2/
	Nf868f21d20604feba0c04303c92849b6 http://brancusi1.usc.edu/RDF/class2 http://brancusi1.usc.edu/brain_parts/Basal-ganglia/
	N7f725ee50861492e91f737e24f1ec626 http://brancusi1.usc.edu/RDF/class1 http://brancusi1.usc.edu/brain_parts/Basal-ganglia/
	Nafcf51fd67674d65a0bd90214bc0e27c http://brancusi1.usc.edu/RDF/class1 http://brancusi1.usc.edu/brain_parts/Basal-ganglia/
	Nc5e884b0dfd74e5694046ce392a138b0 http://brancusi1.usc.edu/RDF/class1 http://brancusi1.usc.edu/brain_parts/Basal-ganglia/
	N32f85bfa33ed470d836c04450414ae56 http://brancusi1.usc.edu/RDF/class1 http://brancusi1.usc.edu/brain_parts/Basal-ganglia/
	Ne4d6872c24744e8ba21e2b9ef4a38c9e http://brancusi1.usc.edu/RDF/class1 http://brancusi1.usc.edu/brain_parts/Basal-ganglia/
######################################################################################################
######################################################################################################








##THE CURRENT RESULTS THAT ARE PUBLISHED IN THE tempVTest.csv document belong to
##"BASAL GANGLIA QUERY" -- aka the second to last query

import csv

for r in qres.result:
	#print str(r[0]), str(r[1]), str(r[2])
	c = csv.writer(open("tempVTest.csv","wb"))
	
	# gives us the triple info in each cell (notice it's not in string format) it's pretty ugly
	#c.writerow(qres.result)
	# regardless of the format, i'm going to index this first
	# figure out how to place at the next 
	
	# need to access each individual part of the triple
	# making row plural allows for this type of functionality
	
	c.writerows(qres.result)
	

